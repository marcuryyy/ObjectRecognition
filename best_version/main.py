import tensorflow as tf
from object_detection.builders import model_builder
from object_detection.utils import config_util
import cv2
from cv2 import aruco
import numpy as np

configs = config_util.get_configs_from_pipeline_file(
    "D:/tf/TFODCourse/Tensorflow/workspace/models/model_custom/pipeline.config")
detection_model = model_builder.build(model_config=configs['model'], is_training=False)

# Restore checkpoint
camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_1000)
aruco_params = aruco.DetectorParameters()
aruco_params.useAruco3Detection = False
aruco_params.minMarkerDistanceRate = 0.001
aruco_params.minMarkerPerimeterRate = 0.001
aruco_params.minSideLengthCanonicalImg = 2
correl = 0
aruco_corners = []
text = ""
show_detected = False
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore("C:/Users/mark/Desktop/ssd_mobilenet_v2/custom_640/ckpt-7").expect_partial()

answer_up = 2
answer_right = 3
answer_down = 4
answer_left = 5


@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections


cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
DELTA = 30
while cap.isOpened():
    ret, frame = cap.read()
    image_np = np.array(frame)

    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections = detect_fn(input_tensor)

    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                  for key, value in detections.items()}
    detections['num_detections'] = num_detections

    all_ids = []
    for i in range(len(detections['detection_boxes'])):
        if detections['detection_scores'][i] > 0.5:
            for j in range(4):
                if j % 2 == 0:
                    detections['detection_boxes'][i][j] = detections['detection_boxes'][i][j] * height
                else:
                    detections['detection_boxes'][i][j] = detections['detection_boxes'][i][j] * width
            n1, n2, n3, n4 = detections['detection_boxes'][i][0], detections['detection_boxes'][i][1], \
                detections['detection_boxes'][i][2], detections['detection_boxes'][i][3]
            aruco_region = frame

            # В процессе
            if int(n1) - DELTA < 0:
                aruco_region = frame[0:int(n3) + DELTA, int(n2) - DELTA:int(n4) + DELTA]
            if int(n3) + DELTA > height:
                aruco_region = frame[int(n1) - DELTA:height, int(n2) - DELTA:int(n4) + DELTA]
            if int(n2) - DELTA < 0:
                aruco_region = frame[int(n1) - DELTA:int(n3) + DELTA, 0:int(n4) + DELTA]
            if int(n4) + DELTA > width:
                aruco_region = frame[int(n1) - DELTA:int(n3) + DELTA, int(n2) - DELTA:width]

            # aruco_region = cv2.cvtColor(aruco_region, cv2.COLOR_BGR2GRAY)
            corners, ids, rejected = aruco.detectMarkers(aruco_region, aruco_dict, parameters=aruco_params)
            if corners:
                for j in range(len(corners)):
                    start_x, end_x = corners[j][0][0][0], corners[j][0][2][0]
                    start_y, end_y = corners[j][0][0][1], corners[j][0][2][1]
                    corners[j][0][0][0] = corners[j][0][3][0] = n2
                    corners[j][0][1][0] = corners[j][0][2][0] = n4
                    corners[j][0][0][1] = corners[j][0][1][1] = n1
                    corners[j][0][2][1] = corners[j][0][3][1] = n3
                    if start_x < end_x and start_y < end_y:
                        text = "False"
                        # text = "UP"
                    elif start_x > end_x and start_y < end_y:
                        text = "False"
                    # text = "RIGHT"
                    elif start_x > end_x and start_y > end_y:
                        text = "True"
                        # text = "DOWN"
                    elif start_x < end_x and start_y > end_y:
                        text = "False"
                    # text = "LEFT"
                    all_ids.append([(n2, n1), text])

    else:
        if all_ids:
            for j in range(len(all_ids)):
                cv2.putText(frame, all_ids[j][1], (int(all_ids[j][0][0]), int(all_ids[j][0][1])),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow(window_name, frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)
