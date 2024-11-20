#entro a la carpeta cylinder/train y me fijo que cada imagen tiene un archivo .txt con las coordenadas de los puntos
#de no ser así borro la imagen
import os
import cv2
import numpy as np

path = 'cylinder/test'
for filename in os.listdir(path):
    if filename.endswith(".jpg"):
        img = cv2.imread(os.path.join(path, filename))
        txt = filename.replace('.jpg', '.txt')
        txt = os.path.join(path, txt)
        if not os.path.exists(txt):
            os.remove(os.path.join(path, filename))
            print('borrado', filename)
        else:
            with open(txt) as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip().split(' ')
                    x = int(float(line[0])*img.shape[1])
                    y = int(float(line[1])*img.shape[0])
                    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)