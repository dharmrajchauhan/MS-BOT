# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainmMFFZm.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide6.QtCore import *  # type: ignore
# from PySide6.QtGui import *  # type: ignore
# from PySide6.QtWidgets import *  # type: ignore
# MainWindow.setWindowIcon(QIcon('./image/profile.ico'))
from __future__ import annotations
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt, QRect, QObject, QCoreApplication, QMetaObject, QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QTabWidget, QGridLayout, QVBoxLayout, \
QHBoxLayout, QSizePolicy, QSpacerItem, QStyle, QStyleFactory, QPushButton, QFrame, QFontDialog, QStackedWidget,\
QLineEdit, QTextBrowser, QTextEdit, QPlainTextEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QCursor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowIcon(QIcon('image/profile.ico'))
        MainWindow.resize(1200, 580)
        MainWindow.setMinimumSize(QSize(1200, 580))
        MainWindow.setMaximumSize(QSize(1200, 580))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setGeometry(QRect(9, 9, 100, 522))
        self.frame_left_menu.setMinimumSize(QSize(100, 0))
        self.frame_left_menu.setMaximumSize(QSize(100, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setGeometry(QRect(10, 10, 83, 334))
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_1)

        self.btn_page_5 = QPushButton(self.frame_top_menus)
        self.btn_page_5.setObjectName(u"btn_page_5")
        self.btn_page_5.setMinimumSize(QSize(0, 40))
        self.btn_page_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_5)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_3)

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 40))
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_4)

        self.btn_page_7 = QPushButton(self.frame_top_menus)
        self.btn_page_7.setObjectName(u"btn_page_7")
        self.btn_page_7.setMinimumSize(QSize(0, 40))
        self.btn_page_7.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_7)

        self.btn_page_6 = QPushButton(self.frame_top_menus)
        self.btn_page_6.setObjectName(u"btn_page_6")
        self.btn_page_6.setMinimumSize(QSize(0, 40))
        self.btn_page_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_6)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setGeometry(QRect(90, 9, 1076, 522))
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1121, 541))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 1131, 551))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 872, 281))
        self.frame_2.setMaximumSize(QSize(872, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 911, 261))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 10, 901, 271))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 10, 821, 91))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 141, 26))
        self.label_2.setStyleSheet(u"color: rgb(255,255,255);\n"
"font-size: 14pt;")
        self.ms_link = QLineEdit(self.frame_10)
        self.ms_link.setObjectName(u"ms_link")
        self.ms_link.setGeometry(QRect(0, 50, 701, 22))
        self.ms_link.setStyleSheet(u"color: rgb(255,255,255);")
        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 126, 841, 111))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 1, 121, 31))
        self.label.setStyleSheet(u"color: rgb(255,255,255);\n"
"font-size: 14pt;")
        self.s_time = QLineEdit(self.frame_8)
        self.s_time.setObjectName(u"s_time")
        self.s_time.setGeometry(QRect(11, 41, 133, 22))
        self.s_time.setStyleSheet(u"color: rgb(255,255,255);")
        self.e_time = QLineEdit(self.frame_8)
        self.e_time.setObjectName(u"e_time")
        self.e_time.setGeometry(QRect(384, 41, 133, 22))
        self.e_time.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(384, 1, 101, 26))
        self.label_3.setStyleSheet(u"color: rgb(255,255,255);\n"
"font-size: 14pt;")
        self.submit_btn = QPushButton(self.frame_8)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(220, 80, 100, 24))
        self.submit_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 280, 1071, 232))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 20, 15, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 0))
        self.label_4.setMaximumSize(QSize(15000000, 15000000))
        self.label_4.setPixmap(QPixmap(u"image/1-5.png"))

        self.horizontalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.frame_7)
        self.textEdit.setObjectName(u"textEdit")
        font = QFont()
        font.setPointSize(9)
        font.setStyleStrategy(QFont.PreferDefault)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(255,255,255);\n"
