#let's start with the shayri as i do always, at the begining of the project

"""
Tuje likhne me din chala gaya,
    sochne me rat bita du kya...

Ye barish ka mausam bada achha he,
    tuje bhi coding sikha du kya...
"""

# =============================================================================
#   Import Library
# =============================================================================
from __future__ import print_function
import os
import sys
# from PyQt5.uic import loadUi
# from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QRect, QObject, QCoreApplication, QMetaObject, QPropertyAnimation, QTimer, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QTabWidget, QGridLayout, QVBoxLayout, \
QHBoxLayout, QSizePolicy, QSpacerItem, QStyle, QStyleFactory, QPushButton, QFrame, QFontDialog, QStackedWidget, \
QMainWindow, QMessageBox, QTableWidget, QGraphicsDropShadowEffect, QSystemTrayIcon, QMenu, qApp
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QKeySequence
# import sqlite3


import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials



from ui_main import Ui_MainWindow
# from ui_image import Ui_MainWindow1
# from ui_splash_screen import Ui_SplashScreen

# =============================================================================
#   Mainwindow of qt5
# =============================================================================
class MainWindow(QMainWindow):
    # =============================================================================
    #     initilize a mainwindow as self
    # =============================================================================
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('image/profile.ico'))
        
        # self._menu = QMenu()
        # self._menu.addAction("&Quit", qApp.quit, QKeySequence.Quit)

        # self._trayIcon = QSystemTrayIcon(QIcon('image/profile.ico'), self)
        # self._trayIcon.setContextMenu(self._menu)
        # self._trayIcon.show()
        
        self.ui.label_4.setPixmap(QPixmap(self.resource_path('image/1-5.png')))
        self.ui.label_8.setPixmap(QPixmap(self.resource_path('image/1-5.png')))
        self.ui.label_15.setPixmap(QPixmap(self.resource_path('image/1-5.png')))
        
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.sqloutput.setColumnWidth(0, 370)
        self.ui.sqloutput.setColumnWidth(1, 200)
        self.ui.sqloutput.setHorizontalHeaderLabels(["Email","Password"])
        
        for i in range(7):
          self.ui.time_table.setColumnWidth(i,150)
        
        for i in range(11):
          self.ui.time_table.setRowHeight(i,60)
          
        for i in range(20):
          self.ui.lec_table.setRowHeight(i,60)
        
        self.ui.lec_table.setColumnWidth(0, 200)
        self.ui.lec_table.setColumnWidth(1, 300)
        self.ui.lec_table.setColumnWidth(2, 220)
        self.ui.lec_table.setColumnWidth(3, 220)
        self.ui.time_table.setHorizontalHeaderLabels(["TIME","MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"])
        self.ui.textEdit.setText("DON'T ENTER WRONG INPUT OTHERWISE APP WILL CLOSE")
        self.ui.textEdit_4.setText("VERSION:-0.67\nSECURITY VERSION:-0.3\nENCRYPTION:-MD5 HASH\nGITHHUB:-SOON...\n\nNEXT UPDATE DETAILS:-HEADERLESS CHROME DRIVER\n\t\tRECORDING FEATURE FOR ALL USER\n\t\tAI IMPLEMENTATION")
        
        
        ## TOGGLE/BURGUER MENU
        ########################################################################
        # self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.btn_page_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        self.ui.btn_page_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
        self.ui.btn_page_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))
        self.ui.btn_page_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.stackedWidget_2.setCurrentIndex(0)))
        
        
        try:
            import funcation1
            self.ui.submit_btn.clicked.connect(lambda: funcation1.UIFunctions.weblinkopener(self, True))
            # self.ui.submit_btn.clicked.connect(self.weblinkstarter)
            import funcation2
            self.ui.add_btn.clicked.connect(lambda: funcation2.account.add(self, True))
            self.ui.sub_btn.clicked.connect(lambda: funcation2.account.remove(self, True))
            # self.ui.sub_btn.clicked.connect(lambda: funcation2.account.clsall(self, True))
            self.ui.refresh.clicked.connect(lambda: funcation2.account.recall(self, True))
            
            import funcation3
            self.ui.conf_tb_btn.clicked.connect(lambda: funcation3.tablemanage.loadtbdata(self, True))
            self.ui.new_tb_btn.clicked.connect(lambda: funcation3.tablemanage.deleteeve(self, True))
            self.ui.refr_btn.clicked.connect(lambda: funcation3.tablemanage.refresh(self, True))
            
            import funcation4
            self.ui.new_lec_btn.clicked.connect(lambda: funcation4.lectable.deleteeve(self, True))
            self.ui.refre_lec_btn.clicked.connect(lambda: funcation4.lectable.refresh(self, True))
            self.ui.conf_lec_btn.clicked.connect(lambda: funcation4.lectable.loadtbdata(self, True))
            
            import funcation5
            self.ui.antaryami.clicked.connect(lambda: funcation5.antar_yami.ubtohts(self, True))
            
            import funcation6
            self.ui.antaryami_2.clicked.connect(lambda: funcation6.antar_yami2.ubtohts(self, True))
            self.ui.update_checker.clicked.connect(lambda: self.updatechecker())
            
            self.ui.next.clicked.connect(lambda: self.nextWidget())
            self.ui.prev.clicked.connect(lambda: self.previousWidget())
            
            import funcation7
            self.ui.bug_report.clicked.connect(lambda: funcation7.bug_report.bugs(self, True))
        except:
            pass
        
        # self.show()
    # =============================================================================
    #   For close the app
    # =============================================================================
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            print('Window closed')
        else:
            event.ignore()
    
    # @pyqtSlot()
    # def setProfile(self):
    #     if QMessageBox.question(self, "Quit?", "Quit?") != QMessageBox.No:
    #         qApp.quit()
    #     self.hide()
    
    # =============================================================================
    #   for making pwd+dir path
    # =============================================================================
    
    def resource_path(self, path):
        frozen = 'not'
        if getattr(sys, 'frozen', False):
                # we are running in executable mode
                frozen = 'ever so'
                app_dir = sys._MEIPASS
        else:
                # we are running in a normal Python environment
                app_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(app_dir, path)
    
    # =============================================================================
    #   Info Menu's next and previous button
    # =============================================================================
    
    def nextWidget(self):
        print('hii i am working')
        self.ui.stackedWidget_2.setCurrentIndex((self.ui.stackedWidget_2.currentIndex() + 1) % 8)

    def previousWidget(self):
        print('hii i am also working')
        self.ui.stackedWidget_2.setCurrentIndex((self.ui.stackedWidget_2.currentIndex() - 1) % 8)
    
    # =============================================================================
    #   Update Menu's update checker and bug fixer menu
    # =============================================================================
    
    def updatechecker(self):
        SCOPES = ['https://www.googleapis.com/auth/documents']
        SERVICE_ACCOUNT_FILE = 'json/ms-boat-193407316d85.json'
        
        credential = None
        credential = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes =SCOPES)
        service = build('docs', 'v1', credentials=credential)
        
        def read_paragraph_element(element):
            """Returns the text in the given ParagraphElement.
        
                Args:
                    element: a ParagraphElement from a Google Doc.
            """
            text_run = element.get('textRun')
            if not text_run:
                return ''
            return text_run.get('content')
        
        
        def read_strucutural_elements(elements):
            """Recurses through a list of Structural Elements to read a document's text where text may be
                in nested elements.
        
                Args:
                    elements: a list of Structural Elements.
            """
            text = ''
            for value in elements:
                if 'paragraph' in value:
                    elements = value.get('paragraph').get('elements')
                    for elem in elements:
                        text += read_paragraph_element(elem)
                elif 'table' in value:
                    # The text in table cells are in nested Structural Elements and tables may be
                    # nested.
                    table = value.get('table')
                    for row in table.get('tableRows'):
                        cells = row.get('tableCells')
                        for cell in cells:
                            text += read_strucutural_elements(cell.get('content'))
                elif 'tableOfContents' in value:
                    # The text in the TOC is also in a Structural Element.
                    toc = value.get('tableOfContents')
                    text += read_strucutural_elements(toc.get('content'))
            return text
        
        def closeEvent(self):
            QMessageBox.about(self, 'Update notification!!', 'Update it for better experience?')

        #--------------------------------------------------------------------------------------------------------------------

        def upfuncation11():
            SAMPLE_DOCUMENTT_ID = ''
            document = service.documents().get(documentId=SAMPLE_DOCUMENTT_ID).execute()
            if document.get('title') == 'funcation11':
                closeEvent(self)
                doc_content = document.get('body').get('content')
                real_content = read_strucutural_elements(doc_content)
                print(real_content)
                with open('funcation1.py', 'w+') as codefile:
                    for i in (real_content):
                        codefile.write(i)
                print("i am update youe file sir")
                codefile.close()
                return True
            else:
                return False
        def upfuncation21():
            SAMPLE_DOCUMENTT_ID = ''
            document = service.documents().get(documentId=SAMPLE_DOCUMENTT_ID).execute()
            if document.get('title') == 'funcation21':
                closeEvent(self)
                doc_content = document.get('body').get('content')
                real_content = read_strucutural_elements(doc_content)
                print(real_content)
                with open('funcation2.py', 'w+') as codefile:
                    for i in (real_content):
                        codefile.write(i)
                print("i am update youe file sir")
                codefile.close()
                return True
            else:
                return False
        def upfuncation31():
            SAMPLE_DOCUMENTT_ID = ''
            document = service.documents().get(documentId=SAMPLE_DOCUMENTT_ID).execute()
            if document.get('title') == 'funcation31':
                closeEvent(self)
                doc_content = document.get('body').get('content')
                real_content = read_strucutural_elements(doc_content)
                print(real_content)
                with open('funcation3.py', 'w+') as codefile:
                    for i in (real_content):
                        codefile.write(i)
                print("i am update youe file sir")
                codefile.close()
                return True
            else:
                return False          
        def upfuncation41():
            SAMPLE_DOCUMENTT_ID = ''
            document = service.documents().get(documentId=SAMPLE_DOCUMENTT_ID).execute()
            if document.get('title') == 'funcation41':
                closeEvent(self)
                doc_content = document.get('body').get('content')
                real_content = read_strucutural_elements(doc_content)
                print(real_content)
                with open('funcation4.py', 'w+') as codefile:
                    for i in (real_content):
                        codefile.write(i)
                print("i am update youe file sir")
                codefile.close()
                return True
            else:
                return False
        def upfuncation51():
            SAMPLE_DOCUMENTT_ID = ''
            document = service.documents().get(documentId=SAMPLE_DOCUMENTT_ID).execute()
            if document.get('title') == 'funcation51':
                closeEvent(self)
                doc_content = document.get('body').get('content')
                real_content = read_strucutural_elements(doc_content)
                print(real_content)
                with open('funcation5.py', 'w+') as codefile:
                    for i in (real_content):
                        codefile.write(i)
                print("i am update youe file sir")
                codefile.close()
                return True
            else:
                return False
        def upfuncation61():
            # print("evet")
            SAMPLE_DOCUMENTT_ID = ''
            document = service.documents().get(documentId=SAMPLE_DOCUMENTT_ID).execute()
            if document.get('title') == 'funcation61':
                closeEvent(self)
                doc_content = document.get('body').get('content')
                real_content = read_strucutural_elements(doc_content)
                print(real_content)
                with open('funcation6.py', 'w+') as codefile:
                    for i in (real_content):
                        codefile.write(i)
                print("i am update youe file sir")
                codefile.close()
                return True
            else:
                return False
        def upfuncation71():
            # print("evet")
            SAMPLE_DOCUMENTT_ID = ''
            document = service.documents().get(documentId=SAMPLE_DOCUMENTT_ID).execute()
            if document.get('title') == 'funcation71':
                closeEvent(self)
                doc_content = document.get('body').get('content')
                real_content = read_strucutural_elements(doc_content)
                print(real_content)
                with open('funcation7.py', 'w+') as codefile:
                    for i in (real_content):
                        codefile.write(i)
                print("i am update youe file sir")
                codefile.close()
                return True
            else:
                return False
        def upfuncationmain1():
            # print("evet")
            SAMPLE_DOCUMENTT_ID = ''
            document = service.documents().get(documentId=SAMPLE_DOCUMENTT_ID).execute()
            if document.get('title') == 'main1':
                closeEvent(self)
                doc_content = document.get('body').get('content')
                real_content = read_strucutural_elements(doc_content)
                print(real_content)
                with open('main.py', 'w+') as codefile:
                    for i in (real_content):
                        codefile.write(i)
                print("i am update youe file sir")
                codefile.close()
                return True
            else:
                return False
        def upfuncationui1():
            # print("evet")
            SAMPLE_DOCUMENTT_ID = ''
            document = service.documents().get(documentId=SAMPLE_DOCUMENTT_ID).execute()
            if document.get('title') == 'main_ui1':
                closeEvent(self)
                doc_content = document.get('body').get('content')
                real_content = read_strucutural_elements(doc_content)
                print(real_content)
                with open('ui_main.py', 'w+') as codefile:
                    for i in (real_content):
                        codefile.write(i)
                print("i am update youe file sir")
                codefile.close()
                return True
            else:
                return False
        if upfuncation11() or upfuncation21() or upfuncation31() or upfuncation41() or upfuncation51() or upfuncation61() or upfuncation71() or upfuncationmain1() or upfuncationui1() == True:
            self.ui.textEdit_4.setText("APP UPDATED SUCESSFULLY")
        
        return True

# =============================================================================
# Main funcation
# =============================================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    TryIcon = QSystemTrayIcon(QIcon('image/profile.ico'))
    TryIcon.setToolTip("BOT")
    TryIcon.show()
    
    # menu = QMenu()
    # exitAction = menu.addAction('Exit')
    # exitAction.triggered.connect(app.quit)
    
    # TryIcon.setContextMenu(menu)
    

    sys.exit(app.exec_())


