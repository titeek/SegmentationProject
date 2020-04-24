# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

#do segmentacji
import cv2 as cv
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import skimage.morphology as mor
#
import os
import platform
import subprocess
import sys
import string

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(300, 400)
        self.labelLoadImage = QtWidgets.QLabel(mainWindow)
        self.labelLoadImage.setGeometry(QtCore.QRect(20, 50, 100, 20))
        self.labelLoadImage.setObjectName("labelLoadImage")
        self.labelChoosen = QtWidgets.QLabel(mainWindow)
        self.labelChoosen.setGeometry(QtCore.QRect(20, 150, 150, 20))
        self.labelChoosen.setObjectName("labelChoosen")
        self.labelX = QtWidgets.QLabel(mainWindow)
        self.labelX.setGeometry(QtCore.QRect(70, 250, 20, 20))
        self.labelX.setObjectName("labelX")
        self.labelY = QtWidgets.QLabel(mainWindow)
        self.labelY.setGeometry(QtCore.QRect(70, 280, 20, 20))
        self.labelY.setObjectName("labelY")
        self.labelZ = QtWidgets.QLabel(mainWindow)
        self.labelZ.setGeometry(QtCore.QRect(70, 310, 20, 20))
        self.labelZ.setObjectName("labelZ")
        self.pushButtonFiles = QtWidgets.QPushButton(mainWindow)
        self.pushButtonFiles.setGeometry(QtCore.QRect(245, 80, 30, 30))
        self.pushButtonFiles.setObjectName("pushButtonFiles")
        self.textEditImage = QtWidgets.QTextEdit(mainWindow)
        self.textEditImage.setGeometry(QtCore.QRect(30, 80, 200, 30))
        self.textEditImage.setObjectName("textEditImage")
        self.radioButtonMouse = QtWidgets.QRadioButton(mainWindow)
        self.radioButtonMouse.setGeometry(QtCore.QRect(30, 190, 160, 20))
        self.radioButtonMouse.setObjectName("radioButtonMouse")
        self.radioButtonPoints = QtWidgets.QRadioButton(mainWindow)
        self.radioButtonPoints.setGeometry(QtCore.QRect(30, 220, 70, 20))
        self.radioButtonPoints.setObjectName("radioButtonPoints")
        self.pushButtonAccept = QtWidgets.QPushButton(mainWindow)
        self.pushButtonAccept.setGeometry(QtCore.QRect(155, 355, 120, 40))
        self.pushButtonAccept.setObjectName("pushButtonAccept")
        self.textEditX = QtWidgets.QTextEdit(mainWindow)
        self.textEditX.setGeometry(QtCore.QRect(90, 244, 60, 28))
        self.textEditX.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.textEditX.setObjectName("textEditX")
        self.textEditY = QtWidgets.QTextEdit(mainWindow)
        self.textEditY.setGeometry(QtCore.QRect(90, 274, 60, 28))
        self.textEditY.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.textEditY.setObjectName("textEditY")
        self.textEditZ = QtWidgets.QTextEdit(mainWindow)
        self.textEditZ.setGeometry(QtCore.QRect(90, 304, 60, 28))
        self.textEditZ.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.textEditZ.setObjectName("textEditZ")
        self.pushButtonClose = QtWidgets.QPushButton(mainWindow)
        self.pushButtonClose.setGeometry(QtCore.QRect(25, 355, 120, 40))
        self.pushButtonClose.setObjectName("pushButtonClose")

        self.retranslateUi(mainWindow)
        self.pushButtonClose.clicked.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


        self.pushButtonFiles.clicked.connect(lambda: self.openFileNameDialog(mainWindow))

        self.radioButtonMouse.toggled.connect(lambda: self.onClickedMouse(mainWindow))
        self.radioButtonPoints.toggled.connect(lambda: self.onClickedPoints(mainWindow))

        self.pushButtonAccept.clicked.connect(lambda: self.onClickedAccept(mainWindow))

    def onClickedAccept(self, mainWindow):
        mainWindow.close()
        x = self.textEditX.toPlainText()
        y = self.textEditY.toPlainText()
        z = self.textEditZ.toPlainText()

        #obróbka danych wejściowych

        filename = self.textEditImage.toPlainText()
        self.segmentationProg(filename)


    def onClickedMouse(self, mainWindow):
        print("Mouse")
        self.radioButtonPoints.setDisabled(1)
        self.labelX.setDisabled(1)
        self.labelY.setDisabled(1)
        self.labelZ.setDisabled(1)
        self.textEditX.setDisabled(1)
        self.textEditY.setDisabled(1)
        self.textEditZ.setDisabled(1)

    def onClickedPoints(self, mainWindow):
        print("Points")
        self.radioButtonMouse.setDisabled(1)

    def openFileNameDialog(self, mainWindow):
        defaultPath = ""
        path = "/home/krystian/Pulpit/ImagesPAMM"
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "Load image", path,"Bitmap (*.bmp);; PNG (*.png)", options=options)

        self.textEditImage.setText(QtCore.QCoreApplication.translate("mainWindow", fileName))
        #self.textEditImage.setDisabled(1)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Application"))
        self.labelLoadImage.setText(_translate("mainWindow", "Load image:"))
        self.labelChoosen.setText(_translate("mainWindow", "Choose source points:"))
        self.labelX.setText(_translate("mainWindow", "X:"))
        self.labelY.setText(_translate("mainWindow", "Y:"))
        self.labelZ.setText(_translate("mainWindow", "Z:"))
        self.pushButtonFiles.setText(_translate("mainWindow", "X"))
        self.radioButtonMouse.setText(_translate("mainWindow", "after mouse clicked"))
        self.radioButtonPoints.setText(_translate("mainWindow", "points:"))
        self.pushButtonAccept.setText(_translate("mainWindow", "Accept"))
        self.pushButtonClose.setText(_translate("mainWindow", "Close"))

    def segmentationProg(self, name):
        picture = cv.imread(name, 0)
        ret, thresh_binary = cv.threshold( picture, 200, 255, cv.THRESH_BINARY)
        thresh_binary = ndi.binary_fill_holes(thresh_binary)
        thresh_binary = mor.remove_small_objects(thresh_binary, min_size=64, connectivity=2)

        titles = ['Bez progowania', 'Globalne z progowa']
        images = [picture, thresh_binary]

        for i in range(len(images)):
            plt.subplot(1, 2, i + 1)
            plt.imshow(images[i], 'gray')
            plt.title(titles[i])
            #plt.xticks([]), plt.yticks([]) # wspolrzedne

        plt.show()

