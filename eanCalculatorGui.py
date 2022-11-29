# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eanCalculatorGui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(266, 122)
        MainWindow.setFocusPolicy(Qt.ClickFocus)
        icon = QIcon()
        icon.addFile(u"../../Desktop/verify.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"* {\n"
"	background: #e1e1e6\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton{\n"
"	background-color: #56a4fd;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #5ecbf1;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background: #ffffff\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.ean_label = QLabel(self.frame)
        self.ean_label.setObjectName(u"ean_label")
        self.ean_label.setGeometry(QRect(10, 10, 35, 20))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.ean_label.setFont(font)
        self.ean_label.setScaledContents(False)
        self.ean_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.validation_label = QLabel(self.frame)
        self.validation_label.setObjectName(u"validation_label")
        self.validation_label.setGeometry(QRect(10, 38, 70, 20))
        self.validation_label.setFont(font)
        self.ean_receiver = QLineEdit(self.frame)
        self.ean_receiver.setObjectName(u"ean_receiver")
        self.ean_receiver.setGeometry(QRect(91, 10, 116, 22))
        self.ean_checker = QLineEdit(self.frame)
        self.ean_checker.setObjectName(u"ean_checker")
        self.ean_checker.setGeometry(QRect(91, 38, 116, 22))
        self.validation_button = QPushButton(self.frame)
        self.validation_button.setObjectName(u"validation_button")
        self.validation_button.setGeometry(QRect(40, 70, 75, 24))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        self.validation_button.setFont(font1)
        self.validation_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_validation = QPushButton(self.frame)
        self.new_validation.setObjectName(u"new_validation")
        self.new_validation.setGeometry(QRect(140, 70, 75, 24))
        font2 = QFont()
        font2.setKerning(False)
        self.new_validation.setFont(font2)
        self.new_validation.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ean_label.setText(QCoreApplication.translate("MainWindow", u"EAN ", None))
        self.validation_label.setText(QCoreApplication.translate("MainWindow", u"Validador ", None))
        self.validation_button.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.new_validation.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
    # retranslateUi

