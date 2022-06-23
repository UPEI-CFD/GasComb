# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from SpecieseDialog import Ui_SpeciesDialog

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
