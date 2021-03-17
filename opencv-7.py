import cv2
import numpy as np
print(cv2.__version__)


capture = cv2.VideoCapture(0)

capture.set(3,640)
capture.set(4,480)

font = cv2.FONT_HERSHEY_SIMPLEX


while True:
    success, img = capture.read()


    cv2.putText(img, 'Hello !', (20, 50), font, 1.3, (0, 255, 0), 2)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()