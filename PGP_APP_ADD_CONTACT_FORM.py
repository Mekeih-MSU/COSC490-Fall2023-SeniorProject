from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_window_frame = QFrame(self.centralwidget)
        self.drop_window_frame.setObjectName(u"drop_window_frame")
        self.drop_window_frame.setGeometry(QRect(0, 0, 600, 600))
        self.drop_window_frame.setMinimumSize(QSize(600, 300))
        self.drop_window_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 63, 255), stop:1 rgba(0, 0, 107, 255));\n"
"border-radius: 10px;")
        self.drop_window_frame.setFrameShape(QFrame.NoFrame)
        self.drop_window_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_window_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_window_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.title_bar.setFont(font)
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(self.title_bar)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(14)
        self.title_frame.setFont(font1)
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.title_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.title_label)


        self.horizontalLayout.addWidget(self.title_frame)

        self.btns_frame = QFrame(self.title_bar)
        self.btns_frame.setObjectName(u"btns_frame")
        self.btns_frame.setMaximumSize(QSize(70, 16777215))
        self.btns_frame.setFrameShape(QFrame.StyledPanel)
        self.btns_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.btns_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minimize_btn = QPushButton(self.btns_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(17, 17))
        self.minimize_btn.setMaximumSize(QSize(17, 17))
        self.minimize_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.btns_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(17, 17))
        self.close_btn.setMaximumSize(QSize(17, 17))
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.horizontalLayout.addWidget(self.btns_frame)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_window_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.first_name_label = QLabel(self.content_bar)
        self.first_name_label.setObjectName(u"first_name_label")
        self.first_name_label.setMinimumSize(QSize(30, 0))
        self.first_name_label.setMaximumSize(QSize(100, 20))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.first_name_label.setFont(font2)
        self.first_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.first_name_label, 0, Qt.AlignHCenter)

        self.first_name_line_edit = QLineEdit(self.content_bar)
        self.first_name_line_edit.setObjectName(u"first_name_line_edit")
        self.first_name_line_edit.setMinimumSize(QSize(400, 25))
        self.first_name_line_edit.setMaximumSize(QSize(400, 25))

        self.verticalLayout_4.addWidget(self.first_name_line_edit, 0, Qt.AlignHCenter)

        self.last_name_label = QLabel(self.content_bar)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setMinimumSize(QSize(30, 0))
        self.last_name_label.setMaximumSize(QSize(100, 20))
        self.last_name_label.setFont(font2)
        self.last_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.last_name_label, 0, Qt.AlignHCenter)

        self.last_name_line_edit = QLineEdit(self.content_bar)
        self.last_name_line_edit.setObjectName(u"last_name_line_edit")
        self.last_name_line_edit.setMinimumSize(QSize(400, 25))
        self.last_name_line_edit.setMaximumSize(QSize(400, 25))

        self.verticalLayout_4.addWidget(self.last_name_line_edit, 0, Qt.AlignHCenter)

        self.phone_number_label = QLabel(self.content_bar)
        self.phone_number_label.setObjectName(u"phone_number_label")
        self.phone_number_label.setMinimumSize(QSize(30, 0))
        self.phone_number_label.setMaximumSize(QSize(100, 20))
        self.phone_number_label.setFont(font2)
        self.phone_number_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.phone_number_label, 0, Qt.AlignHCenter)

        self.phone_number_line_edit = QLineEdit(self.content_bar)
        self.phone_number_line_edit.setObjectName(u"phone_number_line_edit")
        self.phone_number_line_edit.setMinimumSize(QSize(400, 25))
        self.phone_number_line_edit.setMaximumSize(QSize(400, 25))

        self.verticalLayout_4.addWidget(self.phone_number_line_edit, 0, Qt.AlignHCenter)

        self.email_label = QLabel(self.content_bar)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMinimumSize(QSize(30, 0))
        self.email_label.setMaximumSize(QSize(100, 20))
        self.email_label.setFont(font2)
        self.email_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.email_label, 0, Qt.AlignHCenter)

        self.email_line_edit = QLineEdit(self.content_bar)
        self.email_line_edit.setObjectName(u"email_line_edit")
        self.email_line_edit.setMinimumSize(QSize(400, 25))
        self.email_line_edit.setMaximumSize(QSize(400, 25))

        self.verticalLayout_4.addWidget(self.email_line_edit, 0, Qt.AlignHCenter)

        self.public_key_label = QLabel(self.content_bar)
        self.public_key_label.setObjectName(u"public_key_label")
        self.public_key_label.setMinimumSize(QSize(30, 0))
        self.public_key_label.setMaximumSize(QSize(100, 20))
        self.public_key_label.setFont(font2)
        self.public_key_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.public_key_label, 0, Qt.AlignHCenter)

        self.public_key_line_edit = QLineEdit(self.content_bar)
        self.public_key_line_edit.setObjectName(u"public_key_line_edit")
        self.public_key_line_edit.setMinimumSize(QSize(400, 25))
        self.public_key_line_edit.setMaximumSize(QSize(400, 100))

        self.verticalLayout_4.addWidget(self.public_key_line_edit, 0, Qt.AlignHCenter)

        self.add_contact_btn = QPushButton(self.content_bar)
        self.add_contact_btn.setObjectName(u"add_contact_btn")
        self.add_contact_btn.setEnabled(True)
        self.add_contact_btn.setMinimumSize(QSize(250, 60))
        self.add_contact_btn.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(8)
        self.add_contact_btn.setFont(font3)
        self.add_contact_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 100), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	padding-top: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 180), stop:1 rgba(255, 255, 255, 255));\n"
"}")

        self.verticalLayout_4.addWidget(self.add_contact_btn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_window_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: none;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.credits_label_frame = QFrame(self.credits_bar)
        self.credits_label_frame.setObjectName(u"credits_label_frame")
        self.credits_label_frame.setFrameShape(QFrame.StyledPanel)
        self.credits_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.credits_label_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.credits_label = QLabel(self.credits_label_frame)
        self.credits_label.setObjectName(u"credits_label")
        self.credits_label.setStyleSheet(u"color: rgb(129, 129, 129);")

        self.verticalLayout_3.addWidget(self.credits_label)


        self.horizontalLayout_3.addWidget(self.credits_label_frame)

        self.grip_label_frame = QFrame(self.credits_bar)
        self.grip_label_frame.setObjectName(u"grip_label_frame")
        self.grip_label_frame.setMinimumSize(QSize(30, 30))
        self.grip_label_frame.setMaximumSize(QSize(30, 30))
        self.grip_label_frame.setStyleSheet(u"padding: 5px;")
        self.grip_label_frame.setFrameShape(QFrame.StyledPanel)
        self.grip_label_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.grip_label_frame)


        self.verticalLayout.addWidget(self.credits_bar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"PGP APP", None))
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.first_name_label.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.last_name_label.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.phone_number_label.setText(QCoreApplication.translate("MainWindow", u"Phone #:", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"email:", None))
        self.public_key_label.setText(QCoreApplication.translate("MainWindow", u"Public Key:", None))
        self.add_contact_btn.setText(QCoreApplication.translate("MainWindow", u"ADD CONTACT", None))
        self.credits_label.setText(QCoreApplication.translate("MainWindow", u"By: Mekeih Nelson, Gareth Nuyit, Darrius Outlaw, Kye Toussant", None))
    # retranslateUi

