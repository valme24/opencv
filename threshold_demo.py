import cv2 as cv

img = cv.imread("images/cat.jpeg")


g_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,b_img = cv.threshold(g_img,100,255,cv.THRESH_BINARY)
b_img = cv.blur(b_img,(4,7))
cv.imshow("grayscale image ",g_img)
cv.waitKey(0)
cv.imshow("binary images",b_img)
cv.waitKey(0)
