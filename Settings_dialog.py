# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(400, 300)
        Settings.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(Settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FlameSpeed = QtWidgets.QGroupBox(Settings)
        self.FlameSpeed.setObjectName("FlameSpeed")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.FlameSpeed)
        self.verticalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_flSpeed = QtWidgets.QCheckBox(self.FlameSpeed)
        self.checkBox_flSpeed.setEnabled(True)
        self.checkBox_flSpeed.setCheckable(True)
        self.checkBox_flSpeed.setChecked(False)
        self.checkBox_flSpeed.setObjectName("checkBox_flSpeed")
        self.verticalLayout_2.addWidget(self.checkBox_flSpeed)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, -1, 20, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.FlameSpeed)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_ratio = QtWidgets.QLineEdit(self.FlameSpeed)
        self.lineEdit_ratio.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_ratio.setObjectName("lineEdit_ratio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ratio)
        self.label_2 = QtWidgets.QLabel(self.FlameSpeed)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_slope = QtWidgets.QLineEdit(self.FlameSpeed)
        self.lineEdit_slope.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_slope.setObjectName("lineEdit_slope")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_slope)
        self.label_3 = QtWidgets.QLabel(self.FlameSpeed)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_curve = QtWidgets.QLineEdit(self.FlameSpeed)
        self.lineEdit_curve.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_curve.setObjectName("lineEdit_curve")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_curve)
        self.label_4 = QtWidgets.QLabel(self.FlameSpeed)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBox_logLevel = QtWidgets.QSpinBox(self.FlameSpeed)
        self.spinBox_logLevel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spinBox_logLevel.setMaximum(5)
        self.spinBox_logLevel.setProperty("value", 1)
        self.spinBox_logLevel.setObjectName("spinBox_logLevel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_logLevel)
        self.label_5 = QtWidgets.QLabel(self.FlameSpeed)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_width = QtWidgets.QLineEdit(self.FlameSpeed)
        self.lineEdit_width.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_width.setObjectName("lineEdit_width")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_width)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.checkBox_auto = QtWidgets.QCheckBox(self.FlameSpeed)
        self.checkBox_auto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_auto.setTristate(False)
        self.checkBox_auto.setObjectName("checkBox_auto")
        self.verticalLayout_2.addWidget(self.checkBox_auto)
        self.verticalLayout.addWidget(self.FlameSpeed)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.groupBox_2 = QtWidgets.QGroupBox(Settings)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comboBox_equilibrate = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_equilibrate.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_equilibrate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_equilibrate.setObjectName("comboBox_equilibrate")
        self.comboBox_equilibrate.addItem("")
        self.comboBox_equilibrate.addItem("")
        self.comboBox_equilibrate.addItem("")
        self.comboBox_equilibrate.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_equilibrate)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Settings)
        self.comboBox_equilibrate.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Settings.acceptSettingsClicked)
        self.buttonBox.rejected.connect(Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.FlameSpeed.setTitle(_translate("Settings", "Flame Speed"))
        self.checkBox_flSpeed.setText(_translate("Settings", "Enable Flame Speed Calulation"))
        self.label.setText(_translate("Settings", "Ratio"))
        self.lineEdit_ratio.setText(_translate("Settings", "2"))
        self.label_2.setText(_translate("Settings", "Slope"))
        self.lineEdit_slope.setText(_translate("Settings", "0.1"))
        self.label_3.setText(_translate("Settings", "Curve"))
        self.lineEdit_curve.setText(_translate("Settings", "0.1"))
        self.label_4.setText(_translate("Settings", "Log Level"))
        self.label_5.setText(_translate("Settings", "Width [m]"))
        self.lineEdit_width.setText(_translate("Settings", "0.1"))
        self.checkBox_auto.setText(_translate("Settings", "Auto Tune Solution"))
        self.groupBox_2.setTitle(_translate("Settings", "Other settings"))
        self.label_6.setText(_translate("Settings", "Equilibrate"))
        self.comboBox_equilibrate.setCurrentText(_translate("Settings", "HP"))
        self.comboBox_equilibrate.setItemText(0, _translate("Settings", "HP"))
        self.comboBox_equilibrate.setItemText(1, _translate("Settings", "UV"))
        self.comboBox_equilibrate.setItemText(2, _translate("Settings", "SV"))
        self.comboBox_equilibrate.setItemText(3, _translate("Settings", "SP"))

