import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import PGP_APP_GUI

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

		# Move Window Function
        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() -self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow
        
        # Personal Keys Page Button
        self.personal_btn_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.personal_key_page))

        # Contact Keys Page Button
        self.contacts_btn_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.contact_key_page))

        self.show()
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

def main():
    app = QApplication(sys.argv)
    form = PGPApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()