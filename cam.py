import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier("C:\\Users\\Salman\\Documents\\machinelearning\\haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while(True):
    #capture framewise
    ret , frame =cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray ,1.5,5);
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
    cv2.imshow("Frame",frame)
    
    if(cv2.waitKey(1) == ord("q")):
        break;    
cap.release()
cv2.destroyAllWindows()
