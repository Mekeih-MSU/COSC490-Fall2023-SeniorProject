import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import PGP_APP_ADD_KEY_FORM
import PGP_APP_ALGO

class KeyPage(QtWidgets.QMainWindow, PGP_APP_ADD_KEY_FORM.Ui_MainWindow):
    def __init__(self, parent=None):
        super(KeyPage, self).__init__(parent)
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
        self.add_key_btn.clicked.connect(lambda: self.add_personal_key())

        self.show()
    
    def add_personal_key(self):
        name = self.name_line_edit.text()
        if name:
            PGP_APP_ALGO.add_personal_key(name)
            self.name_line_edit.clear()

    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

def main():
    app = QApplication(sys.argv)
    form = KeyPage()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
