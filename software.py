# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'software.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,uic
import numpy as np
import os
import face_recognition
import csv
import sys
import time
import logging as log
import datetime as dt
from time import sleep
from atten import Ui_Dialog
from error import Ui_Dialog_e




class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 417)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("index.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(170, 60, 281, 51))
        #self.label.setIndent(-1)
        #self.label.setObjectName("label")
        #self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        #self.dateEdit.setGeometry(QtCore.QRect(210, 110, 191, 32))
        #self.dateEdit.setCalendarPopup(True)
        #self.dateEdit.setObjectName("dateEdit")
        self.name_enter = QtWidgets.QTextEdit(self.centralwidget)
        self.name_enter.setGeometry(QtCore.QRect(230, 160, 191, 31))
        self.name_enter.setObjectName("name_enter")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(150, 170, 61, 21))
        self.name.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name.setLineWidth(3)
        self.name.setWordWrap(False)
        self.name.setObjectName("name")
        self.Coer_id = QtWidgets.QLabel(self.centralwidget)
        self.Coer_id.setGeometry(QtCore.QRect(150, 210, 81, 20))
        self.Coer_id.setObjectName("Coer_id")
        self.coer_id_enter = QtWidgets.QTextEdit(self.centralwidget)
        self.coer_id_enter.setGeometry(QtCore.QRect(230, 200, 191, 31))
        self.coer_id_enter.setObjectName("coer_id_enter")
        self.brach = QtWidgets.QLabel(self.centralwidget)
        self.brach.setGeometry(QtCore.QRect(150, 250, 71, 18))
        self.brach.setObjectName("brach")
        self.branch_enter = QtWidgets.QTextEdit(self.centralwidget)
        self.branch_enter.setGeometry(QtCore.QRect(230, 240, 191, 31))
        self.branch_enter.setObjectName("branch_enter")
        self.mark = QtWidgets.QPushButton(self.centralwidget)
        self.mark.setGeometry(QtCore.QRect(260, 290, 121, 34))
        self.mark.setObjectName("mark")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mark.clicked.connect(self.open )




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STA"))
        #self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">ENTER DATE</span></p></body></html>"))
        self.name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name</span></p></body></html>"))
        self.Coer_id.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">COER ID</span></p></body></html>"))
        self.brach.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Branch</span></p></body></html>"))
        self.mark.setText(_translate("MainWindow", "submit"))
        #MainWindow.hide()

        #sys.exit()










if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
