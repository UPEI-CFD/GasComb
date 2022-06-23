# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QWidget




class TabPageStream(QWidget):
    """
    Stream Tab Page
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_T_in = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_T_in.setReadOnly(False)
        self.lineEdit_T_in.setObjectName("lineEdit_T_in")
        self.lineEdit_T_in.setText("0")
        # self.lineEdit_T_in.setValidator(QtGui.QDoubleValidator(self))
        self.gridLayout.addWidget(self.lineEdit_T_in, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.comboBoxFlow1 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBoxFlow1.setMinimumContentsLength(10)
        self.comboBoxFlow1.setObjectName("comboBoxFlow1")
        self.comboBoxFlow1.addItem("")
        self.comboBoxFlow1.addItem("")
        self.gridLayout.addWidget(self.comboBoxFlow1, 1, 0, 1, 1)
        self.lineEdit_Flow_in = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_Flow_in.setReadOnly(False)
        self.lineEdit_Flow_in.setObjectName("lineEdit_Flow_in")
        self.lineEdit_Flow_in.setText("0")
        self.gridLayout.addWidget(self.lineEdit_Flow_in, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.lineEdit_P_in = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_P_in.setReadOnly(False)
        self.lineEdit_P_in.setObjectName("lineEdit_P_in")
        self.lineEdit_P_in.setText("101325")
        self.gridLayout.addWidget(self.lineEdit_P_in, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)
        self.lineEdit_RH_in = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_RH_in.setReadOnly(False)
        self.lineEdit_RH_in.setObjectName("lineEdit_RH_in")
        self.lineEdit_RH_in.setText("0")
        self.gridLayout.addWidget(self.lineEdit_RH_in, 3, 2, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonSetAir = QtWidgets.QPushButton(self.tab)
        self.pushButtonSetAir.setObjectName("pushButtonSetAir")
        self.horizontalLayout_3.addWidget(self.pushButtonSetAir)
        self.pushButtonSetNG = QtWidgets.QPushButton(self.tab)
        self.pushButtonSetNG.setObjectName("pushButtonSetNG")
        self.horizontalLayout_3.addWidget(self.pushButtonSetNG)
        self.pushButtonSpecies = QtWidgets.QPushButton(self.tab)
        self.pushButtonSpecies.setObjectName("pushButtonSpecies")
        self.horizontalLayout_3.addWidget(self.pushButtonSpecies)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.checkBox_VolFr_in = QtWidgets.QCheckBox(self.tab)
        self.checkBox_VolFr_in.setChecked(True)
        self.checkBox_VolFr_in.setObjectName("checkBox_VolFr_in")
        self.verticalLayout_9.addWidget(self.checkBox_VolFr_in)
        self.tableWidget_In1 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_In1.setObjectName("tableWidget_In1")
        self.tableWidget_In1.setColumnCount(2)
        self.tableWidget_In1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_In1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_In1.setHorizontalHeaderItem(1, item)
        self.verticalLayout_9.addWidget(self.tableWidget_In1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.plainTextEdit_Stream1_out = QtWidgets.QPlainTextEdit(
            self.groupBox)
        self.plainTextEdit_Stream1_out.setStyleSheet(
            "background-color: rgb(240, 240, 240);")
        self.plainTextEdit_Stream1_out.setReadOnly(True)
        self.plainTextEdit_Stream1_out.setObjectName(
            "plainTextEdit_Stream1_out")
        self.verticalLayout_10.addWidget(self.plainTextEdit_Stream1_out)
        self.verticalLayout_9.addWidget(self.groupBox)
        parent.tabWidget_2.addTab(self.tab, "xx")
        
        validator1 = QtGui.QRegExpValidator(QtCore.QRegExp(r'[+-]?(\d+([.]\d*)?([eE][+-]?\d+)?|[.]\d+([eE][+-]?\d+)?)'))
        self.lineEdit_T_in.setValidator(validator1)
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'[+]?(\d+([.]\d*)?([eE][+-]?\d+)?|[.]\d+([eE][+-]?\d+)?)'))
        self.lineEdit_Flow_in.setValidator(validator)
        self.lineEdit_P_in.setValidator(validator)
        self.lineEdit_RH_in.setValidator(validator)

        self.pushButtonSpecies.clicked.connect(self.speciesButtonClicked)
        self.pushButtonSetAir.clicked.connect(self.airButtonClicked)
        self.pushButtonSetNG.clicked.connect(self.NGButtonClicked)

        self.retranslateUi(parent)

    def speciesButtonClicked(self):
        # print(self.parent.comboBoxMechFile.currentText())
        dialog = UI_SpeDlg(
            self.parent.comboBoxMechFile.currentText(), self.parent)
        dialog.exec()

    def airButtonClicked(self):
        # Clear old rows
        self.tableWidget_In1.setRowCount(0)
        spe_sel = {'O2': 0.2095, 'N2': 0.7809,
                   'Ar': 0.0093, 'CO2': 0.0003, 'H2O': 0}
        # Put species to table in Main Window
        self.tableWidget_In1.setRowCount(len(spe_sel))
        print("Row count:", len(spe_sel)+1)
        for i, (k, v) in enumerate(spe_sel.items()):
            self.tableWidget_In1.setItem(i, 0, QTableWidgetItem(k))
            self.tableWidget_In1.setItem(i, 1, QTableWidgetItem(str(v)))

    def NGButtonClicked(self):
        # Clear old rows
        self.tableWidget_In1.setRowCount(0)
        spe_sel = {'CH4': 1}
        # Put species to table in Main Window
        self.tableWidget_In1.setRowCount(len(spe_sel))
        print("Row count:", len(spe_sel)+1)
        for i, (k, v) in enumerate(spe_sel.items()):
            self.tableWidget_In1.setItem(i, 0, QTableWidgetItem(k))
            self.tableWidget_In1.setItem(i, 1, QTableWidgetItem(str(v)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Inputs"))
        self.comboBoxFlow1.setItemText(0, _translate(
            "MainWindow", "Mass Flow Rate [kg/s]"))
        self.comboBoxFlow1.setItemText(1, _translate(
            "MainWindow", "Vol. Flow Rate [Nm3/h]"))
        self.label_10.setText(_translate("MainWindow", "Temperature [°C]"))
        self.label_13.setText(_translate("MainWindow", "Pressure [Pa]"))
        self.lineEdit_P_in.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>Absolute pressure.</p></body></html>"))
        self.label_14.setText(_translate(
            "MainWindow", "Relative Humidity [%]"))
        self.lineEdit_RH_in.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>If more than 0 -&gt; uit will overwrite dry species concentrations and add water vapour concentration.</p></body></html>"))
        self.pushButtonSetAir.setText(_translate("MainWindow", "Air"))
        self.pushButtonSetNG.setText(_translate("MainWindow", "Natural Gas"))
        self.pushButtonSpecies.setText(
            _translate("MainWindow", "Choose Species"))
        self.checkBox_VolFr_in.setText(
            _translate("MainWindow", "Vol. Fraction"))
        item = self.tableWidget_In1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Species Name"))
        item = self.tableWidget_In1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vol. Fraction"))
        ti = str(MainWindow.tabWidget_2.count())
        self.groupBox.setTitle(_translate(
            "MainWindow", "Properties - Stream"+ti))
        MainWindow.tabWidget_2.setTabText(MainWindow.tabWidget_2.indexOf(
            self.tab), _translate("MainWindow", "Stream"+ti))
