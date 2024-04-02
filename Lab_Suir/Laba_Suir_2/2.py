import numpy as np
import cv2

camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame = camera.read()
    cv2.imshow('Test', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
camera.close()
cv2.destroyAllWindows()

exit(-1)