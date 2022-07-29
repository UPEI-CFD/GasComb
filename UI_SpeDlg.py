# -*- coding: utf-8 -*-

"""
File is part of GasComb software. See licence file of the project.
Copyright 2022 Jiri Vondal
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

import pySpal
from Species_dialog import Ui_SpeciesDialog

class UI_SpeDlg(QDialog, Ui_SpeciesDialog):
    """Species choice dialog."""

    def __init__(self, fnm, purefluids, tady, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_SpeciesDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.tady = tady
        if fnm in purefluids:
            spe_in = [fnm]
        else:
            spe_in = [n.name for n in pySpal.ct.Species.listFromFile(fnm)]
        self.ui.listWidget_all.addItems(spe_in)
        self.parent = parent
        self.fnm = fnm
        #Special handling of single species stream
        if fnm == "water.yaml" or fnm == "liquidvapor.yaml":
            self.ui.listWidget_all.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
    
    def okButtonClickedSpeciesDial(self):
        
        # Clear old rows
        self.tady.tableWidget_In1.setRowCount(0)
        # Get selected species
        spe_sel = [str(self.ui.listWidget_select.item(i).text())
                   for i in range(self.ui.listWidget_select.count())]
        #print("Row count:", len(spe_sel))
        #print(spe_sel)
        self.tady.spe_sel = spe_sel
        # Put species to table in Main Window
        self.tady.tableWidget_In1.setRowCount(len(spe_sel))
        #print("Row count:", len(spe_sel)+1)
        for i, s in enumerate(spe_sel):
            self.tady.tableWidget_In1.setItem(i, 0, QTableWidgetItem(s))
            if self.fnm == "water.yaml" or self.fnm == "liquidvapor.yaml":
                self.tady.tableWidget_In1.setItem(i, 1, QTableWidgetItem("1"))
            else:
                self.tady.tableWidget_In1.setItem(i, 1, QTableWidgetItem("0"))
        
        self.close()
        

    def putSpeciesButtonClicked(self):
        """Add selected items to the other QListWidget"""
        spe_sel = self.ui.listWidget_all.selectedItems()
        if spe_sel:
            spe_sel = [s.text() for s in spe_sel]
            #Special handling of single species stream
            if self.fnm == "water.yaml" or self.fnm == "liquidvapor.yaml":
                self.ui.listWidget_select.clear()
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
