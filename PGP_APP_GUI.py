from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(953, 891)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_window_frame = QFrame(self.centralwidget)
        self.drop_window_frame.setObjectName(u"drop_window_frame")
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
        self.horizontalLayout_4 = QHBoxLayout(self.content_bar)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.crypto_btn_frame = QFrame(self.content_bar)
        self.crypto_btn_frame.setObjectName(u"crypto_btn_frame")
        self.crypto_btn_frame.setMinimumSize(QSize(70, 0))
        self.crypto_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.crypto_btn_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.crypto_btn_frame)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.encrypt_btn = QPushButton(self.crypto_btn_frame)
        self.encrypt_btn.setObjectName(u"encrypt_btn")
        self.encrypt_btn.setMinimumSize(QSize(40, 100))
        self.encrypt_btn.setMaximumSize(QSize(16777215, 16777215))
        self.encrypt_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 100), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	padding-top: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 180), stop:1 rgba(255, 255, 255, 255));\n"
"}")

        self.verticalLayout_5.addWidget(self.encrypt_btn)

        self.decrypt_btn = QPushButton(self.crypto_btn_frame)
        self.decrypt_btn.setObjectName(u"decrypt_btn")
        self.decrypt_btn.setMinimumSize(QSize(40, 100))
        self.decrypt_btn.setMaximumSize(QSize(16777215, 16777215))
        self.decrypt_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 100), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	padding-top: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 180), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.decrypt_btn)


        self.horizontalLayout_4.addWidget(self.crypto_btn_frame, 0, Qt.AlignTop)

        self.key_collection_frame = QFrame(self.content_bar)
        self.key_collection_frame.setObjectName(u"key_collection_frame")
        self.key_collection_frame.setFrameShape(QFrame.StyledPanel)
        self.key_collection_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.key_collection_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.key_btn_collection_frame = QFrame(self.key_collection_frame)
        self.key_btn_collection_frame.setObjectName(u"key_btn_collection_frame")
        self.key_btn_collection_frame.setMinimumSize(QSize(0, 50))
        self.key_btn_collection_frame.setFrameShape(QFrame.StyledPanel)
        self.key_btn_collection_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.key_btn_collection_frame)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.personal_btn_page = QPushButton(self.key_btn_collection_frame)
        self.personal_btn_page.setObjectName(u"personal_btn_page")
        self.personal_btn_page.setMinimumSize(QSize(100, 40))
        self.personal_btn_page.setMaximumSize(QSize(100, 100))
        self.personal_btn_page.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 100), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	padding-top: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 180), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 200), stop:1 rgba(255, 255, 255, 255));\n"
"}")

        self.horizontalLayout_5.addWidget(self.personal_btn_page)

        self.contacts_btn_page = QPushButton(self.key_btn_collection_frame)
        self.contacts_btn_page.setObjectName(u"contacts_btn_page")
        self.contacts_btn_page.setMinimumSize(QSize(100, 40))
        self.contacts_btn_page.setMaximumSize(QSize(100, 100))
        self.contacts_btn_page.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 100), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	padding-top: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 180), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 200), stop:1 rgba(255, 255, 255, 255));\n"
"}")

        self.horizontalLayout_5.addWidget(self.contacts_btn_page)


        self.verticalLayout_4.addWidget(self.key_btn_collection_frame, 0, Qt.AlignLeft)

        self.stackedWidget = QStackedWidget(self.key_collection_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.personal_key_page = QWidget()
        self.personal_key_page.setObjectName(u"personal_key_page")
        self.verticalLayout_6 = QVBoxLayout(self.personal_key_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.personal_key_table = QTableWidget(self.personal_key_page)
        if (self.personal_key_table.columnCount() < 4):
            self.personal_key_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.personal_key_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.personal_key_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.personal_key_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.personal_key_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.personal_key_table.setObjectName(u"personal_key_table")
        self.personal_key_table.setStyleSheet(u"QTableWidget::item {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #ADD8E6;\n"
"}")

        self.verticalLayout_6.addWidget(self.personal_key_table)

        self.personal_key_table_btn_frame = QFrame(self.personal_key_page)
        self.personal_key_table_btn_frame.setObjectName(u"personal_key_table_btn_frame")
        self.personal_key_table_btn_frame.setMinimumSize(QSize(0, 60))
        self.personal_key_table_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.personal_key_table_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.personal_key_table_btn_frame)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.add_key_btn = QPushButton(self.personal_key_table_btn_frame)
        self.add_key_btn.setObjectName(u"add_key_btn")
        self.add_key_btn.setMinimumSize(QSize(250, 60))
        self.add_key_btn.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        self.add_key_btn.setFont(font2)
        self.add_key_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 100), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	padding-top: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 180), stop:1 rgba(255, 255, 255, 255));\n"
