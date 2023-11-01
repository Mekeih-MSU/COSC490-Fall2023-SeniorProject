import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import PGP_APP_GUI
import PGP_APP_ADD_CONTACT_FORM_RUNNER
import PGP_APP_ADD_KEY_FORM_RUNNER
import PGP_APP_ALGO
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class PGPApp(QtWidgets.QMainWindow, PGP_APP_GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PGPApp, self).__init__(parent)
        self.setupUi(self)

		# Minimize Button
        self.minimize_btn.clicked.connect(lambda: self.showMinimized())

		# Close Button
        self.close_btn.clicked.connect(lambda: self.close())

		# Remove Default Window Box
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Set Drop Shadow Window
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 200))

        # Apply Drop Shadow to Frame
        self.drop_window_frame.setGraphicsEffect(self.shadow)

		# Move Window Function
        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() -self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow
        
        # Personal Keys Page Button
        self.personal_btn_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.personal_key_page))
        self.add_key_btn.clicked.connect(lambda: PGP_APP_ADD_KEY_FORM_RUNNER.KeyPage())
        self.remove_personal_key_btn.clicked.connect(lambda: self.deleteKeyClicked())
        self.loadKeyPage()
        self.start_key_file_monitoring()

        # Contact Keys Page Button
        self.contacts_btn_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.contact_key_page))
        self.add_contact_btn.clicked.connect(lambda: PGP_APP_ADD_CONTACT_FORM_RUNNER.ContactPage())
        self.remove_contact_btn.clicked.connect(lambda: self.deleteContactClicked())
        self.loadContactPage()
        self.start_contact_file_monitoring()

        self.show()
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def loadContactPage(self):
        data = PGP_APP_ALGO.load_data("CONTACTS_KEYS.pkl")
        row = 0
        self.contact_table.setRowCount(len(data))

        for entry in data:
            self.contact_table.setItem(row, 0, QtWidgets.QTableWidgetItem(entry["First Name"]))
            self.contact_table.setItem(row, 1, QtWidgets.QTableWidgetItem(entry["Last Name"]))
            self.contact_table.setItem(row, 2, QtWidgets.QTableWidgetItem(entry["Phone Number"]))
            self.contact_table.setItem(row, 3, QtWidgets.QTableWidgetItem(entry["Email"]))
            self.contact_table.setItem(row, 4, QtWidgets.QTableWidgetItem(entry["Public Key"]))
            row += 1
    
    def deleteContactClicked(self):
        selected_row = self.contact_table.currentRow()
        if selected_row >= 0:
            print(selected_row)
            PGP_APP_ALGO.delete_entry(selected_row, "CONTACTS_KEYS.pkl")
    
    def update_contact_page_on_modified(self, event):
        self.loadContactPage()

    def start_contact_file_monitoring(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.update_contact_page_on_modified

        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=False)
        observer.start()
    
    def loadKeyPage(self):
        data = PGP_APP_ALGO.load_data("PERSONAL_KEYS.pkl")
        row = 0
        self.personal_key_table.setRowCount(len(data))
        for entry in data:
            self.personal_key_table.setItem(row, 0, QtWidgets.QTableWidgetItem(entry["Name"]))
            self.personal_key_table.setItem(row, 1, QtWidgets.QTableWidgetItem(entry["Public Key"]))
            self.personal_key_table.setItem(row, 2, QtWidgets.QTableWidgetItem(entry["Private Key"]))
            row += 1
    
    def deleteKeyClicked(self):
        selected_row = self.personal_key_table.currentRow()
        if selected_row >= 0:
            print(selected_row)
            PGP_APP_ALGO.delete_entry(selected_row, "PERSONAL_KEYS.pkl")
    
    def update_key_page_on_modified(self, event):
        self.loadKeyPage()

    def start_key_file_monitoring(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.update_key_page_on_modified

        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=False)
        observer.start()

def main():
    app = QApplication(sys.argv)
    form = PGPApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