"	border: 1px solid rgb(170, 255, 255);\n"
"}")
        self.textEdit.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.textEdit.setLineWrapColumnOrWidth(365)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.textEdit)


        self.horizontalLayout_5.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(924, 40, 141, 231))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.pushButton_3)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(-10, -10, 1131, 551))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(20, 0, 1051, 321))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 20, 611, 271))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.sqloutput = QTableWidget(self.frame_13)
        if (self.sqloutput.columnCount() < 2):
            self.sqloutput.setColumnCount(2)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.sqloutput.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem1.setForeground(brush);
        self.sqloutput.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.sqloutput.rowCount() < 10):
            self.sqloutput.setRowCount(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem2.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem3.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem4.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem5.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem6.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem7.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem8.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem9.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem10.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem11.setForeground(brush);
        self.sqloutput.setVerticalHeaderItem(9, __qtablewidgetitem11)
        self.sqloutput.setObjectName(u"sqloutput")
        self.sqloutput.setGeometry(QRect(0, 0, 571, 251))
        self.sqloutput.setStyleSheet(u"color: rgb(255,255,255);")
        self.sqloutput.setRowCount(10)
        self.sqloutput.setColumnCount(2)
        self.refresh = QPushButton(self.frame_13)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setGeometry(QRect(570, 0, 31, 271))
        self.refresh.setStyleSheet(u"color: rgb(255,255,255);")
        self.refresh.raise_()
        self.sqloutput.raise_()
        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(610, 10, 451, 271))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 40, 111, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_5.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 100, 111, 21))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_6.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.add_btn = QPushButton(self.frame_17)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(140, 170, 75, 24))
        self.add_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.sub_btn = QPushButton(self.frame_17)
        self.sub_btn.setObjectName(u"sub_btn")
        self.sub_btn.setGeometry(QRect(340, 170, 75, 24))
        self.sub_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.email_field = QLineEdit(self.frame_17)
        self.email_field.setObjectName(u"email_field")
        self.email_field.setGeometry(QRect(130, 43, 301, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.email_field.setFont(font2)
        self.email_field.setStyleSheet(u"color: rgb(255,255,255);")
        self.password_field = QLineEdit(self.frame_17)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(130, 103, 301, 21))
        self.password_field.setFont(font2)
        self.password_field.setStyleSheet(u"color: rgb(255,255,255);")
        self.password_field.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhSensitiveData)
        self.password_field.setReadOnly(False)
        self.frame_17.raise_()
        self.frame_13.raise_()
        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(20, 280, 1071, 232))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 20, 15, 0)
        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_18)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 0))
        self.label_8.setMaximumSize(QSize(15000000, 15000000))
        self.label_8.setPixmap(QPixmap(u"image/1-5.png"))

        self.horizontalLayout_8.addWidget(self.label_8)


        self.horizontalLayout_3.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.textEdit_2 = QTextEdit(self.frame_19)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(255,255,255);\n"
"	border: 1px solid rgb(170, 255, 255);\n"
"}")
        self.textEdit_2.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.textEdit_2.setLineWrapColumnOrWidth(365)
        self.textEdit_2.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.textEdit_2)


        self.horizontalLayout_3.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.frame_15 = QFrame(self.page_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, -10, 1111, 531))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 0, 1111, 460))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.time_table = QTableWidget(self.frame_16)
        if (self.time_table.columnCount() < 7):
            self.time_table.setColumnCount(7)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem12.setForeground(brush);
        self.time_table.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem13.setForeground(brush);
        self.time_table.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem14.setForeground(brush);
        self.time_table.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem15.setForeground(brush);
        self.time_table.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem16.setForeground(brush);
        self.time_table.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem17.setForeground(brush);
        self.time_table.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem18.setForeground(brush);
        self.time_table.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        if (self.time_table.rowCount() < 10):
            self.time_table.setRowCount(10)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem19.setForeground(brush);
        self.time_table.setVerticalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem20.setForeground(brush);
        self.time_table.setVerticalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem21.setForeground(brush);
        self.time_table.setVerticalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setBackground(QColor(255, 255, 255));
        self.time_table.setVerticalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem23.setForeground(brush);
        self.time_table.setVerticalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem24.setForeground(brush);
        self.time_table.setVerticalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem25.setForeground(brush);
        self.time_table.setVerticalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem26.setForeground(brush);
        self.time_table.setVerticalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem27.setForeground(brush);
        self.time_table.setVerticalHeaderItem(8, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem28.setForeground(brush);
        self.time_table.setVerticalHeaderItem(9, __qtablewidgetitem28)
        self.time_table.setObjectName(u"time_table")
        self.time_table.setGeometry(QRect(20, 10, 1045, 450))
        self.time_table.setStyleSheet(u"color: rgb(255,255,255);")
        self.time_table.setRowCount(10)
        self.time_table.setColumnCount(7)
        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 470, 1121, 50))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.new_tb_btn = QPushButton(self.frame_20)
        self.new_tb_btn.setObjectName(u"new_tb_btn")
        self.new_tb_btn.setGeometry(QRect(20, 15, 131, 24))
        self.new_tb_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.conf_tb_btn = QPushButton(self.frame_20)
        self.conf_tb_btn.setObjectName(u"conf_tb_btn")
        self.conf_tb_btn.setGeometry(QRect(210, 15, 150, 24))
        self.conf_tb_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.refr_btn = QPushButton(self.frame_20)
        self.refr_btn.setObjectName(u"refr_btn")
        self.refr_btn.setGeometry(QRect(420, 15, 150, 24))
        self.refr_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.tb_error = QTextEdit(self.frame_20)
        self.tb_error.setObjectName(u"tb_error")
        self.tb_error.setGeometry(QRect(690, 10, 371, 31))
        self.tb_error.setFont(font)
        self.tb_error.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(255,255,255);\n"
