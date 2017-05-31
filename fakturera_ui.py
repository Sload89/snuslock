# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fakturera.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_fakturera(object):
    def setupUi(self, Dialog_fakturera):
        Dialog_fakturera.setObjectName("Dialog_fakturera")
        Dialog_fakturera.resize(316, 526)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_fakturera)
        self.verticalLayout.setObjectName("verticalLayout")
        self.columnView = QtWidgets.QColumnView(Dialog_fakturera)
        self.columnView.setObjectName("columnView")
        self.verticalLayout.addWidget(self.columnView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_totalt = QtWidgets.QLabel(Dialog_fakturera)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_totalt.sizePolicy().hasHeightForWidth())
        self.label_totalt.setSizePolicy(sizePolicy)
        self.label_totalt.setObjectName("label_totalt")
        self.horizontalLayout.addWidget(self.label_totalt)
        self.label_antal = QtWidgets.QLabel(Dialog_fakturera)
        self.label_antal.setObjectName("label_antal")
        self.horizontalLayout.addWidget(self.label_antal, 0, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_print = QtWidgets.QPushButton(Dialog_fakturera)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_print.sizePolicy().hasHeightForWidth())
        self.pushButton_print.setSizePolicy(sizePolicy)
        self.pushButton_print.setObjectName("pushButton_print")
        self.horizontalLayout.addWidget(self.pushButton_print)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_fakturera)
        QtCore.QMetaObject.connectSlotsByName(Dialog_fakturera)

    def retranslateUi(self, Dialog_fakturera):
        _translate = QtCore.QCoreApplication.translate
        Dialog_fakturera.setWindowTitle(_translate("Dialog_fakturera", "Fakturera"))
        self.label_totalt.setText(_translate("Dialog_fakturera", "Totalt:"))
        self.label_antal.setText(_translate("Dialog_fakturera", "0"))
        self.pushButton_print.setText(_translate("Dialog_fakturera", "Skriv ut"))

