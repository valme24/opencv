import cv2 as cv

img = cv.imread("images/cat.jpeg")

cv.imshow("image",img)
cv.waitKey(0)

img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("image rgb",img_rgb)
cv.waitKey(0)
