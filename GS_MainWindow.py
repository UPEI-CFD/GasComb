# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QDesktopWidget

from SpalGas import Ui_GasComb
from SpecieseDialog import Ui_SpeciesDialog
import pySpal
from scipy.optimize import minimize_scalar
import copy

from TabPageMix import TabPageMix
from UI_SpeDlg import UI_SpeDlg
from TabPageStream import TabPageStream


class GS_MainWindow(QMainWindow, Ui_GasComb):
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
        button.setToolTip('Add New Stream')
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
        #Move window to center of the screen
        self.center()

    def center(self):
        #Move window to center of the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
        self.lineEdit_conduct.setText("{:.4f}".format(spaliny.thermal_conductivity))

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
        
        #Real Raw output
        self.plainTextEdit_realTxt.clear()
        self.plainTextEdit_realTxt.insertPlainText(spaliny.report(show_thermo=True))
        
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

        #Dry Raw output
        self.plainTextEdit_dryTxt.clear()
        self.plainTextEdit_dryTxt.insertPlainText(spaliny.report(show_thermo=True))

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
            # rh = float(t.lineEdit_RH_in.text())

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
                h2o_x = spaliny.X[spaliny.species_index("H2O")]
                h2o_item = tw.findItems("H2O", QtCore.Qt.MatchExactly)
                
                if h2o_item:
                    row = h2o_item[0].row()
                    tw.item(row,1).setText("{:.4f}".format(h2o_x))
                else:
                    #Add missing H2O species to the end of the table
                    tw.insertRow(tw.rowCount()) 
                    item = QtWidgets.QTableWidgetItem("H2O")
                    tw.setItem(tw.rowCount()-1, 0, item)
                    item = QtWidgets.QTableWidgetItem("{:.4f}".format(h2o_x))
                    tw.setItem(tw.rowCount()-1, 1, item)
                    

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

