import numpy as np
import cv2

path = r'variant-2.png'
img = cv2.imread(path)

dst = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)    #размывает изображение, используя ядро Гаусса размером (5,5) и BORDER_DEFAULT в качестве типа границы.

cv2.imshow('image', np.hstack((img, dst)))
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)
