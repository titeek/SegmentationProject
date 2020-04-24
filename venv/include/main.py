
#pyuic5 test.ui > test_ui.py -> przerobienie .ui na .py
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from test_ui import Ui_StartWindow
from infoWindow_ui import Ui_InfoWindow
from mainWindow_ui import Ui_mainWindow

class MyForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())