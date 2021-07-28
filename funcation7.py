# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 18:01:43 2021

@author: LENOVO
"""

import os
import sys
from PyQt5 import QtWidgets
import pandas as pd
import sqlite3
from sqlite3 import OperationalError
from main import MainWindow

class bug_report(MainWindow):
    
    def bugs(self, enable):
        if enable:
            self.ui.textEdit_4.clear()
            def outputshown(self, x):                
                self.ui.textEdit_4.append(x)
            
            print("report submitted")
            outputshown(self, "REPORT SUBMIT SUCCESFULLY BHAI JAN")


