import cv2
import numpy as np
carcascde = cv2.CascadeClassifier('Re/cars3.xml')
peocascde=cv2.CascadeClassifier('Re/haarcascade_fullbody.xml')
capture=cv2.VideoCapture('Re/Q.mp4')
capture.set(3,640)
capture.set(3,480)

while True:
    success, img=capture.read()
    imGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    car=carcascde.detectMultiScale(imGray,1.1,1)
    for(x,y,w,h)in car:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    peo=peocascde.detectMultiScale(imGray,1.1,1)
    for(x,y,w,h)in peo:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('car',img)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()