# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'defaultGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 316)
        self.captura = QtWidgets.QPushButton(Dialog)
        self.captura.setGeometry(QtCore.QRect(10, 270, 121, 23))
        self.captura.setObjectName("captura")
        self.checkBoxSuavizado = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSuavizado.setGeometry(QtCore.QRect(120, 10, 70, 17))
        self.checkBoxSuavizado.setObjectName("checkBoxSuavizado")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(100, 10, 20, 81))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.LEsuavizadoX = QtWidgets.QLineEdit(Dialog)
        self.LEsuavizadoX.setGeometry(QtCore.QRect(170, 30, 21, 20))
        self.LEsuavizadoX.setObjectName("LEsuavizadoX")
        self.LEsuavizadoY = QtWidgets.QLineEdit(Dialog)
        self.LEsuavizadoY.setGeometry(QtCore.QRect(170, 60, 21, 20))
        self.LEsuavizadoY.setObjectName("LEsuavizadoY")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 47, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 60, 47, 16))
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(190, 10, 20, 151))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.checkBoxCanny = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCanny.setGeometry(QtCore.QRect(210, 10, 70, 17))
        self.checkBoxCanny.setObjectName("checkBoxCanny")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 30, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(210, 60, 101, 16))
        self.label_6.setObjectName("label_6")
        self.LEumbralInf = QtWidgets.QLineEdit(Dialog)
        self.LEumbralInf.setGeometry(QtCore.QRect(290, 30, 31, 20))
        self.LEumbralInf.setObjectName("LEumbralInf")
        self.LEumbralSup = QtWidgets.QLineEdit(Dialog)
        self.LEumbralSup.setGeometry(QtCore.QRect(290, 60, 31, 20))
        self.LEumbralSup.setObjectName("LEumbralSup")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(320, 10, 20, 151))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.checkBoxBinarizado = QtWidgets.QCheckBox(Dialog)
        self.checkBoxBinarizado.setGeometry(QtCore.QRect(10, 10, 101, 17))
        self.checkBoxBinarizado.setObjectName("checkBoxBinarizado")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label_4.setObjectName("label_4")
        self.LEumbralBin = QtWidgets.QLineEdit(Dialog)
        self.LEumbralBin.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.LEumbralBin.setObjectName("LEumbralBin")
        self.comboBoxCamara = QtWidgets.QComboBox(Dialog)
        self.comboBoxCamara.setGeometry(QtCore.QRect(10, 240, 121, 22))
        self.comboBoxCamara.setObjectName("comboBoxCamara")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 220, 131, 16))
        self.label.setObjectName("label")
        self.LEumbralSupThr = QtWidgets.QLineEdit(Dialog)
        self.LEumbralSupThr.setEnabled(False)
        self.LEumbralSupThr.setGeometry(QtCore.QRect(290, 140, 31, 20))
        self.LEumbralSupThr.setObjectName("LEumbralSupThr")
        self.LEumbralInfThr = QtWidgets.QLineEdit(Dialog)
        self.LEumbralInfThr.setEnabled(False)
        self.LEumbralInfThr.setGeometry(QtCore.QRect(290, 110, 31, 20))
        self.LEumbralInfThr.setObjectName("LEumbralInfThr")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(210, 140, 81, 16))
        self.label_7.setObjectName("label_7")
        self.checkBoxCannyThr = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCannyThr.setEnabled(False)
        self.checkBoxCannyThr.setGeometry(QtCore.QRect(210, 90, 91, 17))
        self.checkBoxCannyThr.setObjectName("checkBoxCannyThr")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(210, 110, 81, 16))
        self.label_8.setObjectName("label_8")
        self.guardarCaptura = QtWidgets.QPushButton(Dialog)
        self.guardarCaptura.setEnabled(False)
        self.guardarCaptura.setGeometry(QtCore.QRect(150, 270, 121, 23))
        self.guardarCaptura.setObjectName("guardarCaptura")
        self.labelTildeVerde = QtWidgets.QLabel(Dialog)
        self.labelTildeVerde.setGeometry(QtCore.QRect(280, 270, 41, 21))
        self.labelTildeVerde.setText("")
        self.labelTildeVerde.setObjectName("labelTildeVerde")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.captura.setText(_translate("Dialog", "Iniciar captura"))
        self.checkBoxSuavizado.setText(_translate("Dialog", "Suavizado"))
        self.LEsuavizadoX.setText(_translate("Dialog", "5"))
        self.LEsuavizadoY.setText(_translate("Dialog", "5"))
        self.label_2.setText(_translate("Dialog", "kernel X"))
        self.label_3.setText(_translate("Dialog", "kernel Y"))
        self.checkBoxCanny.setText(_translate("Dialog", "Canny"))
        self.label_5.setText(_translate("Dialog", "umbral inf"))
        self.label_6.setText(_translate("Dialog", "umbral sup"))
        self.LEumbralInf.setText(_translate("Dialog", "100"))
        self.LEumbralSup.setText(_translate("Dialog", "230"))
        self.checkBoxBinarizado.setText(_translate("Dialog", "Binarizado"))
        self.label_4.setText(_translate("Dialog", "Umbral"))
        self.LEumbralBin.setText(_translate("Dialog", "150"))
        self.label.setText(_translate("Dialog", "Seleccionar cámara"))
        self.LEumbralSupThr.setText(_translate("Dialog", "255"))
        self.LEumbralInfThr.setText(_translate("Dialog", "100"))
        self.label_7.setText(_translate("Dialog", "umbral sup"))
        self.checkBoxCannyThr.setText(_translate("Dialog", "threshold"))
        self.label_8.setText(_translate("Dialog", "umbral inf"))
        self.guardarCaptura.setText(_translate("Dialog", "Guardar captura"))