"}")

        self.horizontalLayout_7.addWidget(self.add_key_btn)

        self.remove_personal_key_btn = QPushButton(self.personal_key_table_btn_frame)
        self.remove_personal_key_btn.setObjectName(u"remove_personal_key_btn")
        self.remove_personal_key_btn.setMinimumSize(QSize(0, 60))
        self.remove_personal_key_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 100), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	padding-top: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 180), stop:1 rgba(255, 255, 255, 255));\n"
"}")

        self.horizontalLayout_7.addWidget(self.remove_personal_key_btn)


        self.verticalLayout_6.addWidget(self.personal_key_table_btn_frame)

        self.stackedWidget.addWidget(self.personal_key_page)
        self.contact_key_page = QWidget()
        self.contact_key_page.setObjectName(u"contact_key_page")
        self.contact_key_page.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.verticalLayout_7 = QVBoxLayout(self.contact_key_page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contact_table = QTableWidget(self.contact_key_page)
        if (self.contact_table.columnCount() < 6):
            self.contact_table.setColumnCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.contact_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.contact_table.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.contact_table.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.contact_table.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.contact_table.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.contact_table.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        self.contact_table.setObjectName(u"contact_table")
        self.contact_table.setStyleSheet(u"QTableWidget::item {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #ADD8E6;\n"
"}")

        self.verticalLayout_7.addWidget(self.contact_table)

        self.contact_table_btn_frame = QFrame(self.contact_key_page)
        self.contact_table_btn_frame.setObjectName(u"contact_table_btn_frame")
        self.contact_table_btn_frame.setMinimumSize(QSize(0, 60))
        self.contact_table_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_table_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.contact_table_btn_frame)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.add_contact_btn = QPushButton(self.contact_table_btn_frame)
        self.add_contact_btn.setObjectName(u"add_contact_btn")
        self.add_contact_btn.setMinimumSize(QSize(250, 60))
        self.add_contact_btn.setMaximumSize(QSize(16777215, 16777215))
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

        self.horizontalLayout_6.addWidget(self.add_contact_btn)

        self.remove_contact_btn = QPushButton(self.contact_table_btn_frame)
        self.remove_contact_btn.setObjectName(u"remove_contact_btn")
        self.remove_contact_btn.setMinimumSize(QSize(250, 60))
        self.remove_contact_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 100), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	padding-top: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(185, 185, 185, 180), stop:1 rgba(255, 255, 255, 255));\n"
"}")

        self.horizontalLayout_6.addWidget(self.remove_contact_btn)


        self.verticalLayout_7.addWidget(self.contact_table_btn_frame)

        self.stackedWidget.addWidget(self.contact_key_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.key_collection_frame)


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


        self.drop_shadow_layout.addWidget(self.drop_window_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"PGP APP", None))
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.encrypt_btn.setText(QCoreApplication.translate("MainWindow", u"ENCRYPT", None))
        self.decrypt_btn.setText(QCoreApplication.translate("MainWindow", u"DECRYPT", None))
        self.personal_btn_page.setText(QCoreApplication.translate("MainWindow", u"KEYS", None))
        self.contacts_btn_page.setText(QCoreApplication.translate("MainWindow", u"CONTACTS", None))
        ___qtablewidgetitem = self.personal_key_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.personal_key_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Public Key", None));
        ___qtablewidgetitem2 = self.personal_key_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Private Key", None));
        ___qtablewidgetitem3 = self.personal_key_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Fingerprint", None));
        self.add_key_btn.setText(QCoreApplication.translate("MainWindow", u"ADD KEY", None))
        self.remove_personal_key_btn.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        ___qtablewidgetitem4 = self.contact_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem5 = self.contact_table.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem6 = self.contact_table.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Phone #", None));
        ___qtablewidgetitem7 = self.contact_table.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem8 = self.contact_table.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Public Key", None));
        ___qtablewidgetitem9 = self.contact_table.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Fingerprint", None));
        self.add_contact_btn.setText(QCoreApplication.translate("MainWindow", u"ADD CONTACT", None))
        self.remove_contact_btn.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.credits_label.setText(QCoreApplication.translate("MainWindow", u"By: Mekeih Nelson, Gareth Nuyit, Darrius Outlaw, Kye Toussant", None))
    # retranslateUi

