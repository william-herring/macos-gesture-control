import time

import mediapipe as mp
import cv2
from controller import Controller

ctrl = Controller()

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

base_options = BaseOptions(
    model_asset_path='./gesture_recognizer.task')

feed = cv2.VideoCapture(0)
timestamp = 0
last_recognised_gesture = ''


def handle_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))

    global last_recognised_gesture

    if len(result.gestures) == 0 or result.gestures[0][0].category_name == last_recognised_gesture or result.gestures[0][0].category_name == 'None':
        return

    last_recognised_gesture = result.gestures[0][0].category_name
    ctrl.issue_command(last_recognised_gesture)


options = GestureRecognizerOptions(
    base_options=base_options,
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=handle_result)

with GestureRecognizer.create_from_options(options) as recognizer:
    while True:
        ret, frame = feed.read()

        if not ret:
            break

        timestamp += 1

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        recognizer.recognize_async(mp_image, timestamp)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    feed.release()
    cv2.destroyAllWindows()
