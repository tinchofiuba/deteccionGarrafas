#importo las librerias para trabajar con Qt y el modulo de la interfaz grafica
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import sys
import os
from defaultGUI import Ui_Dialog
import model
from model import colaCanny,colaBin,colaGauss,capturaModel
import cv2
#creo la clase que hereda de QMainWindow y de la interfaz grafica
class GUI(QMainWindow):
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
        self.ui.LEumbralInf.textChanged.connect(self.valoresCanny)
        self.ui.LEumbralSup.textChanged.connect(self.valoresCanny)
        self.ui.LEsuavizadoX.textChanged.connect(self.valoresGauss)
        self.ui.LEsuavizadoY.textChanged.connect(self.valoresGauss)
        self.ui.LEumbralBin.textChanged.connect(self.valoresBin)
        
    def capturaView(self):
        self.ui.captura.setText("Detener captura")
        capturaModel(self.ui.comboBoxCamara.currentText())
        #configBotones
    
    def valoresCanny(self):
        if self.ui.checkBoxCanny.isChecked():
            if self.ui.LEumbralInf.text()!="" and self.ui.LEumbralSup.text()!="":
                colaCanny.put([int(self.ui.LEumbralInf.text()),int(self.ui.LEumbralSup.text())])
                self.
        else:
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

