#importo las librerias para trabajar con Qt y el modulo de la interfaz grafica
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import sys
import os
from defaultGUI import Ui_Dialog
from model import colaCanny,colaBin,colaGauss,capturaModel #,capturaFoto
from PyQt5.QtCore import pyqtSignal, QThread
import cv2
#creo la clase que hereda de QMainWindow y de la interfaz grafica
class GUI(QMainWindow):
    iniciarCaptura = pyqtSignal(str) #señal para comunicarme con el view y prender la camara
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)   
        #me fijo cuantas camara hay así esté o no conectada y las meto en el comboBoxCamara
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                self.ui.comboBoxCamara.addItem(str(i))
                cap.release()
        self.dictConfig={'checkBox':{'canny':False,'suavizado':False,'binarizado':False},'valores':[]}
        self.ui.captura.clicked.connect(self.capturaView)
        self.ui.checkBoxCanny.stateChanged.connect(self.valoresCanny)
        self.ui.checkBoxSuavizado.stateChanged.connect(self.valoresGauss)
        self.ui.checkBoxBinarizado.stateChanged.connect(self.valoresBin)
        self.ui.checkBoxCannyThr.stateChanged.connect(self.valoresCanny)
        self.ui.LEumbralInf.textChanged.connect(self.valoresCanny)
        self.ui.LEumbralSup.textChanged.connect(self.valoresCanny)
        self.ui.LEsuavizadoX.textChanged.connect(self.valoresGauss)
        self.ui.LEsuavizadoY.textChanged.connect(self.valoresGauss)
        self.ui.LEumbralBin.textChanged.connect(self.valoresBin)
        self.ui.LEumbralInfThr.textChanged.connect(self.valoresCanny)
        self.ui.LEumbralSupThr.textChanged.connect(self.valoresCanny)
        self.ui.guardarCaptura.clicked.connect(self.guardarCaptura)
        self.ui.labelTildeVerde.setPixmap(QPixmap("/home/martin/repos/deteccionGarrafas/imagenes/tildeVerde_20_20.png"))
        self.ui.labelTildeVerde.hide()
        
    def guardarCaptura(self):
        self.ui.labelTildeVerde.setVisible(True)
        #self.model.capturaFoto()
        QtCore.QTimer.singleShot(500, self.ocultarTilde)
        
    def ocultarTilde(self):
        self.ui.labelTildeVerde.hide()

    def capturaView(self):
        if self.ui.captura.text()=="Detener captura":
            self.ui.captura.setText("Iniciar captura")
            self.ui.guardarCaptura.setEnabled(False)
            cv2.destroyAllWindows()
        else:
            self.ui.captura.setText("Detener captura")
            self.ui.guardarCaptura.setEnabled(True)
            #self.iniciarCaptura.emit(self.ui.comboBoxCamara.currentText()) #emito al model la camara seleccionada
            capturaModel(self.ui.comboBoxCamara.currentText())
    
    def valoresCanny(self):
        if self.ui.checkBoxCanny.isChecked():
            if self.ui.LEumbralInf.text()!="" and self.ui.LEumbralSup.text()!="":
                umbralInf=int(self.ui.LEumbralInf.text())
                umbralSup=int(self.ui.LEumbralSup.text())
                self.ui.checkBoxCannyThr.setEnabled(True)
                print("canny")
                if self.ui.checkBoxCannyThr.isChecked():
                    self.ui.LEumbralInfThr.setEnabled(True)
                    self.ui.LEumbralSupThr.setEnabled(True)
                    print("entro")
                    if self.ui.LEumbralInfThr.text()!="" and self.ui.LEumbralSupThr.text()!="":
                        umbralInfThr=int(self.ui.LEumbralInfThr.text())
                        umbralSupThr=int(self.ui.LEumbralSupThr.text())
                        if colaCanny.empty()==False:
                            #vacío la cola
                            colaCanny.get()
                            colaCanny.put([umbralInf,umbralSup,umbralInfThr,umbralSupThr])
                        else:
                            colaCanny.put([umbralInf,umbralSup,umbralInfThr,umbralSupThr])
                else:
                    self.ui.LEumbralInfThr.setEnabled(False)
                    self.ui.LEumbralSupThr.setEnabled(False)
                    print("no entro")
                    if colaCanny.empty()==False:
                        colaCanny.get()
                        colaCanny.put([umbralInf,umbralSup]) 
                    else:
                        colaCanny.put([umbralInf,umbralSup])
        else:
            self.ui.checkBoxCannyThr.setEnabled(False)
            colaCanny.put(None)

    def valoresGauss(self):
        if self.ui.checkBoxSuavizado.isChecked():
            if self.ui.LEsuavizadoX.text()!="" and self.ui.LEsuavizadoY.text()!="":
                colaGauss.put([int(self.ui.LEsuavizadoX.text()),int(self.ui.LEsuavizadoY.text())])
        else:
            colaGauss.put(None)
    def valoresBin(self):
        if self.ui.checkBoxBinarizado.isChecked():
            if self.ui.LEumbralBin.text()!="":
                colaBin.put(int(self.ui.LEumbralBin.text()))
        else:
            colaBin.put(None)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

