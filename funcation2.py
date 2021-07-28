# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 04:56:32 2021

@author: UBTOHTS
"""

import sys
from PyQt5 import QtWidgets
import pandas as pd
import sqlite3
import os

from main import MainWindow
class account(MainWindow):
    # def __init__(self):
    #     self.ui.textEdit.clear()
    
    # =============================================================================
    #     For print in textedit
    # =============================================================================
    
    def outputshown(self, y):
        # print('muje call kiya')
        x = y.upper()
        self.ui.textEdit_2.clear()
        self.ui.textEdit_2.append(x)
    
    # =============================================================================
    #     load data from the user idpass
    # =============================================================================        
    
    def loaddata(self):
        self.ui.sqloutput.clear()
        self.ui.sqloutput.setHorizontalHeaderLabels(["Email","Password"])
        stylesheet = "::section{color:rgb(0,0,0);}"
        self.ui.sqloutput.horizontalHeader().setStyleSheet(stylesheet)
        
        stylesheet = "::section{color:rgb(0,0,0);}"
        self.ui.sqloutput.verticalHeader().setStyleSheet(stylesheet)
            
        conn = sqlite3.connect(self.resource_path('sqldata/epassdata.db'))
        c = conn.cursor()
        sqlstr = 'select * from students'

        tablerow=0
        results = c.execute(sqlstr)
        for row in results:
            self.ui.sqloutput.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.sqloutput.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablerow+=1
    
    # =============================================================================
    #     For Refresh the data inside the QwidgetTable
    # =============================================================================
    
    def recall(self, enable):
        if enable:
            self.ui.sqloutput.clear()
            self.ui.sqloutput.setHorizontalHeaderLabels(["Email","Password"])
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.sqloutput.horizontalHeader().setStyleSheet(stylesheet)
            
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.sqloutput.verticalHeader().setStyleSheet(stylesheet)
            try:
                account.loaddata(self)
                print("Data refresh sucessfull")
                account.outputshown(self, "DATA REFRESH SUCCESFULLY")
            except:
                print("Data is not load succesfully")
                account.outputshown(self, "DATA IS NOT LOAD SUCCESFUL")
    def clsall(self, enable):
        if enable:
            self.ui.sqloutput.clear()
            self.ui.sqloutput.setHorizontalHeaderLabels(["Email","Password"])
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.sqloutput.horizontalHeader().setStyleSheet(stylesheet)
            
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.sqloutput.verticalHeader().setStyleSheet(stylesheet)
            try:
                self.ui.sqloutput.clear()
                print("Data clear sucessfull")
                account.outputshown(self, 'DATA CLEAR SUCCESSFUL')
                return True
            except:
                print("Data is not load succesfully")
                account.outputshown(self, 'PLS, ENTER A ID\'PASS...')

    # =============================================================================
    #     For add the data inside the idpass table 
    # =============================================================================

    def add(self, enable):
        if enable:
            self.ui.sqloutput.clear()
            self.ui.sqloutput.setHorizontalHeaderLabels(["Email","Password"])
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.sqloutput.horizontalHeader().setStyleSheet(stylesheet)
            
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.sqloutput.verticalHeader().setStyleSheet(stylesheet)
            
            email = self.ui.email_field.text()
            print(email)
            pas = self.ui.password_field.text()
            print(pas)

            try:
                conn = sqlite3.connect(self.resource_path('sqldata/epassdata.db'))
                c =  conn.cursor()
                c.execute("""CREATE TABLE IF NOT EXISTS students (email, pas)""")
                c.execute("INSERT INTO students (email,pas) VALUES (?,?)",(email,pas))
                conn.commit()
                c.close()
                print('Successful','Student is added successfully to the database.')
                account.outputshown(self, 'SUCCESSFUL, YOUR ID PASS IS SAVE IN HASH..\nSO DON\'T WORRY FROM THE HACKER')
                result=pd.read_sql_query("select * from students;",conn)
                print(result)
                conn.close()
                try:
                    account.recall(self, True)
                except:
                    print('data was not refresh successfull')

            except Exception as E:
                print('Error', 'Could not add student to the database\n', E)
                account.outputshown(self, 'save failed')

    # =============================================================================
    #     For remove all data in to the idpass table
    # =============================================================================

    def remove(self, enable):
        if enable:
            self.ui.sqloutput.clear()
            self.ui.sqloutput.setHorizontalHeaderLabels(["Email","Password"])
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.sqloutput.horizontalHeader().setStyleSheet(stylesheet)
            
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.sqloutput.verticalHeader().setStyleSheet(stylesheet)
            
            email = self.ui.email_field.text()
            print(email)
            
            try:
                conn = sqlite3.connect(self.resource_path('sqldata/epassdata.db'))
                sql = 'DELETE FROM students WHERE email=?'
                c = conn.cursor()
                c.execute(sql, (email,))
                conn.commit()
                c.close()
                result=pd.read_sql_query("select * from students;",conn)
                print(result)
                conn.close()
                print('Successful','Deleted From Table Successful')
                account.outputshown(self, 'DATA DELETED SUCCESSFUL\nALL HASH CLEAR AND ITS NOT RETRIEVABLE')
                if account.clsall(self, True) == True:
                    account.loaddata(self)
                    print("completly load ")
                else:
                    try:
                        new = account.clsall(self, True)
                        if new == True:
                            account.loaddata(self)
                            print("manually do it")
                    except:
                        print("close app something data was not load sucessfull")
                        account.outputshown(self, 'CLOSE APP SOMETHING BAD HAPPENED..')
            except Exception as E:
                print('Error', 'Could not Delete student from the database.\n', E)
                account.outputshown(self, "DATA NOT DELETED\nsomething bad happend")
