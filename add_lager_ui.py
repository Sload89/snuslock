# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_lager.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from operator import itemgetter

class Ui_Dialog_add_lager(QtWidgets.QDialog):
    def __init__(self, MainWindow, db):
        super().__init__()
        self.main = MainWindow
        self.db = db
    def setupUi(self, Dialog_add_lager):
        Dialog_add_lager.setObjectName("Dialog_add_lager")
        Dialog_add_lager.resize(307, 113)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_add_lager)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(Dialog_add_lager)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_add_lager)
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog_add_lager)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.dialog = Dialog_add_lager

        self.smaker = self.db.get_smaker()
        self.smaker.sort(key=itemgetter(1))
        for s in self.smaker:
           self.comboBox.addItem(s[1])
        self.pushButton_ok.clicked.connect(self.add)

        self.retranslateUi(Dialog_add_lager)
        QtCore.QMetaObject.connectSlotsByName(Dialog_add_lager)

    def add(self):
        smak = self.comboBox.currentText()
        antal = self.lineEdit.text()
        if antal != "":
            self.main.add_lager(smak, antal)
            self.lineEdit.clear()
        self.dialog.close()

    def retranslateUi(self, Dialog_add_lager):
        _translate = QtCore.QCoreApplication.translate
        Dialog_add_lager.setWindowTitle(_translate("Dialog_add_lager", "Lägg till i lager"))
        self.comboBox.setCurrentText(_translate("Dialog_add_lager", "--smaker--"))
        self.comboBox.setItemText(0, _translate("Dialog_add_lager", "--smaker--"))
        self.lineEdit.setPlaceholderText(_translate("Dialog_add_lager", "Antal..."))
        self.pushButton_ok.setText(_translate("Dialog_add_lager", "Ok"))

