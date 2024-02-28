import cv2
import numpy as np
from cv2 import aruco

camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'
window_name1 = 'OpenCV QR Code2'
cap = cv2.VideoCapture(camera_id)
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
aruco_params = aruco.DetectorParameters()
aruco_params.useAruco3Detection = True
correl = 0
aruco_corners = []
text = ""
show_detected = False


def check_if_correct(diff1, diff2, diff3, diff4):
    EPS = 20
    is_correct = abs(diff1 - diff2) < EPS and abs(diff1 - diff3) < EPS and abs(diff1 - diff4) < EPS
    return is_correct


while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        corners, ids, rejected = aruco.detectMarkers(thresholded, aruco_dict, parameters=aruco_params)
        if ids is not None:
            if corners:
                print("Something detected!")
                aruco_ids = []
                for i in range(len(corners)):
                    x1, x2, x3, x4 = corners[i][0][0][0], corners[i][0][1][0], corners[i][0][2][0], corners[i][0][3][0]
                    y1, y2, y3, y4 = corners[i][0][0][1], corners[i][0][1][1], corners[i][0][2][1], corners[i][0][3][1]
                    start_x, start_y = x1, y1
                    end_x, end_y = x3, y3
                    aruco_region = frame[int(y1):int(y4), int(x1):int(x2)]
                    aruco_hist = cv2.calcHist([aruco_region], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
                    surrounding_area = frame[int(y1) - 10:int(y4) + 10, int(x1) - 10:int(x2) + 10]
                    surrounding_area_hist = cv2.calcHist([surrounding_area], [0, 1, 2], None, [8, 8, 8],
                                                         [0, 256, 0, 256, 0, 256])
                    correl = cv2.compareHist(aruco_hist, surrounding_area_hist, cv2.HISTCMP_CORREL)
                    if start_x < end_x and start_y < end_y:
                        text = "UP"
                        diff1, diff2, diff3, diff4 = abs(x1 - x2), abs(y4 - y1), abs(y3 - y2), abs(x3 - x4)
                        show_detected = check_if_correct(diff1, diff2, diff3, diff4)
                    elif start_x > end_x and start_y < end_y:
                        text = "RIGHT"
                        diff1, diff2, diff3, diff4 = abs(y1 - y2), abs(x2 - x3), abs(y3 - y4), abs(x4 - x1)
                        show_detected = check_if_correct(diff1, diff2, diff3, diff4)
                    elif start_x > end_x and start_y > end_y:
                        text = "DOWN"
                        diff1, diff2, diff3, diff4 = abs(x1 - x2), abs(y4 - y1), abs(y3 - y2), abs(x3 - x4)
                        show_detected = check_if_correct(diff1, diff2, diff3, diff4)
                    elif start_x < end_x and start_y > end_y:
                        text = "LEFT"
                        diff1, diff2, diff3, diff4 = abs(y1 - y2), abs(x2 - x3), abs(y3 - y4), abs(x4 - x1)
                        show_detected = check_if_correct(diff1, diff2, diff3, diff4)
                    aruco_ids.append([(corners[i][0][0][0], corners[i][0][0][1]), text])
                if correl > 0.85 and show_detected:
                    print("Something has been shown!")
                    frame = aruco.drawDetectedMarkers(frame, corners, ids)
                    thresholded = aruco.drawDetectedMarkers(thresholded, corners, ids)
                    for j in range(len(aruco_ids)):
                        cv2.putText(frame, aruco_ids[j][1], (int(aruco_ids[j][0][0]), int(aruco_ids[j][0][1])),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                        correl = 0
        cv2.imshow(window_name, frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)