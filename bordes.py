import cv2
import numpy as np
import os

def img2Gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def edges(img):
    return cv2.Canny(img, 100, 200)

def capturaVideo():
    i=0
    cap = cv2.VideoCapture(0)
    while True:
       #i+=2
        #if i==180:
         #   i=0
        #print(i)
        ret, frame = cap.read()
        grayFrame = img2Gray(frame)
        edges = cv2.Canny(grayFrame, 30, 230)
        cv2.imshow('frame', edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    capturaVideo()