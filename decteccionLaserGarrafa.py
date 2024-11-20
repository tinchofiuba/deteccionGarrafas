import cv2
import numpy as np
from multiprocessing import Pool

def process_frame(frame):
    # convierto a HSV para poder trabajar con las escalas de color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # defino los rangos de color rojo permisibles para ser segregados en la imagen en formato HSV
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    #Se debería tener en cuenta que se debería mover toda la GUI, de alguna forma u otra.
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = mask1 | mask2  # me quedo con cualquier pixel que este dentro de mask1 o mask2
    # aplico la mascara a la imagen original
    result_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    # encuentro el contorno de la linea roja
    contours, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # me quedo con el contorno más grande
    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)
        #encuadro el contorno con un rectangulo
        x, y, w, h = cv2.boundingRect(contour)
        area=cv2.contourArea(contour)
        if area>4000 and w>20 and h>380:
            #hago una matriz con el mismo tamaño que laimagen
            mask = np.zeros_like(mask_red)
            #a esta imagen recien creada le dibujo el contorno en blanco
            cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
            return mask
        else:
            return None #si no cumple ls condiciones devuelvo None
    else:
        return None #si no hay contornos devuelvo None

def main():
    cap = cv2.VideoCapture(0)
    pool = Pool(processes=4)  # Ajusta el número de procesos según tu CPU

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se puede recibir frame (stream end?). quiteando")
            break
        # Proceso el frame en paralelo
        mask = pool.apply_async(process_frame, (frame,)).get()
        if mask is not None:
            cv2.imshow('Frame', frame)
            cv2.imshow('Result Red', mask)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break   
        else:
            print("No se detectaron colores rojos o el contorno no cumple las condiciones")
            #cierro las ventanas si no se detecta nada
            #cv2.destroyAllWindows()

    cap.release()
    cv2.destroyAllWindows()
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()