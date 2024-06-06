import re
import cv2
import tensorflow as tf
import numpy as np
from cv2 import aruco
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 640


def set_input_tensor(interpreter, image):
    """Sets the input tensor."""
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = np.expand_dims((image - 255) / 255, axis=0)


def get_output_tensor(interpreter, index):
    """Returns the output tensor at the given index."""
    output_details = interpreter.get_output_details()[index]
    tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
    return tensor


def detect_objects(interpreter, image, threshold):
    """Returns a list of detection results, each a dictionary of object info."""
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    # Get all output details
    boxes = get_output_tensor(interpreter, 1)
    classes = get_output_tensor(interpreter, 3)
    scores = get_output_tensor(interpreter, 0)
    count = int(get_output_tensor(interpreter, 2))

    results = []
    for i in range(count):
        if scores[i] >= threshold:
            result = {
                'bounding_box': boxes[i],
                'class_id': classes[i],
                'score': scores[i]
            }
            results.append(result)
    return results


def main(frame=None):
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_100)
    aruco_params = aruco.DetectorParameters()
    aruco_params.useAruco3Detection = False
    aruco_params.minMarkerDistanceRate = 0.001
    aruco_params.minMarkerPerimeterRate = 0.001
    aruco_params.minSideLengthCanonicalImg = 2
    interpreter = tf.lite.Interpreter('detect.tflite')
    interpreter.allocate_tensors()
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

    img = cv2.resize(frame, dsize=(640, 640))
    res = detect_objects(interpreter, img, 0.75)
    all_ids = []
    answers = []
    for result in res:
        ymin, xmin, ymax, xmax = result['bounding_box']
        xmin = int(max(1, xmin * CAMERA_WIDTH))
        xmax = int(min(CAMERA_WIDTH, xmax * CAMERA_WIDTH))
        ymin = int(max(1, ymin * CAMERA_HEIGHT))
        ymax = int(min(CAMERA_HEIGHT, ymax * CAMERA_HEIGHT))
        aruco_region = img[ymin:ymax, xmin:xmax]
        corners, ids, rejected = aruco.detectMarkers(aruco_region, aruco_dict, parameters=aruco_params)
        if corners:
            for j in range(len(corners)):
                start_x, end_x = corners[j][0][0][0], corners[j][0][2][0]
                start_y, end_y = corners[j][0][0][1], corners[j][0][2][1]
                corners[j][0][0][0] = corners[j][0][3][0] = xmin
                corners[j][0][1][0] = corners[j][0][2][0] = xmax
                corners[j][0][0][1] = corners[j][0][1][1] = ymin
                corners[j][0][2][1] = corners[j][0][3][1] = ymax
                if start_x < end_x and start_y < end_y:
                    text = "UP"
                elif start_x > end_x and start_y < end_y:
                    text = "RIGHT"
                elif start_x > end_x and start_y > end_y:
                    text = "DOWN"
                elif start_x < end_x and start_y > end_y:
                    text = "LEFT"
                if [(xmin, ymin), text] not in all_ids:
                    all_ids.append([(xmin, ymin), text])
                    answers.append((int(ids[j]), text))
    else:
        if all_ids:
            for j in range(len(all_ids)):
                cv2.putText(img, all_ids[j][1], (int(all_ids[j][0][0]), int(all_ids[j][0][1])),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    return img, answers
