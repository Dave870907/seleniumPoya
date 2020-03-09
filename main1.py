from PyQt5.QtWidgets import QMainWindow
import sys
from interface import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self , parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def but1(self):
        print('1')

    def initUI(self):
        self.pushButton_1.clicked.connect(self.but1)

if __name__ == "__main__":
    """
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    win = QtWidgets.QMainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
    """
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())