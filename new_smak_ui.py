# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_smak.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_Dialog_new_smak(QtWidgets.QDialog):
    def __init__(self, Ui_form_smaker):
         super().__init__()
         self.smaker = Ui_form_smaker
         self.smak = ""
         self.bild = ""
    def setupUi(self, Dialog_new_smak):
        Dialog_new_smak.setObjectName("Dialog_new_smak")
        Dialog_new_smak.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_new_smak.resize(297, 303)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_new_smak)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_smak = QtWidgets.QLineEdit(Dialog_new_smak)
        self.lineEdit_smak.setInputMask("")
        self.lineEdit_smak.setText("")
        self.lineEdit_smak.setMaxLength(32767)
        self.lineEdit_smak.setObjectName("lineEdit_smak")
        self.verticalLayout.addWidget(self.lineEdit_smak)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_image = QtWidgets.QLabel(Dialog_new_smak)
        self.label_image.setScaledContents(False)
        self.label_image.setObjectName("label_image")
        self.horizontalLayout.addWidget(self.label_image)
        self.pushButton_browse = QtWidgets.QPushButton(Dialog_new_smak)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_browse.sizePolicy().hasHeightForWidth())
        self.pushButton_browse.setSizePolicy(sizePolicy)
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.horizontalLayout.addWidget(self.pushButton_browse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_add = QtWidgets.QPushButton(Dialog_new_smak)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        
        self.dialog = Dialog_new_smak

        self.retranslateUi(Dialog_new_smak)
        self.pushButton_browse.clicked.connect(self.browse)
        self.pushButton_add.clicked.connect(self.add)
        #self.pushButton_browse.clicked.connect(Dialog_new_smak.open)
        QtCore.QMetaObject.connectSlotsByName(Dialog_new_smak)

    def retranslateUi(self, Dialog_new_smak):
        _translate = QtCore.QCoreApplication.translate
        Dialog_new_smak.setWindowTitle(_translate("Dialog_new_smak", "Dialog"))
        self.label_image.setText(_translate("Dialog_new_smak", "Bild"))
        self.pushButton_browse.setText(_translate("Dialog_new_smak", "Bläddra..."))
        self.pushButton_add.setText(_translate("Dialog_new_smak", "Lägg till"))

    def add(self):
        #print("test")
        self.smak = self.lineEdit_smak.text()
        #super().importera()
        self.smaker.add_smak(self.smak, self.bild[0])
        self.dialog.close()

    def browse(self):
        #print("test")
        self.bild = QtWidgets.QFileDialog.getOpenFileName(self,"Bläddra", "")
        self.pix = QPixmap(self.bild[0])
        self.label_image.setPixmap(self.pix)
