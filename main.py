import time

import cv2  as cv
import numpy as np
from mss import mss

import fps
import way

# global variables
isUsingCamera = False

# counting to three before starting the script
for i in range(3):
    print(i + 1)
    time.sleep(1)

if(isUsingCamera):
    cap = cv.VideoCapture(0)
    capWidth = cap.get(3)
    capHeight = cap.get(4)
else:
    capWidth = 1920 // 2
    capHeight = 1080 - 200
    bounding_box = {'top': 130, 'left': 0, 'width': capWidth, 'height': capHeight} 
    sct = mss()

# adding control window to control some parameteres live without restarting the app
def nothing(v):
    pass
cv.namedWindow("controls", cv.WINDOW_NORMAL)
cv.createTrackbar("lower_hue", "controls", 56, 255, nothing)
cv.createTrackbar("upper_hue", "controls", 78, 255, nothing)

# every frame processing loop
while True:
    if(isUsingCamera): _, frame = cap.read()
    else: frame = np.array(sct.grab(bounding_box))
    # making a blured version of the current frame
    bluredFrame = cv.blur(frame, (7, 7))
    # Converting BGR to HSV for better color selecting
    hsv = cv.cvtColor(bluredFrame, cv.COLOR_BGR2HSV)
    # selecting range of green color using HSV
    lowerHue = cv.getTrackbarPos("lower_hue", "controls")
    upperHue = cv.getTrackbarPos("upper_hue", "controls")
    lower_blue = np.array([lowerHue,50,50])
    upper_blue = np.array([upperHue,255,255])
    # making binary image as a mask using the hsv color range
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        # find the biggest countour
        biggestConture = max(contours, key = cv.contourArea)
        # reduce the ammount of points to know the shape
        peri = cv.arcLength(biggestConture, True)
        approx = cv.approxPolyDP(biggestConture, 0.04 * peri, True)
        # selecting rectangle on the biggest contour
        x,y,w,h = cv.boundingRect(biggestConture)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0) if len(approx) == 3 else (0,0,255),2)
        contourCenter = (x + w//2, y + h//2)
        cv.circle(frame, contourCenter, 2, (0, 0, 255), -1)
        cv.putText(frame, str(len(approx)) + " points", (x, y - 20), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), thickness=2)

        # going to the detected contour and calculate the way and go to it
        way.findWayAndGo(contourCenter[0], contourCenter[1], capWidth, capHeight)

    # calculate the fps
    FramePerSecond = fps.calculateFps()
    cv.putText(frame, "fps: " + str(FramePerSecond), (0, 25), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), thickness=2)

    cv.imshow("frame", frame)
    # cv.imshow("mask", mask)

    if cv.waitKey(5) == 113:
        break

if(isUsingCamera): cap.release()
cv.destroyAllWindows()