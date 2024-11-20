import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('garrafaML.png')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grisFiltrada=cv2.GaussianBlur(gris, (11, 11), 0)
grisFiltrada = cv2.GaussianBlur(gris, (11, 11), 0)
canny = cv2.Canny(grisFiltrada, 50, 200)
_,th=cv2.threshold(grisFiltrada, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('th', th)
#encuentro los contornos en la imagen th
contornos, _ = cv2.findContours(cv2.bitwise_not(th), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
sortedContornos = sorted(contornos, key=cv2.contourArea, reverse=True)[0]
canny = cv2.Canny(th, 50, 200)
cv2.imshow('canny2', canny)
#encierro con un rectangulo el contorno
x,y,w,h = cv2.boundingRect(sortedContornos)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('rectangulo', img)
#filtro con Sobel en la dirección vertical
sobel_y = cv2.Sobel(gris, cv2.CV_64F, 1, 0, ksize=3)

# Convertir el resultado a un formato adecuado para mostrar
abs_sobel_y = np.absolute(sobel_y)
sobel_y_8u = np.uint8(abs_sobel_y)

#aplico un umbral
_, sobel_y_8u = cv2.threshold(sobel_y_8u, 100, 255, cv2.THRESH_BINARY)
#hago un engrosado de los blancos, así el borde blanco se ve mejor
kernel = np.ones((5,5),np.uint8)
sobel_y_8u = cv2.dilate(sobel_y_8u, kernel, iterations = 1)
#encuentro los contornos
contornos, _ = cv2.findContours(sobel_y_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#dibujo los contornos
sortedContornos = sorted(contornos, key=cv2.contourArea, reverse=True)
contornoMax=sortedContornos[1]
contornoMax2=sortedContornos[2]
x,y,w,h = cv2.boundingRect(contornoMax)
print(x,y,w,h)
cv2.drawContours(img, [contornoMax], -1, (0, 255, 255), 3)
cv2.drawContours(img, [contornoMax2], -1, (0, 255, 255), 3)

# Mostrar y guardar la imagen con los bordes verticales
#cv2.imshow('Bordes Verticales', img)
#cv2.imwrite('garrafaML_bordes_verticales.png', sobel_y_8u)
cv2.waitKey(0)
cv2.destroyAllWindows()