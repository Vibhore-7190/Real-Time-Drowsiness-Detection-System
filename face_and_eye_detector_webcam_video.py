"""This script uses OpenCV's haarcascade (face and eye cascade) to detect face
and eyes in a video feed which can be inputted through a webcam."""

# Import necessary libraries
from curses.textpad import rectangle

import VideoCapture as VideoCapture
import cv2

# Load face cascade and hair cascade from haarcascades folder
from matplotlib.pyplot import imshow

from face_and_eye_detector_single_image import gray

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")

# Capture video from webcam
video_capture = VideoCapture


# Read all frames from webcam
def flip():
    pass


def cvtColor():
    pass


def COLOR_BGR2GRAY():
    pass


def waitKey():
    pass


while True:
    ret, frame = video_capture.read()
    flip()
    cvtColor()

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rectangle(frame, [x, y], (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    imshow('Video', frame)

    if waitKey() & 0xFF == ord('q'):
        break

# Finally when video capture is over, release the video capture and destroyAllWindows
video_capture.release()


def destroyAllWindows():
    pass


destroyAllWindows()
