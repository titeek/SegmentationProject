# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import os
import platform
import subprocess
import sys
import string
import regionGrowingSegmentation

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

use = 0
process = 0


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
        self.labelDifference = QtWidgets.QLabel(mainWindow)
        self.labelDifference.setGeometry((QtCore.QRect(180, 280, 80, 20)))
        self.labelDifference.setObjectName("labelDifference")
        self.labelZ = QtWidgets.QLabel(mainWindow)
        self.labelZ.setGeometry(QtCore.QRect(70, 310, 20, 20))
        self.labelZ.setObjectName("labelZ")
        self.labelProc = QtWidgets.QLabel(mainWindow)
        self.labelProc.setGeometry(QtCore.QRect(240, 306, 20, 20))
        self.labelProc.setObjectName("labelProc")
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
        self.radioButtonProcess = QtWidgets.QRadioButton(mainWindow)
        self.radioButtonProcess.setGeometry(QtCore.QRect(160, 250, 115, 20))
        self.radioButtonProcess.setObjectName("radioButtonPoints")
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
        self.textEditDifference = QtWidgets.QTextEdit(mainWindow)
        self.textEditDifference.setGeometry(QtCore.QRect(180, 304, 60, 28))
        self.textEditDifference.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.textEditDifference.setObjectName("textEditDifference")
        self.pushButtonClose = QtWidgets.QPushButton(mainWindow)
        self.pushButtonClose.setGeometry(QtCore.QRect(25, 355, 120, 40))
        self.pushButtonClose.setObjectName("pushButtonClose")

        self.retranslateUi(mainWindow)
        self.pushButtonClose.clicked.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.pushButtonFiles.clicked.connect(lambda: self.openFileNameDialog(mainWindow))

        self.radioButtonMouse.toggled.connect(lambda: self.onClickedMouse(mainWindow))
        self.radioButtonPoints.toggled.connect(lambda: self.onClickedPoints(mainWindow))
        self.radioButtonProcess.toggled.connect(lambda: self.onClickedProcess(mainWindow))

        self.pushButtonAccept.clicked.connect(lambda: self.onClickedAccept(mainWindow))

    def onClickedAccept(self, mainWindow):
        mainWindow.close()
        x = self.textEditX.toPlainText()
        y = self.textEditY.toPlainText()
        z = self.textEditZ.toPlainText()
        proc = self.textEditDifference.toPlainText()

        if not proc.isnumeric():
            proc = 7

        filename = self.textEditImage.toPlainText()

        global use
        global process

        if use == 1:
            convertedProc = int(proc)
            regionGrowingSegmentation.main(filename, 0, 0, use, convertedProc, process)
        elif use == 2:
            convertedX = int(x)
            convertedY = int(y)
            convertedProc = int(proc)
            regionGrowingSegmentation.main(filename, convertedX, convertedY, use, convertedProc, process)
        else:
            convertedProc = int(proc)
            regionGrowingSegmentation.main(filename, 0, 0, 1, convertedProc, process)

    def onClickedMouse(self,  mainWindow):
        print("Mouse")
        global use
        use = 1

        self.radioButtonPoints.setDisabled(1)
        self.labelX.setDisabled(1)
        self.labelY.setDisabled(1)
        self.labelZ.setDisabled(1)
        self.textEditX.setDisabled(1)
        self.textEditY.setDisabled(1)
        self.textEditZ.setDisabled(1)

    def onClickedPoints(self, mainWindow):
        print("Points")
        global use
        use = 2
        self.radioButtonMouse.setDisabled(1)

    def onClickedProcess(self, mainWindow):
        print("Process")

        global process
        process = 1

    def openFileNameDialog(self, mainWindow):
        defaultPath = ""
        path = "/home/krystian/Pulpit/ImagesPAMM"
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "Load image", path, "Bitmap (*.bmp);; PNG (*.png);; JPG (*.jpg)",
                                                  options=options)

        self.textEditImage.setText(QtCore.QCoreApplication.translate("mainWindow", fileName))

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Application"))
        self.labelLoadImage.setText(_translate("mainWindow", "Load image:"))
        self.labelChoosen.setText(_translate("mainWindow", "Choose source points:"))
        self.labelX.setText(_translate("mainWindow", "X:"))
        self.labelDifference.setText(_translate("mainWindow", "Difference:"))
        self.labelY.setText(_translate("mainWindow", "Y:"))
        self.labelZ.setText(_translate("mainWindow", "Z:"))
        self.pushButtonFiles.setText(_translate("mainWindow", "X"))
        self.radioButtonMouse.setText(_translate("mainWindow", "after mouse clicked"))
        self.radioButtonProcess.setText(_translate("mainWindow", "Show process of segmentation"))
        self.radioButtonPoints.setText(_translate("mainWindow", "points:"))
        self.pushButtonAccept.setText(_translate("mainWindow", "Accept"))
        self.pushButtonClose.setText(_translate("mainWindow", "Close"))
        self.labelProc.setText(_translate("mainWindow", "%"))

