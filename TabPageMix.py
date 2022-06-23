# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget



class TabPageMix(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tab_Mix = QtWidgets.QWidget()
        self.tab_Mix.setObjectName("tab_Mix")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_Mix)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_Mix)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.plainTextEdit_Mix_in = QtWidgets.QPlainTextEdit(self.groupBox_7)
        self.plainTextEdit_Mix_in.setObjectName("plainTextEdit_Mix_in")
        self.plainTextEdit_Mix_in.setStyleSheet(
            "background-color: rgb(240, 240, 240);")
        self.plainTextEdit_Mix_in.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Mix_in.setReadOnly(True)
        self.verticalLayout_11.addWidget(self.plainTextEdit_Mix_in)
        self.verticalLayout_12.addWidget(self.groupBox_7)
        parent.tabWidget_2.addTab(self.tab_Mix, "")

        self.retranslateUi(parent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_7.setTitle(_translate(
            "MainWindow", "Properties - non-reacted Mixture"))
        MainWindow.tabWidget_2.setTabText(MainWindow.tabWidget_2.indexOf(
            self.tab_Mix), _translate("MainWindow", "Mixture"))
