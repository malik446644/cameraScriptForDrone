import numpy as np
import cv2  as cv

cap = cv.VideoCapture(0)

lowerHue = 0
upperHue = 0

def nothing(v):
    pass

cv.namedWindow("controls")
cv.createTrackbar("lower_hue", "controls", 0, 255, nothing)
cv.createTrackbar("upper_hue", "controls", 0, 255, nothing)

while True:
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([cv.getTrackbarPos("lower_hue", "controls"),50,50])
    upper_blue = np.array([cv.getTrackbarPos("upper_hue", "controls"),255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    bluecnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]

    if len(bluecnts)>0:
        blue_area = max(bluecnts, key=cv.contourArea)
        (xg,yg,wg,hg) = cv.boundingRect(blue_area)
        cv.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)

    if cv.waitKey(5) == 27:
        break

cap.release()
cv.destroyAllWindows()