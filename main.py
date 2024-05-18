import time

import mediapipe as mp
import cv2

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

base_options = BaseOptions(
    model_asset_path='./gesture_recognizer.task')

feed = cv2.VideoCapture(0)
timestamp = 0


def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))


options = GestureRecognizerOptions(
    base_options=base_options,
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)

with GestureRecognizer.create_from_options(options) as recognizer:
    while True:
        ret, frame = feed.read()

        if not ret:
            break

        timestamp += 1

        # cv2.imshow('frame', frame)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        recognizer.recognize_async(mp_image, timestamp)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    feed.release()
    cv2.destroyAllWindows()
