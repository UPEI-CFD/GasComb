# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QWidget

from SpalGas import Ui_MainWindow
from SpecieseDialog import Ui_SpeciesDialog
import pySpal
from scipy.optimize import minimize_scalar
import copy


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Set list of mechanism files for combo box
        mechs = pySpal.getMechanisms()
        self.comboBoxMechFile.addItems(mechs)
        self.comboBoxMechFile.setCurrentIndex(mechs.index("gri30.yaml"))
        self.spe_sel = []

        self.connectSignalsSlots()

        # self.tabs = self.tabWidget_2
        button = QtWidgets.QToolButton()
        button.setToolTip('Add New Tab')
        button.clicked.connect(self.addNewTab)
        button.setIcon(self.style().standardIcon(
            QtWidgets.QStyle.SP_DialogYesButton))
        self.tabWidget_2.setCornerWidget(button, QtCore.Qt.TopRightCorner)
        # self.addNewTab()   PE_IndicatorSpinPlus SP_DialogYesButton
        self.tabMix = None
        self.tabStream = [self]
        
        validator1 = QtGui.QRegExpValidator(QtCore.QRegExp(r'[+-]?(\d+([.]\d*)?([eE][+-]?\d+)?|[.]\d+([eE][+-]?\d+)?)'))
        self.lineEdit_T_in.setValidator(validator1)
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'[+]?(\d+([.]\d*)?([eE][+-]?\d+)?|[.]\d+([eE][+-]?\d+)?)'))
        self.lineEdit_2.setValidator(validator)
        self.lineEdit_3.setValidator(validator)
        self.lineEdit_Flow_in.setValidator(validator)
        self.lineEdit_P_in.setValidator(validator)
        self.lineEdit_RH_in.setValidator(validator)
        # self.lineEdit_3.setValidator(QtGui.QDoubleValidator(self))

    def connectSignalsSlots(self):
        
        self.actionAbout.triggered.connect(self.about)
        self.actionOpen.triggered.connect(self.getFile)
        self.actionSave.triggered.connect(self.saveSetup)
        self.actionSave_as.triggered.connect(self.saveSetup_as)

    def addNewTab(self):
        """
        Add new Stream tab.        
        """
        self.tabStream.append(TabPageStream(self))

    def notImplemented_Msg(self):
        QMessageBox.warning(self, "Warning", "Not yet implemented")

    def getFile(self):
        self.notImplemented_Msg()

        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '.\\', "Setup files (*.xml);;All files (*)")
        if fname[0] != "":
            print(fname)
        # self.le.setPixmap(QPixmap(fname))

    def saveSetup(self):
        self.notImplemented_Msg()

    def saveSetup_as(self):
        self.notImplemented_Msg()

        fname = QFileDialog.getSaveFileName(self, 'Save file as',
                                            '.\\', "Setup files (*.xml);;All files (*)")
        if fname[0] != "":
            print(fname)

    def about(self):
        QMessageBox.about(
            self,
            "About GasComb Application",
            pySpal.license_description,
        )

    def speciesButtonClicked(self):

        dialog = UI_SpeDlg(self.comboBoxMechFile.currentText(), self)
        dialog.exec()

    def airButtonClicked(self):
        # Clear old rows
        self.tableWidget_In1.setRowCount(0)
        spe_sel = {'O2': 0.2095, 'N2': 0.7809,
                   'Ar': 0.0093, 'CO2': 0.0003, 'H2O': 0}
        # Put species to table in Main Window
        self.tableWidget_In1.setRowCount(len(spe_sel))
        # print("Row count:", len(spe_sel)+1)
        for i, (k, v) in enumerate(spe_sel.items()):
            self.tableWidget_In1.setItem(i, 0, QTableWidgetItem(k))
            self.tableWidget_In1.setItem(i, 1, QTableWidgetItem(str(v)))

    def NGButtonClicked(self):
        # Clear old rows
        self.tableWidget_In1.setRowCount(0)
        spe_sel = {'CH4': 1}
        # Put species to table in Main Window
        self.tableWidget_In1.setRowCount(len(spe_sel))
        # print("Row count:", len(spe_sel)+1)
        for i, (k, v) in enumerate(spe_sel.items()):
            self.tableWidget_In1.setItem(i, 0, QTableWidgetItem(k))
            self.tableWidget_In1.setItem(i, 1, QTableWidgetItem(str(v)))

    def calculateButtonClicked(self):
        # self.notImplemented_Msg()
        spaliny = self.evalInButtonClicked()

        spaliny.equilibrate("HP")

        self.lineEdit_tepl.setText("{:.2f}".format(spaliny.T-273.15))
        self.lineEdit_mf.setText("{:.3f}".format(spaliny.mass))
        self.lineEdit_Vf.setText("{:.2f}".format(spaliny.mass/spaliny.density))
        self.lineEdit_density.setText("{:.4f}".format(spaliny.density))
        self.lineEdit_visc.setText("{:.4g}".format(spaliny.viscosity))
        self.lineEdit_cp.setText("{:.2f}".format(spaliny.cp))

        # Table Real
        self.tableWidget_Real.setRowCount(len(spaliny.X))
        for i, s in enumerate(zip(spaliny.species_names, spaliny.X, spaliny.Y)):
            # print(s[0],s[1])
            self.tableWidget_Real.setItem(i, 0, QTableWidgetItem(s[0]))
            self.tableWidget_Real.setItem(
                i, 1, QTableWidgetItem("{:.6f}".format(s[1])))
            self.tableWidget_Real.setItem(
                i, 2, QTableWidgetItem("{:.6f}".format(s[2])))
        self.tableWidget_Real.sortItems(1, QtCore.Qt.DescendingOrder)

        t, p = spaliny.TP
        spaliny.TP = 273.15, 101325
        self.lineEdit_VfN.setText("{:.2f}".format(spaliny.mass/spaliny.density))
        spaliny.TP = t, p

        # Table Dry
        pySpal.set_water_X(spaliny, 0)
        # print(spaliny.report())
        self.tableWidget_Dry.setRowCount(len(spaliny.X))
        for i, s in enumerate(zip(spaliny.species_names, spaliny.X, spaliny.Y)):
            # print(s[0], s[1])
            self.tableWidget_Dry.setItem(i, 0, QTableWidgetItem(s[0]))
            self.tableWidget_Dry.setItem(
                i, 1, QTableWidgetItem("{:.6f}".format(s[1])))
            self.tableWidget_Dry.setItem(
                i, 2, QTableWidgetItem("{:.6f}".format(s[2])))
        self.tableWidget_Dry.sortItems(1, QtCore.Qt.DescendingOrder)

        # Table Reference O2
        o2_ref = float(self.lineEdit_3.text())/100
        pySpal.set_O2_ref_X(spaliny, o2_ref)
        self.tableWidget_RefO2.setRowCount(len(spaliny.X))
        for i, s in enumerate(zip(spaliny.species_names, spaliny.X, spaliny.Y)):
            # print(s[0],s[1])
            self.tableWidget_RefO2.setItem(i, 0, QTableWidgetItem(s[0]))
            self.tableWidget_RefO2.setItem(
                i, 1, QTableWidgetItem("{:.6f}".format(s[1])))
            self.tableWidget_RefO2.setItem(
                i, 2, QTableWidgetItem("{:.6f}".format(s[2])))
        self.tableWidget_RefO2.sortItems(1, QtCore.Qt.DescendingOrder)

    def get_lmbd(self, streams, mass_ox):
        streams[0].mass = mass_ox
        Mix = copy.copy(streams[0])
        for s in streams[1:]:
            Mix += s
        return 1/Mix.equivalence_ratio()

    def lambdaButtonClicked(self):
        """
        Set 1/equivalence ratio -> Air-Fuel Ratio

        Returns
        -------
        None.

        """
        lmbd = self.lineEdit_2.text()
        try:
            lmbd = float(lmbd)
        except ValueError:
            QMessageBox.warning(
                self, "Error", "Wrong input. It has to be a number.")
            return
        QMessageBox.information(self, "Information", "Assumes that the first stream is \
oxydizer and other streams are fuels.")
        spaliny = ""
        streams = []
        mechFile = self.comboBoxMechFile.currentText()

        for t in self.tabStream:
            # print (t.lineEdit_T_in.text())
            t1 = float(t.lineEdit_T_in.text())+273.15
            mf1 = float(t.lineEdit_Flow_in.text())
            p1 = float(t.lineEdit_P_in.text())
            rh = float(t.lineEdit_RH_in.text())

            # Read data from table of species concetration
            tw = t.tableWidget_In1
            allRows = tw.rowCount()
            spe_conc = {}
            for row in range(allRows):
                spe_conc[tw.item(row, 0).text()] = float(
                    tw.item(row, 1).text())

            # Set the cantera object of the first gas stream
            # TODO Check if Multi option exists for other mechanism files
            gas1 = pySpal.ct.Solution(mechFile, transport_model='Multi')
            spaliny = pySpal.ct.Quantity(gas1, constant='HP')
            if t.checkBox_VolFr_in.isChecked() == True:
                spaliny.TPX = t1, p1, spe_conc
            else:
                spaliny.TPY = t1, p1, spe_conc

            if t.comboBoxFlow1.currentText() == "Mass Flow Rate [kg/s]":
                spaliny.mass = mf1
            else:
                spaliny.TP = 273.15, 101325
                dens = spaliny.density
                spaliny.mass = mf1*dens
                spaliny.TP = t1, p1

            rh = t.lineEdit_RH_in.text()
            if rh != "0":
                pySpal.set_water_phi(spaliny, float(rh)/100)

            t.plainTextEdit_Stream1_out.clear()
            t.plainTextEdit_Stream1_out.insertPlainText(spaliny.report())
            streams.append(copy.copy(spaliny))

        # Mix = streams[0]
        # for s in streams[1:]:
        #     Mix += s

        # lmbd_get = 1/Mix.equivalence_ratio()
        res = minimize_scalar(lambda mw: abs(self.get_lmbd(
            streams, mw)-lmbd), bounds=[0, 1e3], method="bounded")
        mw_out = res.x
        # print(res)

        t = self.tabStream[0]
        if t.comboBoxFlow1.currentText() == "Mass Flow Rate [kg/s]":
            t.lineEdit_Flow_in.setText(str(mw_out))
        else:
            streams[0].TP = 273.15, 101325
            dens = streams[0].density
            t.lineEdit_Flow_in.setText(str(mw_out/dens*3600))
            streams[0].TP = t1, p1

        

    def evalInButtonClicked(self):

        spaliny = ""
        streams = []

        # Get data from user's inputs
        mechFile = self.comboBoxMechFile.currentText()

        for t in self.tabStream:
            # print (t.lineEdit_T_in.text())
            t1 = float(t.lineEdit_T_in.text())+273.15
            mf1 = float(t.lineEdit_Flow_in.text())
            p1 = float(t.lineEdit_P_in.text())
            rh = float(t.lineEdit_RH_in.text())

            # Read data from table of species concetration
            tw = t.tableWidget_In1
            allRows = tw.rowCount()
            spe_conc = {}
            for row in range(allRows):
                spe_conc[tw.item(row, 0).text()] = float(
                    tw.item(row, 1).text())

            # Set the cantera object of the first gas stream
            # TODO Check if Multi option exists for other mechanism files
            gas1 = pySpal.ct.Solution(mechFile, transport_model='Multi')
            spaliny = pySpal.ct.Quantity(gas1, constant='HP')
            if t.checkBox_VolFr_in.isChecked() == True:
                spaliny.TPX = t1, p1, spe_conc
            else:
                spaliny.TPY = t1, p1, spe_conc

            if t.comboBoxFlow1.currentText() == "Mass Flow Rate [kg/s]":
                spaliny.mass = mf1
            else:
                spaliny.TP = 273.15, 101325
                dens = spaliny.density
                spaliny.mass = mf1*dens
                spaliny.TP = t1, p1

            rh = t.lineEdit_RH_in.text()
            if rh != "0":
                pySpal.set_water_phi(spaliny, float(rh)/100)

            t.plainTextEdit_Stream1_out.clear()
            t.plainTextEdit_Stream1_out.insertPlainText(spaliny.report())
            streams.append(spaliny)

        Mix = streams[0]
        for s in streams[1:]:
            Mix += s

        # Calculate Air to Fuel equivalence ratio (1/equivalence ratio)
        self.lineEdit_2.setText(str(1/Mix.equivalence_ratio()))

        # Create new tab with results from two streams
        if not self.tabMix:
            self.tabMix = TabPageMix(self)
        self.tabMix.plainTextEdit_Mix_in.clear()
        self.tabMix.plainTextEdit_Mix_in.insertPlainText(Mix.report())

        return Mix

    def chooseMechFileClicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '.\\', "Mechanism file (*.cti);;All files (*)")
        if fname[0] != "":
            print(fname)
        # TODO Control has to be added - when Mech file is changed Species list must be cleared or checked!!!!


