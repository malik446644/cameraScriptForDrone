import numpy as np
import cv2  as cv

cap = cv.VideoCapture(0)

# controls
def nothing(v):
    pass
cv.namedWindow("controls")
cv.createTrackbar("lower_hue", "controls", 56, 255, nothing)
cv.createTrackbar("upper_hue", "controls", 78, 255, nothing)

# video stream while loop
while True:
    _, frame = cap.read()
    # Converting BGR to HSV for better color selecting
    hsv = cv.cvtColor(cv.blur(frame, (15, 15)), cv.COLOR_BGR2HSV)
    # selecting range of green color using HSV
    lowerHue = cv.getTrackbarPos("lower_hue", "controls")
    upperHue = cv.getTrackbarPos("upper_hue", "controls")
    lower_blue = np.array([lowerHue,50,75])
    upper_blue = np.array([upperHue,255,255])
    # making binary image as a mask using the hsv color range
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        cv.drawContours(frame, contours, -1, 255, 3)
        # find the biggest countour (c) by the area
        biggestConture = max(contours, key = cv.contourArea)
        x,y,w,h = cv.boundingRect(biggestConture)
        # draw the biggest contour (c) in green
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv.drawContours(frame, contours, -1, (0, 255, 0), 2)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)

    if cv.waitKey(5) == 113:
        break

cap.release()
cv.destroyAllWindows()