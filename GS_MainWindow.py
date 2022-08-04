# -*- coding: utf-8 -*-

"""
File is part of GasComb software. See licence file of the project.
Copyright 2022 Jiri Vondal
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QDesktopWidget, QProgressBar, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QSettings

from SpalGas import Ui_GasComb
# from SpecieseDialog import Ui_SpeciesDialog
import pySpal
from scipy.optimize import minimize_scalar
import copy

from TabPageMix import TabPageMix
from UI_SpeDlg import UI_SpeDlg
from Settings_dialog import Ui_Settings
from TabPageStream import TabPageStream
import json
import cantera as ct


class GS_MainWindow(QMainWindow, Ui_GasComb):
    def __init__(self, parent=None, version=None):
        super().__init__(parent)
        self.setupUi(self)
        self.version = version
        # Set list of mechanism files for combo box
        self.purefluids = ["CarbonDioxide", "Heptane",
                           "Hydrogen", "Methane", "Nitrogen", "Oxygen", "Water"]
        mechs = self.purefluids + pySpal.getMechanisms()
        self.comboBoxMechFile.addItems(mechs)
        try:
            self.comboBoxMechFile.setCurrentIndex(mechs.index("gri30.yaml"))
        except ValueError:
            self.comboBoxMechFile.setCurrentIndex(0)
        self.spe_sel = []

        # Store settings in registry - initialize basic info.
        self.settings = QSettings("UPI,FME,VUT", "GasComb")

        # Button to add new Stream tabs
        button = QtWidgets.QToolButton()
        button.setToolTip('Add New Stream')
        button.clicked.connect(self.addNewTab)
        button.setIcon(self.style().standardIcon(
            QtWidgets.QStyle.SP_DialogYesButton))
        self.tabWidget_2.setCornerWidget(button, QtCore.Qt.TopRightCorner)
        # self.addNewTab()   PE_IndicatorSpinPlus SP_DialogYesButton

        self.tabMix = None
        self.tabStream = [self]
        #self.tabStream = [TabPageStream(self)]

        # Activate signall calls
        self.connectSignalsSlots()

        # Validators to restrict inputs on float numbers only for some lineEdit fields
        validator1 = QtGui.QRegExpValidator(QtCore.QRegExp(
            r'[+-]?(\d+([.]\d*)?([eE][+-]?\d+)?|[.]\d+([eE][+-]?\d+)?)'))
        self.lineEdit_T_in.setValidator(validator1)
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(
            r'[+]?(\d+([.]\d*)?([eE][+-]?\d+)?|[.]\d+([eE][+-]?\d+)?)'))
        self.lineEdit_2.setValidator(validator)
        self.lineEdit_3.setValidator(validator)
        self.lineEdit_Flow_in.setValidator(validator)
        self.lineEdit_P_in.setValidator(validator)
        self.lineEdit_RH_in.setValidator(validator)
        # self.lineEdit_3.setValidator(QtGui.QDoubleValidator(self))

        # Move window to center of the screen
        self.center()

        # Switch if mechanism contains transport properties 'Multi'
        self.transport = True
        self.fileName = ""

        # Status bar and progress bar settings
        self.statusBar().showMessage('Ready')
        self.progressBar = QProgressBar()
        # self.progressBar.setGeometry(1, 1, 1, 1)
        # self.progressBar.setValue(20)
        self.progressBar.setTextVisible(False)
        self.progressBar.setVisible(False)
        self.statusBar().addPermanentWidget(self.progressBar)
        self.statusBar().setFixedHeight(20)

        # Settings of Flame speed calculation
        self.fs_enabled = False
        self.fs_ratio = 2
        self.fs_slope = 0.1
        self.fs_curve = 0.1
        self.fs_loglevel = 1
        self.fs_auto = False
        self.fs_width = 0.1

        # Settings for Cantera equilibrate function
        self.eqil = "HP"

        # Load Settings data from registry
        self.load_settings()

    #     #Context menu for Stream Tabs
    #     self.tabWidget_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    #     self.tabWidget_2.customContextMenuRequested.connect(self.openMenu)

    # def openMenu(self, position):
    #     """"Context menu for Stream Tabs"""
    #     menu = QtWidgets.QMenu()
    #     quitAction = menu.addAction("Quit")
    #     action = menu.exec_(self.tabWidget_2.mapToGlobal(position))
    #     if action == quitAction:
    #         QtWidgets.qApp.quit()

    def closeEvent(self, event):
        """
        Saves Settings/Options... to values stored in registry via QSettings.
        """
        self.settings.setValue("fs_enabled", self.fs_enabled)
        self.settings.setValue("fs_ratio", self.fs_ratio)
        self.settings.setValue("fs_slope", self.fs_slope)
        self.settings.setValue("fs_curve", self.fs_curve)
        self.settings.setValue("fs_loglevel", self.fs_loglevel)
        self.settings.setValue("fs_auto", self.fs_auto)
        self.settings.setValue("fs_width", self.fs_width)
        self.settings.setValue("equil", self.equil)

    @staticmethod
    def valueToBool(value):
        """Convert str('true') to bool value."""
        return value.lower() == 'true' if isinstance(value, str) else bool(value)

    def load_settings(self):
        """
        Loads Settings/Options... from values stored in registry via QSettings.
        """
        if self.settings.contains("fs_width"):
            self.fs_enabled = self.valueToBool(
                self.settings.value("fs_enabled"))
            self.fs_ratio = self.settings.value("fs_ratio")
            self.fs_slope = self.settings.value("fs_slope")
            self.fs_curve = self.settings.value("fs_curve")
            self.fs_loglevel = self.settings.value("fs_loglevel")
            self.fs_auto = self.valueToBool(self.settings.value("fs_auto"))
            self.fs_width = self.settings.value("fs_width")
            self.equil = self.settings.value("equil")

    def center(self):
        """
        Move window to center of the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def connectSignalsSlots(self):

        self.actionAbout.triggered.connect(self.about)
        self.actionOpen.triggered.connect(self.getFile)
        self.actionOpen.setShortcut(QtGui.QKeySequence("Ctrl+O"))
        self.actionSave.triggered.connect(self.saveSetup)
        self.actionSave.setShortcut(QtGui.QKeySequence("Ctrl+S"))
        self.actionSave_as.triggered.connect(self.saveSetup_as)
        self.actionSave_as.setShortcut(QtGui.QKeySequence("Ctrl+Shift+S"))
        self.actionOptions.triggered.connect(self.dialogSettings)
        self.tabStream[0].checkBox_VolFr_in.stateChanged.connect(
            lambda: self.VolFr_state_changed(self.tabStream[0]))
        # self.acceptSettings.triggered.connect(self.dialogSettings)

    @staticmethod
    def VolFr_state_changed(self, t):
        """
        When changed chek box option: Volume Fraction x Mass Fraction adjust header of Table with species

        Parameters
        ----------
        kind : TabPageStream
            Reference to TabPageStream class where the checkbox belong.
        """
        tw = t.tableWidget_In1
        if t.checkBox_VolFr_in.isChecked():
            tw.horizontalHeaderItem(1).setText("Volume Fraction")
        else:
            tw.horizontalHeaderItem(1).setText("Mass Fraction")

    def addNewTab(self):
        """
        Add new Stream tab.        
        """
        self.tabStream.append(TabPageStream(self))
        self.tabStream[-1].checkBox_VolFr_in.stateChanged.connect(
            lambda: self.VolFr_state_changed(self.tabStream[-1]))

    def notImplemented_Msg(self):
        """
        Use this message box where the feature is not yet implemented.
        """
        QMessageBox.warning(self, "Warning", "Not yet implemented")

    def getFile(self):
        """
        Reads saved setup of all inputs from json file
        """
        # self.notImplemented_Msg()
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '.\\', "Setup files (*.json);;All files (*)")
        self.fileName = fname[0]
        if self.fileName != "":
            # print(fname)
            with open(self.fileName) as f:
                config = json.load(f)
                # TODO: Check for existence in comboBox list
                index = self.comboBoxMechFile.findText(
                    config[0]["mechanismFile"])
                self.comboBoxMechFile.setCurrentIndex(index)
                self.lineEdit_2.setText(config[0]["lambda"])
                self.lineEdit_3.setText(config[0]["refO2"])

                # self.fs_enabled = config[0]["fsEnabled"]
                # self.fs_ratio = config[0]["fsRatio"]
                # self.fs_slope= config[0]["fsSlope"]
                # self.fs_curve = config[0]["fsCurve"]
                # self.fs_width = config[0]["fsWidth"]
                # self.fs_loglevel = config[0]["fsLoglevel"]
                # self.fs_auto = config[0]["fsAuto"]

                # Remove extra Stream tabs which are not needed.
                l = len(self.tabStream)
                for i, t in enumerate(reversed(self.tabStream[1:])):
                    if t is not None:
                        t.deleteLater()
                        t.close()
                        self.tabWidget_2.removeTab(l-i-1)
                self.tabStream = [self.tabStream[0]]

                t = self.tabStream[0]
                t.lineEdit_T_in.setText(str(config[1]["t1"]-273.15))
                t.lineEdit_Flow_in.setText(str(config[1]["mf1"]))
                t.lineEdit_P_in.setText(str(config[1]["p1"]))
                t.lineEdit_RH_in.setText(str(config[1]["rh"]))
                volFr = config[1]["volumeFractionChecked"]

                # Set checkbox and table header for Volume/Mass Fraction
                tw = t.tableWidget_In1
                if volFr:
                    t.checkBox_VolFr_in.setChecked(True)
                    tw.horizontalHeaderItem(1).setText("Volume Fraction")
                else:
                    t.checkBox_VolFr_in.setChecked(False)
                    tw.horizontalHeaderItem(1).setText("Mass Fraction")

                # Clear old rows
                t.tableWidget_In1.setRowCount(0)
                # Put species to table in Main Window
                t.tableWidget_In1.setRowCount(config[1]["rows_no"])

                # Loop over all saved species in json file and add them to first stream tab
                for i, (k, v) in enumerate(config[1]["species"].items()):
                    t.tableWidget_In1.setItem(i, 0, QTableWidgetItem(k))
                    t.tableWidget_In1.setItem(i, 1, QTableWidgetItem(str(v)))

                # For other stream tabs loop over their all species and put them to tabs
                for i, c in enumerate(config[2:]):
                    try:
                        t = self.tabStream[i+1]
                    except IndexError:
                        self.tabStream.append(TabPageStream(self))
                        t = self.tabStream[i+1]
                    t.lineEdit_T_in.setText(str(c["t1"]-273.15))
                    t.lineEdit_Flow_in.setText(str(c["mf1"]))
                    t.lineEdit_P_in.setText(str(c["p1"]))
                    t.lineEdit_RH_in.setText(str(c["rh"]))
                    volFr = c["volumeFractionChecked"]

                    # Set checkbox and table header for Volume/Mass Fraction
                    tw = t.tableWidget_In1
                    if volFr:
                        t.checkBox_VolFr_in.setChecked(True)
                        tw.horizontalHeaderItem(1).setText("Volume Fraction")
                    else:
                        t.checkBox_VolFr_in.setChecked(False)
                        tw.horizontalHeaderItem(1).setText("Mass Fraction")

                    # Clear old rows
                    t.tableWidget_In1.setRowCount(0)
                    # Put species to table in Main Window
                    t.tableWidget_In1.setRowCount(c["rows_no"])
                    # print("Row count:", len(spe_sel)+1)
                    for j, (k, v) in enumerate(c["species"].items()):
                        t.tableWidget_In1.setItem(j, 0, QTableWidgetItem(k))
                        t.tableWidget_In1.setItem(
                            j, 1, QTableWidgetItem(str(v)))

        # self.le.setPixmap(QPixmap(fname))

    def saveToJson(self):
        """
        Saves data from streams into json file 
        """
        datas = [{"mechanismFile": self.comboBoxMechFile.currentText(),
                  "lambda": self.lineEdit_2.text(), "refO2": self.lineEdit_3.text()}]  # ,\
        # "fsEnabled":self.fs_enabled, "fsRatio":self.fs_ratio, "fsSlope":self.fs_slope, "fsCurve":self.fs_curve, \
        #     "fsWidth":self.fs_width, "fsLoglevel":self.fs_loglevel, "fsAuto":self.fs_auto}]
        for t in self.tabStream:
            # Loop over all Streams ans save data to list of dictionaries
            t1 = float(t.lineEdit_T_in.text())+273.15
            mf1 = float(t.lineEdit_Flow_in.text())
            p1 = float(t.lineEdit_P_in.text())
            rh = float(t.lineEdit_RH_in.text())
            volFr = t.checkBox_VolFr_in.isChecked()

            # Read data from table of species concetration
            tw = t.tableWidget_In1
            allRows = tw.rowCount()
            data = {"t1": t1, "mf1": mf1, "p1": p1, "rh": rh,
                    "rows_no": allRows, "volumeFractionChecked": volFr}
            spe_conc = {}
            for row in range(allRows):
                spe_conc[tw.item(row, 0).text()] = float(
                    tw.item(row, 1).text())

            data.update({"species": spe_conc})
            datas.append(data)

        # Write data to file in json format
        print("Saving settings to file:", self.fileName)
        with open(self.fileName, "w") as f:
            json.dump(datas, f, indent=2)

    def saveSetup(self):
        # self.notImplemented_Msg()
        if not self.fileName:
            self.saveSetup_as()
        else:
            self.saveToJson()

    def saveSetup_as(self):
        # self.notImplemented_Msg()
        fname = QFileDialog.getSaveFileName(self, 'Save file as',
                                            '.\\', "Setup files (*.json);;All files (*)")
        self.fileName = fname[0]
        if self.fileName != "":
            # print(self.fileName)
            self.saveToJson()
        else:
            QMessageBox.warning(
                self, "Error", "Invalid file name. Data not saved. Choose valid filename.")

    def about(self):
        QMessageBox.about(
            self,
            "About GasComb Application",
            pySpal.license_description.format(self.version),
        )

    def dialogSettings(self):
        """Load dialog with Settings options - Menu->Settings->Options..."""
        settings = SettingsDlg(self)  # self)
        settings.exec()

    def speciesButtonClicked(self):

        dialog = UI_SpeDlg(self.comboBoxMechFile.currentText(),
                           self.purefluids, self, self)  # self)
        dialog.exec()

    def airButtonClicked(self):
        """Preset species to composition of Air and put it to table."""
        mechFile = self.comboBoxMechFile.currentText()
        spes = [n.name for n in pySpal.ct.Species.listFromFile(mechFile)]

        # Clear old rows
        self.tableWidget_In1.setRowCount(0)
        spe_sel = {'O2': 0.2095, 'N2': 0.7809,
                   'Ar': 0.0093, 'CO2': 0.0003, 'H2O': 0}
        # Put species to table in Main Window
        j = 0
        for (k, v) in spe_sel.items():
            if k in spes:
                rowCount = self.tableWidget_In1.rowCount()
                self.tableWidget_In1.insertRow(rowCount)
                self.tableWidget_In1.setItem(j, 0, QTableWidgetItem(k))
                self.tableWidget_In1.setItem(j, 1, QTableWidgetItem(str(v)))
                j += 1

        # Read data from table of species concetration
        tw = self.tableWidget_In1
        allRows = tw.rowCount()
        sps = []
        for row in range(allRows):
            sps.append(float(tw.item(row, 1).text()))
        # Correction for missing spescies - renormalization of sum to 1
        tot = sum(sps)
        sps = [n/tot for n in sps]
        for i, s in enumerate(sps):
            self.tableWidget_In1.setItem(
                i, 1, QTableWidgetItem("{:.4f}".format(s)))

    def NGButtonClicked(self):
        """Preset species to composition of Methane and put it to table."""
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
        """Do all the calculation and print results."""
        spaliny = self.evalInButtonClicked()
        if not spaliny:
            return
        t_in, p_in, x_in = spaliny.TPX
        
        # Get data from user's inputs
        mechFile = self.comboBoxMechFile.currentText()

        # ------When PureFluid is selected instead of Mechanism File------
        if mechFile in self.purefluids or mechFile == "water.yaml" or mechFile == "liquidvapor.yaml":
            self.lineEdit_tepl.setText("{:.2f}".format(spaliny.T-273.15))
            self.lineEdit_FlSp.setText("-")
            if not mechFile == "water.yaml":
                self.lineEdit_mf.setText("{:.3g}".format(spaliny.mass))
                self.lineEdit_Vf.setText(
                    "{:.2g}".format(spaliny.mass/spaliny.density))
            else:
                self.lineEdit_mf.setText("-")
                self.lineEdit_Vf.setText("-")
            self.lineEdit_density.setText("{:.4f}".format(spaliny.density))
            self.lineEdit_cp.setText("{:.2f}".format(spaliny.cp))
            self.lineEdit_VfN.setText("-")
            if self.transport:
                self.lineEdit_visc.setText("{:.4g}".format(spaliny.viscosity))
                self.lineEdit_conduct.setText(
                    "{:.4f}".format(spaliny.thermal_conductivity))
            else:
                self.lineEdit_visc.setText("-")
                self.lineEdit_conduct.setText("-")

            # Real Raw output
            self.plainTextEdit_realTxt.clear()
            self.plainTextEdit_realTxt.insertPlainText(
                spaliny.report(show_thermo=True))
            return
        # ------------

        try:
            spaliny.equilibrate(self.equil)
        except ct.CanteraError as err:
            print(err)
            print("Stopping calculation - correct the error and run again!")
            QMessageBox.warning(self, "Error", "{0}\n{1}".format(
                err, "Stopping calculation - correct the error and run again!"))
            return

        self.lineEdit_tepl.setText("{:.2f}".format(spaliny.T-273.15))
        self.lineEdit_mf.setText("{:.3f}".format(spaliny.mass))
        self.lineEdit_Vf.setText("{:.2f}".format(spaliny.mass/spaliny.density))
        self.lineEdit_density.setText("{:.4f}".format(spaliny.density))
        self.lineEdit_cp.setText("{:.2f}".format(spaliny.cp))
        if self.transport:
            self.lineEdit_visc.setText("{:.4g}".format(spaliny.viscosity))
            self.lineEdit_conduct.setText(
                "{:.4f}".format(spaliny.thermal_conductivity))
        else:
            self.lineEdit_visc.setText("-")
            self.lineEdit_conduct.setText("-")

        # Table Real
        self.tableWidget_Real.setRowCount(0)
        self.tableWidget_Real.setRowCount(len(spaliny.X))
        for i, s in enumerate(zip(spaliny.species_names, spaliny.X, spaliny.Y)):
            # print(s[0],s[1])
            self.tableWidget_Real.setItem(i, 0, QTableWidgetItem(s[0]))
            self.tableWidget_Real.setItem(
                i, 1, QTableWidgetItem("{:.6f}".format(s[1])))
            self.tableWidget_Real.setItem(
                i, 2, QTableWidgetItem("{:.6f}".format(s[2])))
        self.tableWidget_Real.sortItems(2, QtCore.Qt.DescendingOrder)

        t, p = spaliny.TP
        spaliny.TP = 273.15, 101325
        self.lineEdit_VfN.setText(
            "{:.2f}".format(spaliny.mass/spaliny.density))
        spaliny.TP = t, p

        # Real Raw output
        self.plainTextEdit_realTxt.clear()
        self.plainTextEdit_realTxt.insertPlainText(
            spaliny.report(show_thermo=True))

        # Table Dry
        pySpal.set_water_X(spaliny, 0)
        # print(spaliny.report())
        self.tableWidget_Dry.setRowCount(0)
        self.tableWidget_Dry.setRowCount(len(spaliny.X))
        for i, s in enumerate(zip(spaliny.species_names, spaliny.X, spaliny.Y)):
            # print(s[0], s[1])
            self.tableWidget_Dry.setItem(i, 0, QTableWidgetItem(s[0]))
            self.tableWidget_Dry.setItem(
                i, 1, QTableWidgetItem("{:.6f}".format(s[1])))
            self.tableWidget_Dry.setItem(
                i, 2, QTableWidgetItem("{:.6f}".format(s[2])))
        self.tableWidget_Dry.sortItems(2, QtCore.Qt.DescendingOrder)

        # Dry Raw output
        self.plainTextEdit_dryTxt.clear()
        self.plainTextEdit_dryTxt.insertPlainText(
            spaliny.report(show_thermo=True))

        # Table Reference O2
        o2_ref = float(self.lineEdit_3.text())/100
        try:
            pySpal.set_O2_ref_X(spaliny, o2_ref)
            self.tableWidget_RefO2.setRowCount(0)
            self.tableWidget_RefO2.setRowCount(len(spaliny.X))
            for i, s in enumerate(zip(spaliny.species_names, spaliny.X, spaliny.Y)):
                # print(s[0],s[1],s[2])
                self.tableWidget_RefO2.setItem(i, 0, QTableWidgetItem(s[0]))
                self.tableWidget_RefO2.setItem(
                    i, 1, QTableWidgetItem("{:.6f}".format(s[1])))
                self.tableWidget_RefO2.setItem(
                    i, 2, QTableWidgetItem("{:.6f}".format(s[2])))
            self.tableWidget_RefO2.sortItems(2, QtCore.Qt.DescendingOrder)
        except ct.CanteraError as err:
            print(err)
            print("Cannot calculate with reference O2 - correct the error and run again!")
            QMessageBox.warning(self, "Error", "{0}\n{1}".format(
                err, "Cannot calculate with reference O2 - correct the error and run again!"))
            pass

        # flame_speed = pySpal.getFlameSpeed(gas1)
        # self.lineEdit_FlSp.setText("{:.3f}".format(flame_speed))

        if self.fs_enabled:
            # Calculate Flame speed when enabled in Settings/Options... with multithreading.
            self.lineEdit_FlSp.setText("")
            self.lineEdit_FlSp.setEnabled(True)
            gas1 = ct.Solution(mechFile)
            gas1.TPX = t_in, p_in, x_in
            # Create a QThread object
            self.thread = QThread()
            # Create a worker object
            self.worker = Worker(gas1, self.fs_ratio, self.fs_slope,
                                 self.fs_curve, self.fs_loglevel, self.fs_width, self.fs_auto)
            # Move worker to the thread
            self.worker.moveToThread(self.thread)
            # Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)

            # Start the thread
            self.thread.start()
            print("Getting flame speed results")
            # Final settings
            self.lineEdit_FlSp.setEnabled(False)

            # Seems start has to be placed before finished call
            # lambda: print("Start worker"))
            self.worker.start.connect(self.on_flame_start)
            self.worker.finished.connect(self.on_flame_finished)
        else:
            self.lineEdit_FlSp.setText("Disabled in Settings")
            self.lineEdit_FlSp.setEnabled(False)

    def on_flame_start(self):
        """ Set status bar text and progressbar pulsating bar. """
        self.statusBar().showMessage("Calculating Flame speed ...")
        self.progressBar.setVisible(True)
        self.progressBar.setRange(0, 0)

    def on_flame_finished(self, flame_speed):
        """Used for threading flame speed calculation"""
        print("Flame speed:", flame_speed, "m/s")
        self.lineEdit_FlSp.setEnabled(True)
        self.lineEdit_FlSp.setText("{:.3f}".format(flame_speed))
        self.progressBar.setVisible(False)
        self.statusBar().showMessage("Ready")
        # self.progres_worker.requestInterruption()

    def get_lmbd(self, streams, mass_ox):
        """Get Air-Fuel ratio based on equivalence ratio."""
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
        if mechFile in self.purefluids or mechFile == "water.yaml" or mechFile == "liquidvapor.yaml":
            QMessageBox.information(
                self, "Information", "Lambda is not relevant for Pure Fluids.")
            return

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
            try:
                gas1 = pySpal.ct.Solution(mechFile, transport_model='Multi')
                self.transport = True
            except ct.CanteraError as err:
                print(err)
                gas1 = pySpal.ct.Solution(mechFile, name="gas")
                self.transport = False
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
        """
        Evaluate inputs and print information about input streams and resulting mixture.
        """
        spaliny = ""
        streams = []

        # print(self.fs_ratio, self.fs_slope, self.fs_curve,self.fs_loglevel, self.fs_width, self.fs_auto)

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

            # ------When PureFluid is selected instead of Mechanism File-----
            if mechFile in self.purefluids:
                if mechFile == "Water":
                    self.transport = True
                else:
                    self.transport = False
                fnct = getattr(ct, mechFile)
                gas1 = fnct()
                try:
                    gas1.TP = t1, p1
                except ct.CanteraError as err:
                    print(err)
                    print("Stopping calculation - correct the error and run again!")
                    QMessageBox.warning(self, "Error", "{0}\n{1}".format(
                        err, "Stopping calculation - correct the error and run again!"))
                    return
                spaliny = pySpal.ct.Quantity(gas1, constant='HP')

                if t.comboBoxFlow1.currentText() == "Mass Flow Rate [kg/s]":
                    spaliny.mass = mf1
                else:
                    spaliny.TP = 273.15, 101325
                    dens = spaliny.density
                    spaliny.mass = mf1*dens
                    spaliny.TP = t1, p1

                # -------------------------------------------
            else:
                # Set the cantera object of the first gas stream
                # TODO Check if Multi option exists for other mechanism files
                try:
                    list(spe_conc.keys())[0]
                except IndexError as err:
                    print(err)
                    print("Stopping calculation - no species specified for a Stream!")
                    QMessageBox.warning(
                        self, "Error", "No species specified for a Stream!\nSpecify species in all Streams and run again.")
                    return

                try:
                    gas1 = pySpal.ct.Solution(
                        mechFile, transport_model='Multi')
                    self.transport = True
                except ct.CanteraError as err:
                    print(err)
                    if mechFile == "liquidvapor.yaml":
                        self.transport = False
                        if list(spe_conc.keys())[0] == "H2O":
                            gas1 = pySpal.ct.Solution(mechFile, name="water")
                        elif list(spe_conc.keys())[0] == "N2":
                            gas1 = pySpal.ct.Solution(
                                mechFile, name="nitrogen")
                        elif list(spe_conc.keys())[0] == "CH4":
                            gas1 = pySpal.ct.Solution(mechFile, name="methane")
                        elif list(spe_conc.keys())[0] == "H2":
                            gas1 = pySpal.ct.Solution(
                                mechFile, name="hydrogen")
                        elif list(spe_conc.keys())[0] == "O2":
                            gas1 = pySpal.ct.Solution(mechFile, name="oxygen")
                        elif list(spe_conc.keys())[0] == "CO2":
                            gas1 = pySpal.ct.Solution(
                                mechFile, name="carbon-dioxide")
                        elif list(spe_conc.keys())[0] == "C7H16":
                            gas1 = pySpal.ct.Solution(mechFile, name="heptane")
                        elif list(spe_conc.keys())[0] == "C2F4H2":
                            gas1 = pySpal.ct.Solution(
                                mechFile, name="HFC-134a")

                    elif mechFile == "silane.yaml":
                        gas1 = pySpal.ct.Solution(mechFile, name="gas")
                        self.transport = False
                    elif mechFile == "water.yaml":
                        self.transport = False
                        if list(spe_conc.keys())[0] == "H2O(S)":
                            gas1 = pySpal.ct.Solution(mechFile, name="ice")
                        elif list(spe_conc.keys())[0] == "H2O(L)":
                            gas1 = pySpal.ct.Solution(
                                mechFile, name="liquid_water")
                        gas1.TP = t1, p1
                        t.plainTextEdit_Stream1_out.clear()
                        t.plainTextEdit_Stream1_out.insertPlainText(
                            gas1.report())
                        return gas1
                    else:
                        gas1 = pySpal.ct.Solution(mechFile)
                        self.transport = False

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
                    try:
                        pySpal.set_water_phi(spaliny, float(rh)/100)
                    except ct.CanteraError as err:
                        print(err)
                        print(
                            "Stopping calculation - correct the error and run again!")
                        QMessageBox.warning(self, "Error", "{0}\n{1}".format(
                            err, "Stopping calculation - correct the error and run again!"))

                        return
                    if t.checkBox_VolFr_in.isChecked() == True:
                        h2o_val = spaliny.X[spaliny.species_index("H2O")]
                    else:
                        h2o_val = spaliny.Y[spaliny.species_index("H2O")]

                    h2o_item = tw.findItems("H2O", QtCore.Qt.MatchExactly)
                    h2o_val_old = 0
                    if h2o_item:
                        row = h2o_item[0].row()
                        h2o_val_old = float(tw.item(row, 1).text())
                        tw.item(row, 1).setText("{:.4f}".format(h2o_val))
                    else:
                        # Add missing H2O species to the end of the table
                        tw.insertRow(tw.rowCount())
                        item = QtWidgets.QTableWidgetItem("H2O")
                        tw.setItem(tw.rowCount()-1, 0, item)
                        item = QtWidgets.QTableWidgetItem(
                            "{:.4f}".format(h2o_val))
                        tw.setItem(tw.rowCount()-1, 1, item)
                    for row in range(tw.rowCount()):
                        if tw.item(row, 0):
                            if not tw.item(row, 0).text() == "H2O":
                                val = float(tw.item(row, 1).text())
                                new_val = val*(1-h2o_val)/(1-h2o_val_old)
                                tw.item(row, 1).setText(
                                    "{:.4f}".format(new_val))

            t.plainTextEdit_Stream1_out.clear()
            t.plainTextEdit_Stream1_out.insertPlainText(spaliny.report())
            streams.append(spaliny)

        Mix = streams[0]
        for s in streams[1:]:
            try:
                Mix += s
            except ZeroDivisionError as err:
                print(err)
                print("Check Mass or Volume flow rate for all streams!")
                QMessageBox.warning(self, "Error", "{0}\n{1}".format(
                    err, "Check Mass or Volume flow rate for all streams!"))

                return

        if not (mechFile in self.purefluids or mechFile == "water.yaml" or mechFile == "liquidvapor.yaml"):
            # Calculate Air to Fuel equivalence ratio (1/equivalence ratio)
            try:
                self.lineEdit_2.setText(str(1/Mix.equivalence_ratio()))
            except ZeroDivisionError as err:
                self.lineEdit_2.setText("-")

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


class Worker(QObject):
    """
    It's purpose is not to block GUI when calculation Flame speed, which is time
    consuming. It is used for threading.
    """
    finished = pyqtSignal(float)
    start = pyqtSignal()
    # result  = pyqtSignal(float)
    # progress = pyqtSignal(int)

    def __init__(self, gas1, ratio, slope, curve, loglevel, width, auto):
        super(Worker, self).__init__()
        self.gas1 = gas1
        self.ratio = ratio
        self.slope = slope
        self.curve = curve
        self.loglevel = loglevel
        self.width = width
        self.auto = auto
        self.start.emit()

    def run(self):
        """Long-running task."""
        self.start.emit()
        flame_speed = pySpal.getFlameSpeed(
            self.gas1, self.ratio, self.slope, self.curve, self.loglevel, self.width, self.auto)
        #flame_speed = pySpal.getFlameSpeed(self.gas1)
        # self.progress.emit(i + 1)
        self.finished.emit(flame_speed)


class SettingsDlg(QDialog):
    "Settings/Options... dialog"

    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Settings()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.checkBox_flSpeed.setChecked(parent.fs_enabled)
        self.ui.lineEdit_ratio.setText(str(parent.fs_ratio))
        self.ui.lineEdit_slope.setText(str(parent.fs_slope))
        self.ui.lineEdit_curve.setText(str(parent.fs_curve))
        self.ui.spinBox_logLevel.setValue(parent.fs_loglevel)
        self.ui.lineEdit_width.setText(str(parent.fs_width))
        self.ui.checkBox_auto.setChecked(parent.fs_auto)
        # Set Equilibrate option according the previous choice
        index = self.ui.comboBox_equilibrate.findText(
            self.parent.equil, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.comboBox_equilibrate.setCurrentIndex(index)

    def acceptSettingsClicked(self):
        """ Load choices from dialog to class variables. """
        self.parent.fs_enabled = self.ui.checkBox_flSpeed.isChecked()
        self.parent.fs_ratio = float(self.ui.lineEdit_ratio.text())
        self.parent.fs_slope = float(self.ui.lineEdit_slope.text())
        self.parent.fs_curve = float(self.ui.lineEdit_curve.text())
        self.parent.fs_loglevel = self.ui.spinBox_logLevel.value()
        self.parent.fs_width = float(self.ui.lineEdit_width.text())
        self.parent.fs_auto = self.ui.checkBox_auto.isChecked()

        self.parent.equil = self.ui.comboBox_equilibrate.currentText()

        self.close()
