# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'okno_prof1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_prof(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 522)
        MainWindow.setStyleSheet("background-color: rgb(187, 255, 187);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 70, 311, 331))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 220, 51, 51))
        self.label_2.setStyleSheet(r"background-image: url(C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\Screenshot_8.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(r"C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\Screenshot_8.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 300, 61, 61))
        self.label_3.setStyleSheet(r"background-image: url(C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\Screenshot_7.png);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\Screenshot_7.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 60, 61, 61))
        self.label_4.setStyleSheet(r"background-image: url(C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\Screenshot_9.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(r"C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\Screenshot_9.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 140, 51, 51))
        self.label_5.setStyleSheet(r"background-image: url(C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\Screenshot_6.png);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(r"C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\Screenshot_6.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_itog = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_itog.setGeometry(QtCore.QRect(230, 430, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.pushButton_itog.setFont(font)
        self.pushButton_itog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_itog.setObjectName("pushButton_itog")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(320, 430, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 430, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 430, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 430, 131, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Профилактика"))
        self.label.setText(_translate("MainWindow", "Профилактические средства по вашему запросу:"))
        self.pushButton_itog.setText(_translate("MainWindow", "Итого"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_3.setText(_translate("MainWindow", "Выйти"))
        self.label_6.setText(_translate("MainWindow", "Итого:"))
