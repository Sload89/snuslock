#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  snuslock.py
#  
#  Copyright 2017 mackan <mackan@mackan-pecon>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem
from snuslock_ui import Ui_MainWindow
from database import Database as db
from smaker_ui import Ui_form_smaker as formSmaker
from mottaget_ui import Ui_Form_mottaget as formMottaget
from add_lager_ui import Ui_Dialog_add_lager as addLager
from new_smak_ui import Ui_Dialog_new_smak as newSmak
from fakturera_ui import Ui_Dialog_fakturera as Formfakturera
from inlev_ui import Ui_Dialog_inlev as formInlev

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.pushButton_smaker.clicked.connect(self.action_smaker)
        self.pushButton_mottaget.clicked.connect(self.action_mottaget)
        self.pushButton_fakturera.clicked.connect(self.action_fakturera)
        self.pushButton_inleverera.clicked.connect(self.action_inlev)
        self.toolButton_add_Lager.clicked.connect(self.action_add_lager)
        self.action_Importera.triggered.connect(self.importera)

        self.test = ""
    
        self.db = db()
        self.smaker = self.db.get_smaker()
        self.show_lager()


    def show_dialog(self, form):
        dialog = QtWidgets.QDialog()
        dialog.ui = form
        dialog.ui.setupUi(dialog)
        dialog.exec_()


    def action_smaker(self):
        self.show_dialog(formSmaker(self))
        self.statusbar.showMessage("Test", 0)

    def action_fakturera(self):
        self.show_dialog(Formfakturera())
        
        
    def action_mottaget(self):
        self.show_dialog(formMottaget())
        
    def action_add_lager(self):
        self.show_dialog(addLager(self, self.db))
        self.statusbar.showMessage(self.test, 0)

    def action_inlev(self):
        self.show_dialog(formInlev(self))
        
    def new_smak(self, smaker_ui):
        #print("Weeeiiiii")
        self.show_dialog(newSmak(smaker_ui))
        self.statusbar.showMessage("Hej!", 0)
    
    def importera(self):
        self.statusbar.showMessage("Tja!", 0)
        print("Hej!")

    def inlev(self, date, antal):
        #print(date, antal)
        #self.date = date.toString()
        #print(type(antal))
        #print(self.date)
        #self.d = QtCore.QDate.fromString(self.date)
        #print(self.d)
        self.db.inlev(date.toString(), antal)
    

    def add_lager(self, smak, antal):
        #print(self.get_id(smak), antal)
        self.db.add_lager(self.get_id(smak), antal)
        self.show_lager()

    def show_lager(self):
        i = 0
        count = 0
        #width = self.tableWidget_lager.horizontalHeader().width()
        #print(width)
        self.lager = self.db.get_lager()
        #print(self.lager)
        self.tableWidget_lager.setRowCount(len(self.lager))
        #self.tableWidget_lager.setColumnCount(2)
        self.tableWidget_lager.setHorizontalHeaderLabels(["Smak", "Antal"])
        self.tableWidget_lager.setColumnWidth(0, 150)
        self.tableWidget_lager.setColumnWidth(1, 150)
        while i < len(self.lager):
            self.tableWidget_lager.setItem(i, 0, QTableWidgetItem(str(self.get_smak(self.lager[i][0]))))
            self.tableWidget_lager.setItem(i, 1, QTableWidgetItem(str("{:,}".format(self.lager[i][1]))))
            count += self.lager[i][1]
            i+=1
        self.label_totalCount.setText(str("{:,}").format(count))
        #width = self.tableWidget_lager.columnWidth(0)
        #print(width)

    def get_id(self, smak):
        for s in self.smaker:
            if s[1] == smak:
                return int(s[0])

    def get_smak(self, num):
        for s in self.smaker:
            if s[0] == num:
                return str(s[1])
        
    #def add_smak(self, smak=None, bild=None):
    #   print(smak, bild)
        #self.db.add_smak(smak, bild)
        #self.smaker.reload_smaker(self)
    #   super(MainWindow, self).reload_smaker()
    
    
        
        
        
#class ShowDialog(QtWidgets.QDialog, form):
    #def __init__(self):
        #self.dialog = QtWidgets.QDialog()
        #self.dialog.ui = form
        #self.dialog.ui.setupUi(self.dialog)
        #self.exec_()
        #self.show()

def main(args):
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

self.db.close()
