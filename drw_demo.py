import cv2 as cv

board = cv.imread("images/white.jpg")
board = cv.resize(board,(500,500))
#line
cv.line(board,(0,0),(255,255),(0,255,0),3)
#image, cordinates,color,thickness


#rectangle
cv.rectangle(board,(10,10),(400,400),(0,0,255),3)
# give thickness -1 for filled ractangle



#circle
cv.circle(board,(255,255),40,(255,0,0),4)

#text
cv.putText(board,"hy",(400,100),cv.FONT_HERSHEY_PLAIN,2,(255,255,0),2)
#img,etxt,postition,font,size,color,thickness
cv.imshow("image",board)
cv.waitKey(0)