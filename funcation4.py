# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 20:19:11 2021

@author: UBTOHTS
"""

import sys
from PyQt5 import QtWidgets
import pandas as pd
import sqlite3
from sqlite3 import OperationalError
import os

from main import MainWindow
class lectable(MainWindow):
            
    def outputshown(self, x):
        self.ui.tb_error.clear()
        self.ui.lec_error.append(x)
            
    # =============================================================================
    #     Load the data from the lectable
    # =============================================================================
    
    def loadtbdata(self, enable):
        if enable:
            self.ui.lec_table.setHorizontalHeaderLabels(["LECTURE NAME","MS-SUB NAME", "MS-LEC NAME", "ALTER NAME"])
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.lec_table.horizontalHeader().setStyleSheet(stylesheet)
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.lec_table.verticalHeader().setStyleSheet(stylesheet)
            
            df = pd.DataFrame()
            rows = self.ui.lec_table.rowCount()
            print(rows)
            columnss = self.ui.lec_table.columnCount()   
            print(columnss)
            
            df_list = {}
            for col in range(columnss):
                df_list2 = []
                for row in range(rows):
                    table_item = self.ui.lec_table.item(row, col)
                    df_list2.append('' if table_item is None else str(table_item.text()))
                    headerit = self.ui.lec_table.horizontalHeaderItem(col)
                    nameit = str(col) if headerit is None else headerit.text()
                    df_list[nameit] = df_list2
        
            df = pd.DataFrame(data=df_list)
            print(df)
            try:
                conn = sqlite3.connect(self.resource_path('sqldata/lectable.db'))
                df.to_sql('lecdata', con=conn)
                conn.close()
                print('thara bhai work completely')
                lectable.outputshown(self, "Completely, save tha data")
            except Exception as e:
                print("exception rise:- ", e)
            except:
                print("It doesn't work")
                lectable.outputshown(self,"something wrong check again")
            # tablemanage.assigntbdata(self)
    
    # =============================================================================
    #     Delete the data from the lectable
    # =============================================================================
    
    def deleteeve(self, enable):
        if enable:
            self.ui.lec_table.setHorizontalHeaderLabels(["LECTURE NAME","MS-SUB NAME", "MS-LEC NAME", "ALTER NAME"])
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.lec_table.horizontalHeader().setStyleSheet(stylesheet)
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.lec_table.verticalHeader().setStyleSheet(stylesheet)
            try:
                conn = sqlite3.connect(self.resource_path('sqldata/lectable.db'))
                c = conn.cursor()
                c.execute('DROP TABLE lecdata')
                conn.commit()
                c.close()
                conn.close()
                print("completly work succesfully")
                lectable.outputshown(self, "Everything delete successul")
            except Exception as E:
                lectable.outputshown(self, "TABLE is comepletely deleted Make new one")
                print(E)
            except:
                print('sorry something going wrong')
                
    # =============================================================================
    #     For refresh the data in table
    # =============================================================================
                
    def refresh(self, enable):
        if enable:
            try:
                self.ui.lec_table.clear()
                self.ui.lec_table.setHorizontalHeaderLabels(["LECTURE NAME","MS-SUB NAME", "MS-LEC NAME", "ALTER NAME"])
                stylesheet = "::section{color:rgb(0,0,0);}"
                self.ui.lec_table.horizontalHeader().setStyleSheet(stylesheet)
                
                stylesheet = "::section{color:rgb(0,0,0);}"
                self.ui.lec_table.verticalHeader().setStyleSheet(stylesheet)
            
                conn = sqlite3.connect(self.resource_path('sqldata/lectable.db'))
                c = conn.cursor()
                sqlstr = 'select * from lecdata'
                
                tablerow = 0
                results = c.execute(sqlstr)
                
                for row in results:
                    print(row[1])
                    self.ui.lec_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
                    self.ui.lec_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
                    self.ui.lec_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
                    tablerow += 1
                print("i am doing my work completely")
                c.close()
                print("emit the database which i saved")
                conn.close()
                print("i am close the connection")
                lectable.outputshown(self, "REFRESH COMPLETELY")
            except OperationalError:
                print('Table is not defined mean a table is not exist make own your table')
            except:
                print("lode lage bhai")
                lectable.outputshown(self, "something going wrong ramu")