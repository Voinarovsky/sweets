import cv2
import numpy as np

img =  cv2.imread('fhkessf.jpg', cv2.IMREAD_COLOR)    #читаем картинку cv2.IMREAD_COLOR тип картинки цветной
img[0,0] = np.array([0,0,0]) #пикселю с координат 0 0 присваиваем черный цвет
img[:100,:100] = np.array([0,0,0])  #закрасили первые 100 на 100 строк в черный
blur_img = cv2.blur(img, (10,10))   #блюр картинки


cv2.inwrite('dsd.jpg',r)
print(b)