"	border: 1px solid rgb(170, 255, 255);\n"
"}")
        self.tb_error.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.tb_error.setLineWrapColumnOrWidth(365)
        self.tb_error.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.frame_21 = QFrame(self.page_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(10, -20, 1081, 531))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.lec_table = QTableWidget(self.frame_21)
        if (self.lec_table.columnCount() < 4):
            self.lec_table.setColumnCount(4)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem29.setForeground(brush);
        self.lec_table.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem30.setForeground(brush);
        self.lec_table.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem31.setForeground(brush);
        self.lec_table.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem32.setForeground(brush);
        self.lec_table.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        if (self.lec_table.rowCount() < 20):
            self.lec_table.setRowCount(20)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem33.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem34.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem35.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem36.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem37.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem38.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem39.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(6, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem40.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(7, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem41.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(8, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem42.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(9, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem43.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(10, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem44.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(11, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem45.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(12, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem46.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(13, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem47.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(14, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem48.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(15, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem49.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(16, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem50.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(17, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem51.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(18, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem52.setForeground(brush);
        self.lec_table.setVerticalHeaderItem(19, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.lec_table.setItem(0, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.lec_table.setItem(0, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.lec_table.setItem(0, 2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.lec_table.setItem(1, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.lec_table.setItem(1, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.lec_table.setItem(1, 2, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.lec_table.setItem(2, 0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.lec_table.setItem(2, 1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.lec_table.setItem(2, 2, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.lec_table.setItem(3, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.lec_table.setItem(3, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.lec_table.setItem(3, 2, __qtablewidgetitem64)
        self.lec_table.setObjectName(u"lec_table")
        self.lec_table.setGeometry(QRect(5, 21, 1000, 471))
        self.lec_table.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.new_lec_btn = QPushButton(self.frame_21)
        self.new_lec_btn.setObjectName(u"new_lec_btn")
        self.new_lec_btn.setGeometry(QRect(1010, 20, 31, 101))
        self.new_lec_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.refre_lec_btn = QPushButton(self.frame_21)
        self.refre_lec_btn.setObjectName(u"refre_lec_btn")
        self.refre_lec_btn.setGeometry(QRect(1010, 240, 31, 271))
        self.refre_lec_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.conf_lec_btn = QPushButton(self.frame_21)
        self.conf_lec_btn.setObjectName(u"conf_lec_btn")
        self.conf_lec_btn.setGeometry(QRect(1010, 130, 31, 101))
        self.conf_lec_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.lec_error = QTextEdit(self.frame_21)
        self.lec_error.setObjectName(u"lec_error")
        self.lec_error.setGeometry(QRect(310, 500, 401, 31))
        self.lec_error.setFont(font)
        self.lec_error.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(255,255,255);\n"
"	border: 1px solid rgb(170, 255, 255);\n"
"}")
        self.lec_error.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.lec_error.setLineWrapColumnOrWidth(365)
        self.lec_error.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.frame_22 = QFrame(self.page_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(0, -10, 1091, 521))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(10, 0, 1081, 211))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_23)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 10, 161, 41))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 12pt;")
        self.auto_error = QTextEdit(self.frame_23)
        self.auto_error.setObjectName(u"auto_error")
        self.auto_error.setGeometry(QRect(650, 30, 401, 171))
        self.auto_error.setFont(font)
        self.auto_error.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(255,255,255);\n"
"	border: 1px solid rgb(170, 255, 255);\n"
"}")
        self.auto_error.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.auto_error.setLineWrapColumnOrWidth(365)
        self.auto_error.setReadOnly(True)
        self.antaryami = QPushButton(self.frame_23)
        self.antaryami.setObjectName(u"antaryami")
        self.antaryami.setGeometry(QRect(80, 90, 331, 41))
        self.antaryami.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(10, 205, 1081, 301))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_24)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(200, 10, 171, 41))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 12pt;")
        self.c_error = QTextEdit(self.frame_24)
        self.c_error.setObjectName(u"c_error")
        self.c_error.setGeometry(QRect(650, 50, 401, 241))
        self.c_error.setFont(font)
        self.c_error.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(255,255,255);\n"
"	border: 1px solid rgb(170, 255, 255);\n"
"}")
        self.c_error.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.c_error.setLineWrapColumnOrWidth(365)
        self.c_error.setReadOnly(True)
        self.c_lec_join = QLineEdit(self.frame_24)
        self.c_lec_join.setObjectName(u"c_lec_join")
        self.c_lec_join.setGeometry(QRect(340, 70, 81, 21))
        self.c_lec_join.setFont(font2)
        self.c_lec_join.setStyleSheet(u"color: rgb(255,255,255);")
        self.c_lec_leave = QLineEdit(self.frame_24)
        self.c_lec_leave.setObjectName(u"c_lec_leave")
        self.c_lec_leave.setGeometry(QRect(340, 110, 81, 21))
        self.c_lec_leave.setFont(font2)
        self.c_lec_leave.setStyleSheet(u"color: rgb(255,255,255);")
        self.c_lec_join_2 = QLineEdit(self.frame_24)
        self.c_lec_join_2.setObjectName(u"c_lec_join_2")
        self.c_lec_join_2.setGeometry(QRect(340, 150, 81, 21))
        self.c_lec_join_2.setFont(font2)
        self.c_lec_join_2.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_10 = QLabel(self.frame_24)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 70, 301, 21))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_10.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.label_11 = QLabel(self.frame_24)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 150, 301, 21))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_11.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.label_12 = QLabel(self.frame_24)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 110, 301, 21))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_12.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.label_13 = QLabel(self.frame_24)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 190, 301, 21))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_13.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.c_lab_leave = QLineEdit(self.frame_24)
        self.c_lab_leave.setObjectName(u"c_lab_leave")
        self.c_lab_leave.setGeometry(QRect(340, 190, 81, 21))
        self.c_lab_leave.setFont(font2)
        self.c_lab_leave.setStyleSheet(u"color: rgb(255,255,255);")
        self.c_thread_time = QLineEdit(self.frame_24)
        self.c_thread_time.setObjectName(u"c_thread_time")
        self.c_thread_time.setGeometry(QRect(340, 230, 81, 21))
        self.c_thread_time.setFont(font2)
        self.c_thread_time.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_14 = QLabel(self.frame_24)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 230, 291, 21))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_14.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.antaryami_2 = QPushButton(self.frame_24)
        self.antaryami_2.setObjectName(u"antaryami_2")
        self.antaryami_2.setGeometry(QRect(500, 70, 91, 181))
        self.antaryami_2.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.frame_25 = QFrame(self.page_6)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(-10, -10, 1131, 551))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(20, 280, 1071, 232))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(1, 21, 687, 210))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_28)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1, 1, 685, 208))
        self.label_15.setMinimumSize(QSize(200, 0))
        self.label_15.setMaximumSize(QSize(15000000, 15000000))
        self.label_15.setPixmap(QPixmap(u"image/1-5.png"))
        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(698, 21, 357, 210))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.textEdit_3 = QTextEdit(self.frame_29)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(1, 1, 355, 208))
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(255,255,255);\n"
"	border: 1px solid rgb(170, 255, 255);\n"
"}")
        self.textEdit_3.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.textEdit_3.setLineWrapColumnOrWidth(365)
        self.textEdit_3.setReadOnly(True)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(10, 10, 1081, 261))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.textEdit_4 = QTextEdit(self.frame_26)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(290, 0, 751, 241))
        font3 = QFont()
        font3.setPointSize(11)
        self.textEdit_4.setFont(font3)
        self.textEdit_4.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(255,255,255);\n"
