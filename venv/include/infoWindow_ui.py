# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoWindow(object):
    def setupUi(self, InfoWindow):
        InfoWindow.setObjectName("InfoWindow")
        InfoWindow.resize(300, 400)
        self.labelInfo = QtWidgets.QLabel(InfoWindow)
        self.labelInfo.setGeometry(QtCore.QRect(25, 75, 250, 200))
        self.labelInfo.setAutoFillBackground(False)
        self.labelInfo.setObjectName("labelInfo")
        self.pushButtonCloseWindow = QtWidgets.QPushButton(InfoWindow)
        self.pushButtonCloseWindow.setGeometry(QtCore.QRect(90, 30, 120, 40))
        self.pushButtonCloseWindow.setObjectName("pushButtonCloseWindow")
        self.labelAuthors = QtWidgets.QLabel(InfoWindow)
        self.labelAuthors.setGeometry(QtCore.QRect(20, 300, 140, 65))
        self.labelAuthors.setObjectName("labelAuthors")
        self.labelVersion = QtWidgets.QLabel(InfoWindow)
        self.labelVersion.setGeometry(QtCore.QRect(220, 330, 60, 35))
        self.labelVersion.setObjectName("labelVersion")

        self.retranslateUi(InfoWindow)
        self.pushButtonCloseWindow.clicked.connect(InfoWindow.close)
        QtCore.QMetaObject.connectSlotsByName(InfoWindow)

    def retranslateUi(self, InfoWindow):
        _translate = QtCore.QCoreApplication.translate
        InfoWindow.setWindowTitle(_translate("InfoWindow", "Information"))
        self.labelInfo.setText(_translate("InfoWindow", "<html><head/><body><p align=\"center\"><a name=\"tw-target-text\"/><span style=\" font-family:\'Courier New,courier\';\">T</span><span style=\" font-family:\'Courier New,courier\';\">he application loads the <br/>indicated image and then <br/>performs segmentation. <br/>It is possible to select <br/>the source points after <br/>clicking the mouse and <br/>indicating the coordinates.</span></p></body></html>"))
        self.pushButtonCloseWindow.setText(_translate("InfoWindow", "Close window"))
        self.labelAuthors.setText(_translate("InfoWindow", "<html><head/><body><p align=\"center\">Authors:<br/>Krystian Bendinger<br/>Patryk Mazurek<br/>Szymon Delikat</p></body></html>"))
        self.labelVersion.setText(_translate("InfoWindow", "<html><head/><body><p align=\"center\">Version: <br/>0.1</p></body></html>"))
