import cv2 as cv
img = cv.imread("images/w.jfif")

cv.imshow("image",img)
cv.waitKey(200)
g_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,b_img = cv.threshold(g_img,150,255,cv.THRESH_BINARY)
b_img = cv.blur(b_img,(4,7))
bad_img = cv.adaptiveThreshold(g_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,15,10)
cv.imshow("adaptive threshold binaryimage ",bad_img)
cv.waitKey(0)
cv.imshow("binary images",b_img)
cv.waitKey(0)