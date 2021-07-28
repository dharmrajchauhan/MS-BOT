# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 21:27:38 2021

@author: UBTOHTS
"""
import os
import sys
from PyQt5 import QtWidgets
import pandas as pd
import sqlite3
from sqlite3 import OperationalError
from main import MainWindow

class tablemanage(MainWindow):
    
    
    def outputshown(self, y):
        x = y.upper()
        self.ui.tb_error.clear()
        self.ui.tb_error.append(x)

    # =============================================================================
    #     Assign new data and delete exciting data
    # =============================================================================
        
    def assigntbdata(self):
        self.ui.time_table.setHorizontalHeaderLabels(["TIME","MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"])
        stylesheet = "::section{color:rgb(0,0,0);}"
        self.ui.time_table.horizontalHeader().setStyleSheet(stylesheet)
        stylesheet = "::section{color:rgb(0,0,0);}"
        self.ui.time_table.verticalHeader().setStyleSheet(stylesheet)
        try:
            def resultpasser():
                conn = sqlite3.connect(self.resource_path('sqldata/timetable.db'))
                c = conn.cursor()
                sqlstr = 'select * from tbdata'
                results = c.execute(sqlstr)
                print("i get the data from timetable")
                return results, conn, c
            #--------------------------------------result grabbing successfull
            try:
                conv1=None
                if conv1 == None:
                    conv1=sqlite3.connect(self.resource_path('sqldata/timetablev1.db'))
            
                cv1 = conv1.cursor()
            #--------------------------------------deleting exciting table    
                try:
                    cv1.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='tb' ''')
                    if cv1.fetchone()[0]==1 : 
                        print('Table exists.')
                        try:
                            cv1.execute('''DROP TABLE tb ''')
                            print('Table deleted successfully')
                            # self.outputshown('Table deleted successfully')
                        except:
                            print('something going wrong')
                    else :
                        print('Table does not exist.')
                        # self.outputshown('Table does not exist.')
                except:
                    print('table is not created ya table is not delted')
                    tablemanage.outputshown("buddy data is not created ya empty so pls first make it thn confirm")
                
                cv1.execute("""CREATE TABLE IF NOT EXISTS tb (name, start_time, end_time, day)""")
                result, conn, c  = resultpasser()
                for row in result:
                    # print(row[1])
                    try:
                        combtime = str(row[1]).split('-')
                        star_time = combtime[0]
                        end_time = combtime[1]
                        
                    
                        cv1.execute(f"""INSERT INTO tb (name, start_time, end_time, day) values('{row[2]}','{star_time}','{end_time}','monday')""")
                        print(star_time, end_time, row[2])
                        cv1.execute(f"""INSERT INTO tb (name, start_time, end_time, day) values('{row[3]}','{star_time}','{end_time}','tuesday')""")
                        print(star_time, end_time, row[3])
                        cv1.execute(f"""INSERT INTO tb (name, start_time, end_time, day) values('{row[4]}','{star_time}','{end_time}','wednesday')""")
                        print(star_time, end_time, row[4])
                        cv1.execute(f"""INSERT INTO tb (name, start_time, end_time, day) values('{row[5]}','{star_time}','{end_time}','thursday')""")
                        print(star_time, end_time, row[5])
                        cv1.execute(f"""INSERT INTO tb (name, start_time, end_time, day) values('{row[6]}','{star_time}','{end_time}','friday')""")
                        print(star_time, end_time, row[6])
                        cv1.execute(f"""INSERT INTO tb (name, start_time, end_time, day) values('{row[7]}','{star_time}','{end_time}','saturday')""")
                        print(star_time, end_time, row[7])
                        # cv1.execute(f"""INSERT INTO tb (name, start_time, end_time, day) values('{row[8]}','{star_time}','{end_time}','sunday')""")
                        # print(star_time, end_time, row[8])
                        conv1.commit()
                    except:
                        pass
                print("All data is compteley save")
                tablemanage.outputshown(self, "All data is completely save")
                conv1.close()
                cv1.close()
                c.close()
                conn.close()
            except sqlite3.ProgrammingError:
                print("Programming error is occure buddy")
                pass
        except:
            print('timetable is not detected so timetablev1 is not created')
            tablemanage.outputshown(self, "Something going wrong/nfirst click on new and then after intialize your new data")
    
    # =============================================================================
    #     Load data from the database and refresh it
    # =============================================================================            

    def loadtbdata(self, enable):
        self.ui.time_table.setHorizontalHeaderLabels(["TIME","MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"])
        stylesheet = "::section{color:rgb(0,0,0);}"
        self.ui.time_table.horizontalHeader().setStyleSheet(stylesheet)
        stylesheet = "::section{color:rgb(0,0,0);}"
        self.ui.time_table.verticalHeader().setStyleSheet(stylesheet)
        if enable:
            df = pd.DataFrame()
            rows = self.ui.time_table.rowCount()
            print(rows)
            columnss = self.ui.time_table.columnCount()   
            print(columnss)
            # headers = [str(self.ui.time_table.horizontalHeaderItem(i).text()) for i in range(columnss)]
            
            df_list = {}
            for col in range(columnss):
                df_list2 = []
                for row in range(rows):
                    table_item = self.ui.time_table.item(row, col)
                    df_list2.append('' if table_item is None else str(table_item.text()))
                    headerit = self.ui.time_table.horizontalHeaderItem(col)
                    nameit = str(col) if headerit is None else headerit.text()
                    df_list[nameit] = df_list2
        
            df = pd.DataFrame(data=df_list)
            print(df)
            try:
                conn = sqlite3.connect(self.resource_path('sqldata/timetable.db'))
                df.to_sql('tbdata', con=conn)
                conn.close()
                print('thara bhai work completely')
                tablemanage.outputshown(self, "Completely, save tha data")
            except Exception as e:
                print("exception rise:- ", e)
            except:
                print("It doesn't work")
            
            tablemanage.assigntbdata(self)

    # =============================================================================
    #     
    # =============================================================================

    def deleteeve(self, enable):
        if enable:
            self.ui.time_table.setHorizontalHeaderLabels(["TIME","MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"])
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.time_table.horizontalHeader().setStyleSheet(stylesheet)
            stylesheet = "::section{color:rgb(0,0,0);}"
            self.ui.time_table.verticalHeader().setStyleSheet(stylesheet)
            try:
                conn = sqlite3.connect(self.resource_path('sqldata/timetable.db'))
                c = conn.cursor()
                c.execute('DROP TABLE tbdata')
                conn.commit()
                c.close()
                conn.close()
                print("completly work succesfully")
                tablemanage.outputshown(self, "successfully data deleted")
            except Exception as E:
                print(E)
                tablemanage.outputshown(self, "Table is not created pls create first")
            except:
                print('sorry something going wrong')
                tablemanage.outputshown(self, "idk but something bad happend, so close it and try again..")

    # =============================================================================
    #     For refresh the table in the database
    # =============================================================================

    def refresh(self, enable):
        if enable:
            try:
                self.ui.time_table.clear()
                self.ui.time_table.setHorizontalHeaderLabels(["TIME","MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"])
                stylesheet = "::section{color:rgb(0,0,0);}"
                self.ui.time_table.horizontalHeader().setStyleSheet(stylesheet)
                
                stylesheet = "::section{color:rgb(0,0,0);}"
                self.ui.time_table.verticalHeader().setStyleSheet(stylesheet)
                
                
                conn = sqlite3.connect(self.resource_path('sqldata/timetable.db'))
                c = conn.cursor()
                sqlstr = 'select * from tbdata'
                
                tablerow = 0
                results = c.execute(sqlstr)
                
                for row in results:
                    print(row[1])
                    self.ui.time_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
                    self.ui.time_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
                    self.ui.time_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
                    self.ui.time_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
                    self.ui.time_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
                    self.ui.time_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[6]))
                    self.ui.time_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[7]))
                    tablerow += 1
                print("i am doing my work completely")
                c.close()
                print("emit the database which i saved")
                conn.close()
                print("i am close the connection")
                tablemanage.outputshown(self, "LOADING DATA SUCCESSFULL")
            except OperationalError:
                print('Table is not defined mean a table is not exist make own your table')
                tablemanage.outputshown(self, 'TABLE IS EMPTY BUDDY, PLS ENTER A DATA')
            except Exception as E:
                print("lode lage bhai", E)
                tablemanage.outputshown(self, 'SOMETHING BAD HAPPENED, SHUT THE APP AND AGAIN TRY..')

#---------------------------------------------------------------------------------------------------------                
