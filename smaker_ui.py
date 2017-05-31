# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smaker.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database as db
from PyQt5.QtGui import QPixmap

stock = "/home/mackan/Documents/Projects/Snuslock/images/stock.png"

class Ui_form_smaker(object):
    def __init__(self, MainWindow):
        #super().__init__()
        self.main = MainWindow
        self.db = db()
    def setupUi(self, form_smaker):
        form_smaker.setObjectName("form_smaker")
        form_smaker.setWindowModality(QtCore.Qt.NonModal)
        form_smaker.resize(460, 475)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(form_smaker)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_newSmak = QtWidgets.QPushButton(form_smaker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_newSmak.sizePolicy().hasHeightForWidth())
        self.pushButton_newSmak.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.pushButton_newSmak.setFont(font)
        self.pushButton_newSmak.setCheckable(False)
        self.pushButton_newSmak.setDefault(False)
        self.pushButton_newSmak.setFlat(False)
        self.pushButton_newSmak.setObjectName("pushButton_newSmak")
        self.verticalLayout_2.addWidget(self.pushButton_newSmak)
        self.listWidget = QtWidgets.QListWidget(form_smaker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image = QtWidgets.QLabel(form_smaker)
        self.label_image.setObjectName("label")
        self.verticalLayout.addWidget(self.label_image)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(form_smaker)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(form_smaker)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_change = QtWidgets.QPushButton(form_smaker)
        self.pushButton_change.setObjectName("pushButton_change")
        self.verticalLayout.addWidget(self.pushButton_change)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.action_newSmak = QtWidgets.QAction(form_smaker)
        self.action_newSmak.setObjectName("action_newSmak")
        self.label_antal = QtWidgets.QLabel(form_smaker)
        self.label_antal.setObjectName("label_antal")
        self.verticalLayout_2.addWidget(self.label_antal)
        

        self.pix = QPixmap(stock)
        self.label_image.setPixmap(self.pix)
        #print(type(stock))
        
        self.smaker = self.db.get_smaker()
        for s in self.smaker:
           self.listWidget.addItem(s[1])
        self.listWidget.sortItems()
        self.antal = self.listWidget.count()
        #print(self.antal)

        self.retranslateUi(form_smaker)
        self.listWidget.currentRowChanged.connect(self.view_smak)
        self.pushButton_newSmak.clicked.connect(self.new_smak)
        QtCore.QMetaObject.connectSlotsByName(form_smaker)

    def retranslateUi(self, form_smaker):
        _translate = QtCore.QCoreApplication.translate
        form_smaker.setWindowTitle(_translate("form_smaker", "Smaker"))
        self.pushButton_newSmak.setText(_translate("form_smaker", "Lägg till smak"))
        self.label_2.setText(_translate("form_smaker", "Antal tryckt:"))
        self.label_3.setText(_translate("form_smaker", "0"))
        self.label_antal.setText(_translate("form_smaker",str(self.antal) + " smaker."))
        self.pushButton_change.setText(_translate("form_smaker", "Ändra"))
        self.action_newSmak.setText(_translate("form_smaker", "newSmak"))

    def new_smak(self):
        self.main.new_smak(self)

    def add_smak(self, smak=None, bild=None):
        print(smak, bild)
        self.db.add_smak(smak, bild)
        self.reload_smaker()
		
    def reload_smaker(self):
        smaker = self.db.get_smaker()
        self.listWidget.clear()
        for s in smaker:
            self.listWidget.addItem(s[1])
        self.listWidget.sortItems()

    def view_smak(self):
       #print("Hej")
       name = self.listWidget.currentItem().text()
       if not name:
           self.listWidget.setCurrentRow(1)
           name = self.listWidget.currentItem().text()
		   
       #print(name)
       for s in self.smaker:
           if s[1] == name:
        #       print(s[2])
               self.pix = QPixmap(s[2])
               self.label_image.setPixmap(self.pix)
