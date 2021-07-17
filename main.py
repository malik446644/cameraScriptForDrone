import cv2 as cv

capture = cv.VideoCapture("videos/video.mp4")

while True:
    success, img = capture.read()
    cv.imshow("video", img)

    if cv.waitKey(24) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()