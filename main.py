import numpy as np
import cv2  as cv

# controls
def nothing(v):
    pass
cv.namedWindow("controls")
cv.createTrackbar("lower_hue", "controls", 56, 255, nothing)
cv.createTrackbar("upper_hue", "controls", 78, 255, nothing)

cap = cv.VideoCapture(0)

# video stream while loop
while True:
    _, frame = cap.read()
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
        cv.putText(frame, str(len(approx)) + " points", (x, y - 20), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), thickness=2)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)

    if cv.waitKey(5) == 113:
        break

cap.release()
cv.destroyAllWindows()