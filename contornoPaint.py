import cv2

imagen=cv2.imread('fotosGarrafas/contornos/contorno1.jpg')
#paso a escala de grises
gray=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
#hago una umbralizacion
_,bin=cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
cv2.imshow('imagen',bin)
cv2.waitKey(0)