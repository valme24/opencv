import cv2 as cv
img = cv.imread("images/w.jfif")
edge_image = cv.Canny(img,100,200)

cv.imshow("edged imae",edge_image)
cv.waitKey(0)