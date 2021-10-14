# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 373)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 110, 81, 72))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_1 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout.addWidget(self.radioButton_4)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 220, 75, 23))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 260, 75, 23))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(170, 110, 181, 171))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioButton_1.setText(QCoreApplication.translate("MainWindow", u"Freq band 1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Freq band 2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Freq band 3", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Freq band 4", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Zablokuje okno", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Nezablokuje okno", None))
    # retranslateUi