"	border: 1px solid rgb(170, 255, 255);\n"
"}")
        self.update_checker = QPushButton(self.frame_26)
        self.update_checker.setObjectName(u"update_checker")
        self.update_checker.setGeometry(QRect(30, 0, 241, 91))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.update_checker.setFont(font4)
        self.update_checker.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.update_checker.setInputMethodHints(Qt.ImhNone)
        self.update_checker.setAutoDefault(False)
        self.bug_report = QPushButton(self.frame_26)
        self.bug_report.setObjectName(u"bug_report")
        self.bug_report.setGeometry(QRect(30, 150, 241, 91))
        self.bug_report.setFont(font4)
        self.bug_report.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.bug_report.setInputMethodHints(Qt.ImhNone)
        self.bug_report.setAutoDefault(False)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.frame_30 = QFrame(self.page_7)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(10, 0, 1081, 521))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(0, 0, 1001, 551))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.stackedWidget_2 = QStackedWidget(self.frame_31)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 0, 1001, 470))
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.aaa = QWidget()
        self.aaa.setObjectName(u"aaa")
        self.frame_32 = QFrame(self.aaa)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(0, 0, 1001, 541))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_32)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 20, 1011, 431))
        self.label_19.setPixmap(QPixmap(u"image/1st complete.jpg"))
        self.label_19.setScaledContents(True)
        self.label_20 = QLabel(self.frame_32)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, -10, 1001, 51))
        font5 = QFont()
        font5.setPointSize(14)
        self.label_20.setFont(font5)
        self.label_20.setStyleSheet(u"color: rgb(0, 255, 255);\n"
"background-color: rgb(12, 32, 53);\n"
"text-align: center")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(self.aaa)
        self.bbb = QWidget()
        self.bbb.setObjectName(u"bbb")
        self.frame_33 = QFrame(self.bbb)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(0, 0, 1001, 551))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_33)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 0, 1001, 450))
        self.label_24.setPixmap(QPixmap(u"image/2nd complete.jpg"))
        self.label_24.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.bbb)
        self.ccc = QWidget()
        self.ccc.setObjectName(u"ccc")
        self.frame_34 = QFrame(self.ccc)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(0, 0, 1001, 551))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_34)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 0, 1001, 450))
        self.label_28.setPixmap(QPixmap(u"image/3rd complete.jpg"))
        self.label_28.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.ccc)
        self.ddd = QWidget()
        self.ddd.setObjectName(u"ddd")
        self.frame_35 = QFrame(self.ddd)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(0, 0, 1001, 551))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.label_32 = QLabel(self.frame_35)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(0, 0, 1001, 450))
        self.label_32.setPixmap(QPixmap(u"image/weblinker.jpg"))
        self.label_32.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.ddd)
        self.eee = QWidget()
        self.eee.setObjectName(u"eee")
        self.frame_40 = QFrame(self.eee)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setGeometry(QRect(0, 0, 1011, 551))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.label_38 = QLabel(self.frame_40)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(0, 0, 1004, 452))
        self.label_38.setPixmap(QPixmap(u"image/mail-id.jpg"))
        self.label_38.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.eee)
        self.fff = QWidget()
        self.fff.setObjectName(u"fff")
        self.frame_36 = QFrame(self.fff)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(0, 0, 1011, 551))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.label_37 = QLabel(self.frame_36)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(-2, -2, 1004, 452))
        self.label_37.setPixmap(QPixmap(u"image/timetable manager.jpg"))
        self.label_37.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.fff)
        self.ggg = QWidget()
        self.ggg.setObjectName(u"ggg")
        self.frame_37 = QFrame(self.ggg)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(0, 0, 1001, 551))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.label_41 = QLabel(self.frame_37)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(0, 0, 1001, 450))
        self.label_41.setPixmap(QPixmap(u"image/lecname understading....jpg"))
        self.label_41.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.ggg)
        self.hhh = QWidget()
        self.hhh.setObjectName(u"hhh")
        self.frame_38 = QFrame(self.hhh)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setGeometry(QRect(0, 0, 1001, 551))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.label_45 = QLabel(self.frame_38)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(0, -1, 1001, 451))
        self.label_45.setPixmap(QPixmap(u"image/antaryamimi.jpg"))
        self.label_45.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.hhh)
        self.frame_39 = QFrame(self.frame_30)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(0, 450, 1091, 61))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.label_46 = QLabel(self.frame_39)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, 10, 1001, 51))
        self.label_46.setStyleSheet(u"background-color: rgb(33, 37, 39);")
        self.next = QPushButton(self.frame_39)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(660, 20, 221, 24))
        self.next.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.prev = QPushButton(self.frame_39)
        self.prev.setObjectName(u"prev")
        self.prev.setGeometry(QRect(140, 20, 221, 24))
        self.prev.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(103, 255, 2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_7)
        self.frame_pages.raise_()
        self.frame_left_menu.raise_()

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.update_checker.setDefault(False)
        self.bug_report.setDefault(False)
        self.stackedWidget_2.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MS-BOT", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"D_LINK", None))
        self.btn_page_5.setText(QCoreApplication.translate("MainWindow", u"ANTARYAMI", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"ID_PASS", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"TIME TABLE", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"LEC_NAME", None))
        self.btn_page_7.setText(QCoreApplication.translate("MainWindow", u"INFO", None))
        self.btn_page_6.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Microsoft Link", None))
        self.ms_link.setText("")
        self.ms_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start Time", None))
        self.s_time.setPlaceholderText(QCoreApplication.translate("MainWindow", u"12:32", None))
        self.e_time.setPlaceholderText(QCoreApplication.translate("MainWindow", u"13:32", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"End Time", None))
        self.submit_btn.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
        self.label_4.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Audio\n"
