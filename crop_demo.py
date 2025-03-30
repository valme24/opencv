import cv2 as cv

img = cv.imread("images/cat.jpeg")
cv.imshow("image" , img)
print(img.shape)
cv.waitKey(0)

c_img = img[50:200,50:200]
cv.imshow("cropped image",c_img)
cv.waitKey(0)
print(c_img.shape)