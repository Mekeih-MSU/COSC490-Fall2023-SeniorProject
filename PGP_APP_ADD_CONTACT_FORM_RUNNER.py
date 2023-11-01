import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import PGP_APP_ADD_CONTACT_FORM
import PGP_APP_ALGO

class ContactPage(QtWidgets.QMainWindow, PGP_APP_ADD_CONTACT_FORM.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ContactPage, self).__init__(parent)
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

        # Contact Keys Page Button
        self.add_contact_btn.clicked.connect(lambda: self.add_contact())

        self.show()
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def add_contact(self):
        first_name = self.first_name_line_edit.text()
        last_name = self.last_name_line_edit.text()
        phone_number = self.phone_number_line_edit.text()
        email = self.email_line_edit.text()
        pub_key = self.public_key_line_edit.text()

        if first_name and last_name and phone_number and email and pub_key:
            PGP_APP_ALGO.add_contact_key(
                first_name,
                last_name,
                phone_number,
                email,
                pub_key)
            
            self.first_name_line_edit.clear()
            self.last_name_line_edit.clear()
            self.phone_number_line_edit.clear()
            self.email_line_edit.clear()
            self.public_key_line_edit.clear()

def main():
    app = QApplication(sys.argv)
    form = ContactPage()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
