import cv2 as cv
img  = cv.imread("images/cat.jpeg")


cv.imshow("image",img)

print(img.shape)
cv.waitKey(0)

img2=cv.resize(img,(640, 480))
cv.imshow("after resize ",img2)
print(img2.shape)
cv.waitKey(0)