import cv2 as cv

vid = cv.VideoCapture("videos/video.mp4")

while True:
    success, img = vid.read()
    cv.imshow("video", img)

    if cv.waitKey(24) == ord('q'):
        break