"Recording", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Video\n"
"recording", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Screen\n"
"Capture", None))
        ___qtablewidgetitem = self.sqloutput.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem1 = self.sqloutput.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None));
        ___qtablewidgetitem2 = self.sqloutput.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem3 = self.sqloutput.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem4 = self.sqloutput.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem5 = self.sqloutput.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem6 = self.sqloutput.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem7 = self.sqloutput.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem8 = self.sqloutput.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem9 = self.sqloutput.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem10 = self.sqloutput.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem11 = self.sqloutput.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.refresh.setText(QCoreApplication.translate("MainWindow", u"R\n"
"E\n"
"F\n"
"R\n"
"E\n"
"S\n"
"H", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.sub_btn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.password_field.setText("")
        self.label_8.setText("")
        ___qtablewidgetitem12 = self.time_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"TIME", None));
        ___qtablewidgetitem13 = self.time_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"MONDAY", None));
        ___qtablewidgetitem14 = self.time_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TUESDAY", None));
        ___qtablewidgetitem15 = self.time_table.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"WEDNESDAY", None));
        ___qtablewidgetitem16 = self.time_table.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"THURSDAY", None));
        ___qtablewidgetitem17 = self.time_table.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"FRIDAY", None));
        ___qtablewidgetitem18 = self.time_table.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"SATURDAY", None));
        ___qtablewidgetitem19 = self.time_table.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem20 = self.time_table.verticalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem21 = self.time_table.verticalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem22 = self.time_table.verticalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem23 = self.time_table.verticalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem24 = self.time_table.verticalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem25 = self.time_table.verticalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem26 = self.time_table.verticalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem27 = self.time_table.verticalHeaderItem(8)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem28 = self.time_table.verticalHeaderItem(9)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.new_tb_btn.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
        self.conf_tb_btn.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
        self.refr_btn.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        self.tb_error.setPlaceholderText("")
        ___qtablewidgetitem29 = self.lec_table.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"LECTURE NAME", None));
        ___qtablewidgetitem30 = self.lec_table.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"MS-SUB NAME", None));
        ___qtablewidgetitem31 = self.lec_table.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"MS-LEC NAME", None));
        ___qtablewidgetitem32 = self.lec_table.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ALTER NAME", None));
        ___qtablewidgetitem33 = self.lec_table.verticalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem34 = self.lec_table.verticalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem35 = self.lec_table.verticalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem36 = self.lec_table.verticalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem37 = self.lec_table.verticalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem38 = self.lec_table.verticalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem39 = self.lec_table.verticalHeaderItem(6)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem40 = self.lec_table.verticalHeaderItem(7)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem41 = self.lec_table.verticalHeaderItem(8)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem42 = self.lec_table.verticalHeaderItem(9)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem43 = self.lec_table.verticalHeaderItem(10)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem44 = self.lec_table.verticalHeaderItem(11)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem45 = self.lec_table.verticalHeaderItem(12)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem46 = self.lec_table.verticalHeaderItem(13)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem47 = self.lec_table.verticalHeaderItem(14)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem48 = self.lec_table.verticalHeaderItem(15)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem49 = self.lec_table.verticalHeaderItem(16)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem50 = self.lec_table.verticalHeaderItem(17)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem51 = self.lec_table.verticalHeaderItem(18)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem52 = self.lec_table.verticalHeaderItem(19)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"20", None));

        __sortingEnabled = self.lec_table.isSortingEnabled()
        self.lec_table.setSortingEnabled(False)
        self.lec_table.setSortingEnabled(__sortingEnabled)

        self.new_lec_btn.setText(QCoreApplication.translate("MainWindow", u"N\n"
"E\n"
"W", None))
        self.refre_lec_btn.setText(QCoreApplication.translate("MainWindow", u"R\n"
"E\n"
"F\n"
"R\n"
"E\n"
"S\n"
"H", None))
        self.conf_lec_btn.setText(QCoreApplication.translate("MainWindow", u"C\n"
"O\n"
"N\n"
"F", None))
        self.lec_error.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DEFAULT BOT", None))
        self.auto_error.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.auto_error.setPlaceholderText(QCoreApplication.translate("MainWindow", u"It's a fully automatic bot. which attend you all online lectures within a given period. This bot has a Shweta checker function so don't worry about your mike and video. This bot comes with a default time of 15 minutes to detect whether the particular lecture is a start or not (the counting of times starts when you press the start button) If the lecture has not started then it will sleep and is waking up again at the next lecture time. If there are more than 10 students only then the bot will join the class. And last but not least bot will automatically leave the class if there are fewer than 10 students.", None))
        self.antaryami.setText(QCoreApplication.translate("MainWindow", u"PRESS IT AND ENJOY IT", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"CUSTOM BOT", None))
        self.c_error.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CUSTOMIZE IT BY YOUR NEEDS", None))
        self.c_lec_join.setPlaceholderText(QCoreApplication.translate("MainWindow", u"15", None))
        self.c_lec_leave.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10", None))
        self.c_lec_join_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Min.  students for join", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Min. students for Join in lab", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Min. students for leave", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Min. students for leave in lab", None))
        self.c_lab_leave.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3", None))
        self.c_thread_time.setPlaceholderText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Thread Time for searching starting class", None))
        self.antaryami_2.setText(QCoreApplication.translate("MainWindow", u"RIDER\n"
"PROVIDER", None))
        self.label_15.setText("")
        self.update_checker.setText(QCoreApplication.translate("MainWindow", u"UPDATE\n"
"CHECKER", None))
        self.bug_report.setText(QCoreApplication.translate("MainWindow", u"BUG REPORT\n"
"SUBMIT", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"FOR AUTOMATION IT'S NEEDED.", None))
        self.label_24.setText("")
        self.label_28.setText("")
        self.label_32.setText("")
        self.label_38.setText("")
        self.label_37.setText("")
        self.label_41.setText("")
        self.label_45.setText("")
        self.label_46.setText("")
        self.next.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.prev.setText(QCoreApplication.translate("MainWindow", u"PREVIOUS", None))
    # retranslateUi





























