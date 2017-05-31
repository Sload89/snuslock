#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  collection.py
#  
#  Copyright 2017 Marcus Andersson <marcus@marcus-desktop>
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

import sqlite3 as sql

db_path = "/home/mackan/Documents/Projects/Snuslock/snuslock.db"

class Database:
    def __init__(self):
        self.con = sql.connect(db_path)
        self.cur = self.con.cursor()
        #self.create_table()

    def add_smak(self, smak, bild):
        self.smak = smak
        self.bild = bild
        #print(self.smak, self.bild)
        self.cur.execute("INSERT INTO smaker(smak, bild) VALUES (?, ?)", (self.smak, self.bild))
        self.commit()

    def add_lager(self, smak, antal):
        self.smak = smak
        #print(self.smak)
        self.antal = int(antal)
        print(type(self.antal))
        self.cur.execute("SELECT * FROM lager WHERE id=?", (self.smak,))
        row = self.cur.fetchone()
        if row != None:
            #print(row)
            #print(row[1])
            self.antal += int(row[1])
            self.cur.execute("UPDATE lager SET antal=? WHERE id=?", (self.antal, self.smak))
        else:
            self.cur.execute("INSERT INTO lager(id, antal) VALUES (?, ?)", (self.smak, self.antal))
        self.commit()
        #print(row)

    def inlev(self, datum, antal):
        self.antal = int(antal)
        self.datum = datum
        #print(type(self.antal))
        #print(type(self.datum))
        self.cur.execute("SELECT * FROM inlev WHERE datum=?", (self.datum,))
        row = self.cur.fetchone()
        print(row)
        if row != None:
            self.antal += int(row[0])
            self.cur.execute("UPDATE inlev SET antal=? WHERE datum=?", (self.antal, self.datum))
        else:
            self.cur.execute("INSERT INTO inlev(antal, datum) VALUES (?, ?)", (self.antal, self.datum))
        self.commit()

    def get_smaker(self):
        self.cur.execute("SElECT * FROM smaker")
        rows = self.cur.fetchall()
        return rows

    def get_inlev(self):
        self.cur.execute("SELECT * FROM inlev")
        rows = self.cur.fetchall()
        return rows

    def get_lager(self):
        self.cur.execute("SELECT * FROM lager ORDER BY id")
        rows = self.cur.fetchall()
        return rows

    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()
        
    def create_table(self):
        #self.cur.execute("CREATE TABLE smaker (id PRIMARY KEY, smak TEXT, bild TEXT)")
        #self.cur.execute("CREATE TABLE inlev (antal INT, datum DATE)")
        #self.cur.execute("CREATE TABLE utlev (id INT, antal INT, datum DATE)")
        #self.cur.execute("CREATE TABLE monthly (id INT, month INT, antal INT)")
        #self.cur.execute("CREATE TABLE weekly (id INT, week INT, antal INT)")
        self.cur.execute("CREATE TABLE lager (id INT, antal INT)")
        self.commit()
