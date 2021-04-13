from imutils.video import VideoStream
import numpy as np
import cv2
import time
import imutils
from imutils.video import VideoStream
from imutils import face_utils

vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF