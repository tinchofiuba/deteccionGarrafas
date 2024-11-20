import cv2
import numpy as np

# Iniciar la captura de video desde la webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened(): #en caso de no poder abrir la camara
    print("Error: No se puede abrir la cámara!!")
    exit()
while True:
    #repito hasta abortar
    ret, frame = cap.read() #capturo un frame de la camara
    if not ret:
        print("Error: No se puede recibir frame (stream end?). quiteando ...")
        break
    #convierto a HSV para poder trabajar con las escalas de color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #defino los rangos de color rojo permisibles para ser segregados en la imagen 
    #en formato HSV
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    #creo las mascaras para los rangos de color rojo
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = mask1 | mask2 #me quedo con cualquier pixel que este dentro de mask1 o mask2
    #aplico la mascara a la imagen original
    result_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    #muestro en un cuadro las 2 imagenes, la original y la que tiene solo el color rojo
    #encuentro el contorno de la linea roja
    contours, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #me quedo con el contorno más grande
    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)
        #dibujo en resul_red el contorno con color blanco
        cv2.drawContours(result_red, [contour], -1, (255, 255, 255), 3)
        esqueleto=[]
        for i in range(len(contour)):
            #me quedo con los puntos que tienen la misma Y
            points = [p for p in contour if p[0][1] == contour[i][0][1]]
            #busco el valor maximo y mínimo de x para ese Y
            Mx=max(points,key=lambda x: x[0][0])
            mx=min(points,key=lambda x: x[0][0])
            #lo redondeo a 0 decimales para poder graficar el pixel.qq
            meanX=round((Mx[0][0]+mx[0][0])/2,0)
            esqueleto.append([meanX,contour[i][0][1]]) #apendizo el x,y
        #hago una regresión y saco m,b de la recta
        x = np.array([p[0] for p in esqueleto])
        y = np.array([p[1] for p in esqueleto])
        try:
            m, b = np.polyfit(x, y, 1)
        except:
            m = 0
            b = 0
    cv2.imshow('Imagen Roja', result_red)
    #Salgo del bucle si se presiona la tecla 'escape'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#dejo de reproducir la camara y cierrro.
cap.release()
cv2.destroyAllWindows()
