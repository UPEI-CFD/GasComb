# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Species_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpeciesDialog(object):
    def setupUi(self, SpeciesDialog):
        SpeciesDialog.setObjectName("SpeciesDialog")
        SpeciesDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(SpeciesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(SpeciesDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_all = QtWidgets.QListWidget(self.frame)
        self.listWidget_all.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget_all.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_all.setObjectName("listWidget_all")
        self.horizontalLayout.addWidget(self.listWidget_all)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(80, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_speciesPut = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_speciesPut.setObjectName("pushButton_speciesPut")
        self.verticalLayout_2.addWidget(self.pushButton_speciesPut)
        self.pushButton_speciesUnPut = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_speciesUnPut.sizePolicy().hasHeightForWidth())
        self.pushButton_speciesUnPut.setSizePolicy(sizePolicy)
        self.pushButton_speciesUnPut.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_speciesUnPut.setObjectName("pushButton_speciesUnPut")
        self.verticalLayout_2.addWidget(self.pushButton_speciesUnPut)
        self.horizontalLayout.addWidget(self.frame_2)
        self.listWidget_select = QtWidgets.QListWidget(self.frame)
        self.listWidget_select.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget_select.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_select.setObjectName("listWidget_select")
        self.horizontalLayout.addWidget(self.listWidget_select)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(SpeciesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SpeciesDialog)
        self.buttonBox.accepted.connect(SpeciesDialog.okButtonClickedSpeciesDial)
        self.buttonBox.rejected.connect(SpeciesDialog.reject)
        self.pushButton_speciesPut.clicked.connect(SpeciesDialog.putSpeciesButtonClicked)
        self.pushButton_speciesUnPut.clicked.connect(SpeciesDialog.unPutSpeciesButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(SpeciesDialog)

    def retranslateUi(self, SpeciesDialog):
        _translate = QtCore.QCoreApplication.translate
        SpeciesDialog.setWindowTitle(_translate("SpeciesDialog", "Choose Species"))
        self.pushButton_speciesPut.setText(_translate("SpeciesDialog", ">>"))
        self.pushButton_speciesUnPut.setText(_translate("SpeciesDialog", "<<"))

