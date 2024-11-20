import numpy as numpy
import cv2
from queue import Queue
colaCanny=Queue()
colaGauss=Queue()
colaBin=Queue()
configBin=None
configGauss=None
configCanny=None

def binarizado(img, umbral:int):
    gray=img2Gray(img)
    _,umbralizado=cv2.threshold(gray,umbral,255,cv2.THRESH_BINARY)
    return umbralizado

def img2Gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def filtradoGauss(img, kernelSize:list):
    kernelSize = [max(1, k) | 1 for k in kernelSize]
    return cv2.GaussianBlur(img, (kernelSize[0], kernelSize[1]), 0)

def canny(img, umbral1:int, umbral2:int, umbralThr1:int, umbralThr2:int):
    gray=img2Gray(img)
    print(umbralThr1,umbralThr2)
    if umbralThr1!=0 and umbralThr2!=0:
        _,th=cv2.threshold(gray, umbralThr1,umbralThr2,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return cv2.Canny(th, umbral1, umbral2)
    else:
        return cv2.Canny(gray, umbral1, umbral2)

def capturaModel(camara:str):
    global configBin
    global configGauss
    global configCanny
    cap = cv2.VideoCapture(int(camara))
    if not cap.isOpened(): #en caso de no poder abrir la camara
        print("Error: No se puede abrir la cámara!!")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se puede recibir frame (stream end?). quiteando ...")
            break
        if colaBin.empty()==False:
            configBin=colaBin.get()
        if colaCanny.empty()==False:
            configCanny=colaCanny.get()
        if colaGauss.empty()==False:
            configGauss=colaGauss.get()
        if configBin!=None:
            frame=binarizado(frame,configBin)
        if configGauss!=None:
            frame=filtradoGauss(frame,configGauss)
        if configCanny!=None:
            if len(configCanny)==2:
                frame=canny(frame,configCanny[0],configCanny[1],0,0)
            else:
                frame=canny(frame,configCanny[0],configCanny[1],configCanny[2],configCanny[3])
        cv2.imshow('Captura', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    
