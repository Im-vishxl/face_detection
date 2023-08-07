import cv2
import face_recognition
from simple_facerec import SimpleFacerec

#load camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)

    key = cv2.waitKey()
    if key == ord("a"):
        break

cap.release()
cv2.destroyAllWindows()

