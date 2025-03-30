import cv2 as cv
# img = cv.imread("images/cat.jpeg")

capture = cv.VideoCapture("vidoes/dog.mp4")
print("video is read")
while True:
    isTrue,frame = capture.read()
    print("videos are frames are currently showing")
    cv.imshow("Vidoes",frame)

    if cv.waitKey(20) &  0xFF ==ord('d'):
        break 
capture.release()
cv.destroyAllWindows()
# cv.imshow("Cat",img)------------------------
# cv.waitKey(0)
