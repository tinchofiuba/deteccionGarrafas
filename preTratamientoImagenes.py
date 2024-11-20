import cv2
import os
import numpy as np
#script para convertir a escala de grises y a normalizar una imagen a un tamaño normalizado
#primero calculo el tamaño promedio de todas las imagenes.

def tamañoPromedio(img):
    return [img.shape[0], img.shape[1]]

def verificarFormato(img,formato):
    return img.endswith('.'+formato)

def img2Gray(img,dirImg):
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nombreImg=dirImg.split('.')[0] 
    #guardo las imagenes en escala de grisis dentro de la carpeta 'fotosGarrafasGray'
    cv2.imwrite(nombreImg+'_Gray.jpg',gray)

def resizeImg(img, x, y, nombreImg):
    resized = cv2.resize(img, (x, y))
    #cv2.imwrite('fotosGarrafas/' + nombreImg + '_resized.jpg', resized)

if __name__ == '__main__':  
    #leo las imagenes que sea
    #me fijo todos los archivos en la carpeta 'fotosGarrafas
    sizeX=[]
    sizeY=[]
    carpeta="fotosGarrafas"
    for img in os.listdir(carpeta):
        if verificarFormato(img,'jpeg'):
            dirImg=carpeta+'/'+img
            imagen=cv2.imread(dirImg)
            x,y=tamañoPromedio(imagen)
            sizeX.append(x)
            sizeY.append(y)
            print("ok")
        else:
            print("no es jpeg")
    print("fin")
    #hago un resize de todas las imagenes con x=232 y=221
    for img in os.listdir(carpeta):
        print(img)
        if verificarFormato(img,'jpg') and img.endswith('_Gray.jpg'):
            dirImg=carpeta+'/'+img
            resizeImg(imagen, 232, 221, img.split('.')[0])
            print("ok")
        else:
            print("no es jpeg")
