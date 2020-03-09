from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
#name = input("請輸入名稱:")   #名稱
#num = '0'+name  #編號
#driver = webdriver.Chrome() #共用的瀏覽器

import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from interface import Ui_MainWindow
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QMainWindow

from interface import *
from test import *
from printer1 import *
from printer2 import *
from printer3 import *
from Ricoh import *
from Ricoh2 import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self , parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUi()



    def initUi(self):
        self.pushButton_1.clicked.connect(self.but1)
        self.pushButton_2.clicked.connect(self.but2)
        self.pushButton_3.clicked.connect(self.but3)
        self.pushButton_4.clicked.connect(self.but4)
        self.pushButton_5.clicked.connect(self.but5)
        self.pushButton_all.clicked.connect(self.butAll)


    def but1(self):
        name = self.txt1.text()
        num = '0'+name  #編號
        if name != '':
            driver = webdriver.Chrome()  # 共用的瀏覽器
            c = printer1(name, num, driver)
            # print(c)
        else:
            c = ['請輸入字串!']
        str1 = ''
        for i in range (len(c)):
            str1 += c[i] 
        self.label.setText(str1)   

    def but2(self):
        name = self.txt1.text()
        num = '0'+name  #編號
        if name != '':
            driver = webdriver.Chrome()  # 共用的瀏覽器
            c = printer2(name, num, driver)
            # print(c)
        else:
            c = ['請輸入字串!']
        str1 = ''
        for i in range (len(c)):
            str1 += c[i] 
        self.label.setText(str1)

    def but3(self):
        name = self.txt1.text()
        num = '0'+name  #編號
        if name != '':
            driver = webdriver.Chrome()  # 共用的瀏覽器
            c = printer3(name, num, driver)
            # print(c)
        else:
            c = ['請輸入字串!']
        str1 = ''
        for i in range (len(c)):
            str1 += c[i] 
        self.label.setText(str1)
        
    def but4(self):
        name = self.txt1.text()
        num = '0'+name  #編號
        print(name)
        if name != '':
            driver = webdriver.Chrome()  # 共用的瀏覽器
            c = Ricoh(name, driver)
            # print(c)
        else:
            c = ['請輸入字串!']
        str1 = ''
        for i in range (len(c)):
            str1 += c[i] + "\n"
        self.label.setText(str1)

    def but5(self):
        name = self.txt1.text()
        num = '0'+name  #編號
        print(name)
        if name != '':
            driver = webdriver.Chrome()  # 共用的瀏覽器
            c = Ricoh2(name, driver)
            # print(c)
        else:
            c = ['請輸入字串!']
        str1 = ''
        for i in range (len(c)):
            str1 += c[i] + "\n"
        self.label.setText(str1)
        
    def butAll(self):
        name = self.txt1.text()
        num = '0'+name  #編號
        print(name)
        if name != '':
            driver = webdriver.Chrome()  # 共用的瀏覽器
            c = printerall(name, num, driver)
            # print(c)
        else:
            c = ['請輸入字串!']
        str1 = ''
        for i in range (len(c)):
            str1 += c[i] + "\n"
        self.label.setText(str1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # ui = Ui_MainWindow()
    win = MainWindow()
    #ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())