import cv2 as cv
import numpy as np
from PIL import Image




def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit




vid = cv.VideoCapture(0)
colour = [0,255,255]
while True:
    ret,frame=vid.read()
    hsv_img = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    ll,ul = get_limits(color=colour)
    mask = cv.inRange(hsv_img,ll,ul)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    print(bbox)
    if bbox is not None :
        x1,y1,x2,y2 = bbox
        cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),1)
    

    cv.imshow("video frame ",frame)
    if cv.waitKey(1) &  0xFF == ord('q') :
        break



vid.release()
cv.destroyAllWindows()
