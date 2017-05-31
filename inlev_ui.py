# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inlev.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_inlev(object):
    def __init__(self, MainWindow):
        self.main = MainWindow
    def setupUi(self, Dialog_inlev):
        Dialog_inlev.setObjectName("Dialog_inlev")
        Dialog_inlev.setWindowModality(QtCore.Qt.WindowModal)
        Dialog_inlev.resize(350, 55)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_inlev.sizePolicy().hasHeightForWidth())
        Dialog_inlev.setSizePolicy(sizePolicy)
        Dialog_inlev.setMinimumSize(QtCore.QSize(350, 55))
        Dialog_inlev.setMaximumSize(QtCore.QSize(350, 55))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog_inlev)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEdit = QtWidgets.QDateEdit(Dialog_inlev)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.lineEdit = QtWidgets.QLineEdit(Dialog_inlev)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog_inlev)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.dialog = Dialog_inlev

        #self.date = QtCore.QDate().currentDate()
        #print(self.date)
        self.dateEdit.setDate(QtCore.QDate().currentDate())
        self.pushButton.clicked.connect(self.inlev)

        self.retranslateUi(Dialog_inlev)
        QtCore.QMetaObject.connectSlotsByName(Dialog_inlev)

    def inlev(self):
        try:
            self.date = self.dateEdit.date()
            self.antal = int(self.lineEdit.text())
            self.main.inlev(self.date, self.antal)
        except ValueError:
            print("Wrong!")
        self.dialog.close()

    def retranslateUi(self, Dialog_inlev):
        _translate = QtCore.QCoreApplication.translate
        Dialog_inlev.setWindowTitle(_translate("Dialog_inlev", "Inleverans"))
        self.pushButton.setText(_translate("Dialog_inlev", "Ok!"))

