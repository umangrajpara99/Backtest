# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alert1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_AlertWindow(object):
    def setupUi(self, MainWindow_2):
        MainWindow_2.setObjectName("MainWindow_2")
        MainWindow_2.resize(250 , 50)
        self.centralwidget = QtWidgets.QWidget(MainWindow_2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 20))
        self.label.setObjectName("label")
        MainWindow_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 22))
        self.menubar.setObjectName("menubar")
        MainWindow_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_2)
        self.statusbar.setObjectName("statusbar")
        MainWindow_2.setStatusBar(self.statusbar)
        MainWindow_2.setWindowTitle("Alert")
        QtCore.QMetaObject.connectSlotsByName(MainWindow_2)

    def AlertBrowse(self, MainWindow_2):
        MainWindow_2.resize(350 , 50)
        self.label.setText("Please select Downloaded 'stocks' folder")

    def AlertBuySell(self, MainWindow_2):
        MainWindow_2.resize(250 , 50)
        self.label.setText("Please select Buy or Sell")
