import cv2 as cv

img = cv.imread("images/cat.jpeg")

size =12   # THE STROMGNESS OF THE BLURR AND THE ARES AROUND THEM 
b_img=cv.blur(cv.resize(img,(1000,1000)),(size,size))
cv.imshow("blurred image",b_img)
cv.waitKey(0)

gb_img=cv.GaussianBlur(cv.resize(img,(1000,1000)),(size,size),3)
cv.imshow(" guassian blurred image",gb_img)
cv.waitKey(0)