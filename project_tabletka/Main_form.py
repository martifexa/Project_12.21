# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_form1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 94)
        Form.setStyleSheet("background-color: rgb(187, 255, 187);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 10, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_yes = QtWidgets.QPushButton(Form)
        self.pushButton_yes.setGeometry(QtCore.QRect(30, 50, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.pushButton_yes.setFont(font)
        self.pushButton_yes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_yes.setObjectName("pushButton_yes")
        self.pushButton_no = QtWidgets.QPushButton(Form)
        self.pushButton_no.setGeometry(QtCore.QRect(214, 50, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.pushButton_no.setFont(font)
        self.pushButton_no.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_no.setObjectName("pushButton_no")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 51, 41))
        self.label_2.setStyleSheet("background-image: url(Screenshot_1.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Screenshot_1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "У вас есть рецепт от врача?"))
        self.pushButton_yes.setText(_translate("Form", "Да"))
        self.pushButton_no.setText(_translate("Form", "Нет"))