class UI_SpeDlg(QDialog, Ui_SpeciesDialog):
    """Species choice dialog."""

    def __init__(self, fnm, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_SpeciesDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        spe_in = [n.name for n in pySpal.ct.Species.listFromFile(fnm)]
        self.ui.listWidget_all.addItems(spe_in)
        self.parent = parent
        
    def okButtonClickedSpeciesDial(self):
        
        # Clear old rows
        self.parent.tableWidget_In1.setRowCount(0)
        # Get selected species
        spe_sel = [str(self.ui.listWidget_select.item(i).text())
                   for i in range(self.ui.listWidget_select.count())]
        print("Row count:", len(spe_sel))
        
        self.parent.spe_sel = spe_sel
        # Put species to table in Main Window
        self.parent.tableWidget_In1.setRowCount(len(spe_sel))
        print("Row count:", len(spe_sel)+1)
        for i, s in enumerate(spe_sel):
            self.parent.tableWidget_In1.setItem(i, 0, QTableWidgetItem(s))
            self.parent.tableWidget_In1.setItem(i, 1, QTableWidgetItem("0"))
        
        self.close()

    def putSpeciesButtonClicked(self):
        """Add selected items to the other QListWidget"""
        spe_sel = self.ui.listWidget_all.selectedItems()
        if spe_sel:
            spe_sel = [s.text() for s in spe_sel]
            self.ui.listWidget_select.addItems(spe_sel)
        spe_sel = self.ui.listWidget_select.selectedItems()
        if spe_sel:
            spe_sel = [s.text() for s in spe_sel]
            spe_sel = set(spe_sel)
            spe_sel = (list(spe_sel))
            self.ui.listWidget_select.clear()
            self.ui.listWidget_all.addItems(spe_sel)

    def unPutSpeciesButtonClicked(self):
        """ Remove selected items from the QListWidget """
        spe_sel = self.ui.listWidget_select.selectedItems()
        if not spe_sel:
            return
        for item in spe_sel:
            self.ui.listWidget_select.takeItem(
                self.ui.listWidget_select.row(item))


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


if __name__ == "__main__":
    def run_app():
        # app = QApplication(sys.argv)
        if not QApplication.instance():
            app = QApplication(sys.argv)
        else:
            app = QApplication.instance()
        MainWindow = QMainWindow()
        win = Window(MainWindow)
        win.show()
        app.exec_()
        # sys.exit(app.exec())
    run_app()

    # app = QApplication(sys.argv)
    # win = Window()
    # win.show()
    # sys.exit(app.exec())

    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
