import os
import cv2 as cv
vid = cv.VideoCapture("videos/dog.mp4")
ret =True
while True :
    ret,frame = vid.read()
    if not ret :
        break
    cv.imshow("video",frame)
    cv.waitKey(1)

vid.release()
cv.destroyAllWindows()




