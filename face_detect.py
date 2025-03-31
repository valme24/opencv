import cv2 as cv
import mediapipe as mp
#read image 
# img = cv.imread("images/man.jpg")
webcam = cv.VideoCapture(0)
ret,img = webcam.read()

H,W,_ = img.shape



#detect face
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.5) as face_detection:
    img_rgb = cv.cvtColor(img,cv.COLOR_RGB2BGR)
    out = face_detection.process(img_rgb)
    print(out.detections)

    if out.detections is not None :
        for detection in out.detections :
          location_data = detection.location_data
          bbox = location_data.relative_bounding_box


          x1,y1,w,h = bbox.xmin,bbox.ymin,bbox.width,bbox.height
          y1 = int(y1*H)
          x1 = int(x1*W)
          w = int(w*W)
          h = int(h*H)

          cv.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),10)

    cv.imshow("image ",img)
    cv.waitKey(0) 

    






#blur faces



#save the image 


