import cv2 as cv
img =cv.imread("images/bird.jfif")
img = cv.resize(img,(800,800))
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,image=cv.threshold(img,170,255,cv.THRESH_BINARY_INV)
contours,heir = cv.findContours(image,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    print(cv.contourArea(cnt))
    if cv.contourArea(cnt)>100:
        cv.drawContours(img,cnt,-1,(255,0,0),5)

        x1,y1,w,h = cv.boundingRect(cnt)
        cv.rectangle(image,(x1,y1),(x1+w,y1+h),(255,255,255),1)
cv.imshow("image ", image)
cv.imshow(" ",img)
cv.waitKey(0)
