# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from infoWindow_ui import Ui_InfoWindow
from mainWindow_ui import Ui_mainWindow

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(300, 400)
        self.pushButtonExit = QtWidgets.QPushButton(StartWindow)
        self.pushButtonExit.setGeometry(QtCore.QRect(90, 270, 120, 40))
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.pushButtonAbout = QtWidgets.QPushButton(StartWindow)
        self.pushButtonAbout.setGeometry(QtCore.QRect(90, 210, 120, 40))
        self.pushButtonAbout.setObjectName("pushButtonInfo")
        self.pushButtonStart = QtWidgets.QPushButton(StartWindow)
        self.pushButtonStart.setGeometry(QtCore.QRect(90, 150, 120, 40))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.labelSegmentation = QtWidgets.QLabel(StartWindow)
        self.labelSegmentation.setGeometry(QtCore.QRect(80, 60, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelSegmentation.setFont(font)
        self.labelSegmentation.setObjectName("labelSegmentation")

        self.retranslateUi(StartWindow)
        self.pushButtonExit.clicked.connect(StartWindow.close)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

        self.pushButtonAbout.clicked.connect(lambda: self.checkButtonClickedAbout(StartWindow))
        self.pushButtonStart.clicked.connect(lambda: self.checkButtonClickedStart(StartWindow))

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Segmentation"))
        self.pushButtonExit.setText(_translate("StartWindow", "Exit"))
        self.pushButtonAbout.setText(_translate("StartWindow", "About"))
        self.pushButtonStart.setText(_translate("StartWindow", "Start"))
        self.labelSegmentation.setText(_translate("StartWindow", "Segmentation"))

    def checkButtonClickedAbout(self, StartWindow):  # otwiera okno z informacjami // docelowo chciałbym zamykac stare okno
            print("info")

            #StartWindow.hide()
            self.aboutWindow = AboutWindow()
            self.aboutWindow.show()

            #if self.aboutWindow.isVisible() == 1:
                #StartWindow.show()

    def checkButtonClickedStart(self, StartWindow):
            print("start")

            #StartWindow.hide()
            self.mainWindow = MainWindow()
            self.mainWindow.show()

class AboutWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_InfoWindow()
        self.ui.setupUi(self)

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

