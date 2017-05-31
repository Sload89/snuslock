# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mottaget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from database import Database as db

class Ui_Form_mottaget(object):
    def __init__(self):
        self.db = db()
        self.inlev = self.db.get_inlev()
    def setupUi(self, Form_mottaget):
        Form_mottaget.setObjectName("Form_mottaget")
        Form_mottaget.resize(265, 370)
        Form_mottaget.setMinimumSize(QtCore.QSize(265, 370))
        Form_mottaget.setMaximumSize(QtCore.QSize(265, 370))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_mottaget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form_mottaget)
        self.tabWidget.setObjectName("tabWidget")
        self.monthly = QtWidgets.QWidget()
        self.monthly.setObjectName("monthly")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.monthly)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget_monthly = QtWidgets.QTableWidget(self.monthly)
        self.tableWidget_monthly.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_monthly.setTabKeyNavigation(False)
        self.tableWidget_monthly.setProperty("showDropIndicator", False)
        self.tableWidget_monthly.setDragDropOverwriteMode(False)
        self.tableWidget_monthly.setRowCount(12)
        self.tableWidget_monthly.setColumnCount(2)
        self.tableWidget_monthly.setObjectName("tableWidget_monthly")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_monthly.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_monthly.setHorizontalHeaderItem(1, item)
        self.tableWidget_monthly.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tableWidget_monthly)
        self.tabWidget.addTab(self.monthly, "")
        self.weekly = QtWidgets.QWidget()
        self.weekly.setObjectName("weekly")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.weekly)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.weekly)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setRowCount(53)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.weekly, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form_mottaget)
        self.tabWidget.setCurrentIndex(0)
        self.tableWidget_monthly.setColumnWidth(0, 100)
        self.tableWidget_monthly.setColumnWidth(1, 112)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 112)
        self.mon()
        QtCore.QMetaObject.connectSlotsByName(Form_mottaget)

    def mon(self):
        self.i = 1
        self.m = {} # månad
        self.w = {} # vecka
        while self.i <= 12:
            self.m[self.i] = 0
            self.i += 1
        self.i = 1
        while self.i <= 53:
            self.w[self.i] = 0
            self.i += 1
        #print(self.m)
        for a, d in self.inlev:
            mon = QtCore.QDate.fromString(d).month()
            wk = QtCore.QDate.fromString(d).weekNumber()
            #print(wk[0], a)
            self.m[mon] += a
            self.w[wk[0]] += a
            #print(mon)
            #print(d, a)
            #print(self.m)
        #print(type(self.m))
        for m, a in self.m.items():
            #print(y)
            self.tableWidget_monthly.setItem(m-1, 0, QTableWidgetItem(str(self.get_month(m))))
            self.tableWidget_monthly.setItem(m-1, 1, QTableWidgetItem(str("{:,}".format(a))))
        for w, a in self.w.items():
            self.tableWidget.setItem(w-1, 0, QTableWidgetItem(str(w)))
            self.tableWidget.setItem(w-1, 1, QTableWidgetItem(str("{:,}".format(a))))

        
    #def get_week(self):
        

    def get_month(self, num):
        return {1: "Januari", 2: "Februrari", 3: "Mars", 4: "April",
            5: "Maj", 6: "Juni", 7: "Juli", 8: "Augusti", 9: "September", 10: "Oktober", 11: "November", 12: "December"}.get(num)


    def retranslateUi(self, Form_mottaget):
        _translate = QtCore.QCoreApplication.translate
        Form_mottaget.setWindowTitle(_translate("Form_mottaget", "Mottaget"))
        item = self.tableWidget_monthly.horizontalHeaderItem(0)
        item.setText(_translate("Form_mottaget", "Månad"))
        item = self.tableWidget_monthly.horizontalHeaderItem(1)
        item.setText(_translate("Form_mottaget", "Antal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monthly), _translate("Form_mottaget", "Månadsvis"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_mottaget", "Vecka"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_mottaget", "Antal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weekly), _translate("Form_mottaget", "Veckovis"))

