# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zakaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_zakaz(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 86)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(187, 255, 187);\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 20, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_ok = QtWidgets.QPushButton(Form)
        self.pushButton_ok.setGeometry(QtCore.QRect(280, 50, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(370, 50, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 50, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " "))
        self.label.setText(_translate("Form", "Назовите ваш заказ:"))
        self.pushButton_ok.setText(_translate("Form", "Ок"))
        self.pushButton_cancel.setText(_translate("Form", "Отмена"))
        self.label_2.setText(_translate("Form", "Такой заказ уже есть!"))
