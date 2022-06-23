# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GasComb_v3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, GasComb):
        GasComb.setObjectName("GasComb")
        GasComb.setGeometry(QtCore.QRect(0, 0, 890, 770))
        font = QtGui.QFont()
        font.setPointSize(10)
        GasComb.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("upi_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GasComb.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(GasComb)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBoxMechFile = QtWidgets.QComboBox(self.frame)
        self.comboBoxMechFile.setObjectName("comboBoxMechFile")
        self.horizontalLayout.addWidget(self.comboBoxMechFile)
        self.verticalLayout.addWidget(self.frame)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_4)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_T_in = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_T_in.setReadOnly(False)
        self.lineEdit_T_in.setObjectName("lineEdit_T_in")
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
        self.gridLayout.addWidget(self.lineEdit_Flow_in, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.lineEdit_P_in = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_P_in.setReadOnly(False)
        self.lineEdit_P_in.setObjectName("lineEdit_P_in")
        self.gridLayout.addWidget(self.lineEdit_P_in, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)
        self.lineEdit_RH_in = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_RH_in.setReadOnly(False)
        self.lineEdit_RH_in.setObjectName("lineEdit_RH_in")
        self.gridLayout.addWidget(self.lineEdit_RH_in, 3, 2, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_6)
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
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.checkBox_VolFr_in = QtWidgets.QCheckBox(self.tab)
        self.checkBox_VolFr_in.setChecked(True)
        self.checkBox_VolFr_in.setObjectName("checkBox_VolFr_in")
        self.verticalLayout_7.addWidget(self.checkBox_VolFr_in)
        self.tableWidget_In1 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_In1.setObjectName("tableWidget_In1")
        self.tableWidget_In1.setColumnCount(2)
        self.tableWidget_In1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_In1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_In1.setHorizontalHeaderItem(1, item)
        self.verticalLayout_7.addWidget(self.tableWidget_In1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.plainTextEdit_Stream1_out = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_Stream1_out.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.plainTextEdit_Stream1_out.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Stream1_out.setReadOnly(True)
        self.plainTextEdit_Stream1_out.setObjectName("plainTextEdit_Stream1_out")
        self.verticalLayout_10.addWidget(self.plainTextEdit_Stream1_out)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.tabWidget_2.addTab(self.tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget_2)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.frame_7 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Lambda = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Lambda.setObjectName("pushButton_Lambda")
        self.gridLayout_2.addWidget(self.pushButton_Lambda, 0, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_7)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_7)
        self.pushButtonEval_in = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonEval_in.setObjectName("pushButtonEval_in")
        self.verticalLayout.addWidget(self.pushButtonEval_in)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_5)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_Vf = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_Vf.setReadOnly(True)
        self.lineEdit_Vf.setClearButtonEnabled(False)
        self.lineEdit_Vf.setObjectName("lineEdit_Vf")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Vf)
        self.lineEdit_VfN = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_VfN.setReadOnly(True)
        self.lineEdit_VfN.setObjectName("lineEdit_VfN")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_VfN)
        self.lineEdit_mf = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_mf.setReadOnly(True)
        self.lineEdit_mf.setObjectName("lineEdit_mf")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_mf)
        self.lineEdit_tepl = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_tepl.setReadOnly(True)
        self.lineEdit_tepl.setObjectName("lineEdit_tepl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tepl)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_density = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_density.setReadOnly(True)
        self.lineEdit_density.setObjectName("lineEdit_density")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_density)
        self.lineEdit_visc = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_visc.setReadOnly(True)
        self.lineEdit_visc.setObjectName("lineEdit_visc")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_visc)
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_cp = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_cp.setReadOnly(True)
        self.lineEdit_cp.setObjectName("lineEdit_cp")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_cp)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_real = QtWidgets.QWidget()
        self.tab_real.setObjectName("tab_real")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_real)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget_Real = QtWidgets.QTableWidget(self.tab_real)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_Real.setFont(font)
        self.tableWidget_Real.setRowCount(1)
        self.tableWidget_Real.setColumnCount(3)
        self.tableWidget_Real.setObjectName("tableWidget_Real")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Real.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Real.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Real.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Real.setHorizontalHeaderItem(2, item)
        self.tableWidget_Real.horizontalHeader().setVisible(True)
        self.tableWidget_Real.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Real.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_Real.verticalHeader().setVisible(False)
        self.tableWidget_Real.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_Real.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_3.addWidget(self.tableWidget_Real)
        self.tabWidget.addTab(self.tab_real, "")
        self.tab_Dry = QtWidgets.QWidget()
        self.tab_Dry.setObjectName("tab_Dry")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_Dry)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget_Dry = QtWidgets.QTableWidget(self.tab_Dry)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_Dry.setFont(font)
        self.tableWidget_Dry.setRowCount(1)
        self.tableWidget_Dry.setColumnCount(3)
        self.tableWidget_Dry.setObjectName("tableWidget_Dry")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Dry.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Dry.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Dry.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Dry.setHorizontalHeaderItem(2, item)
        self.tableWidget_Dry.horizontalHeader().setVisible(True)
        self.tableWidget_Dry.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Dry.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_Dry.verticalHeader().setVisible(False)
        self.tableWidget_Dry.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_Dry.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_5.addWidget(self.tableWidget_Dry)
        self.tabWidget.addTab(self.tab_Dry, "")
        self.tab_Ref = QtWidgets.QWidget()
        self.tab_Ref.setObjectName("tab_Ref")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_Ref)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidget_RefO2 = QtWidgets.QTableWidget(self.tab_Ref)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_RefO2.setFont(font)
        self.tableWidget_RefO2.setRowCount(1)
        self.tableWidget_RefO2.setColumnCount(3)
        self.tableWidget_RefO2.setObjectName("tableWidget_RefO2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_RefO2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_RefO2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_RefO2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_RefO2.setHorizontalHeaderItem(2, item)
        self.tableWidget_RefO2.horizontalHeader().setVisible(True)
        self.tableWidget_RefO2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_RefO2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_RefO2.verticalHeader().setVisible(False)
        self.tableWidget_RefO2.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_RefO2.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_6.addWidget(self.tableWidget_RefO2)
        self.tabWidget.addTab(self.tab_Ref, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.pushButtonCalculate = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.verticalLayout_2.addWidget(self.pushButtonCalculate)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        GasComb.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GasComb)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        GasComb.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GasComb)
        self.statusbar.setObjectName("statusbar")
        GasComb.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(GasComb)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(GasComb)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(GasComb)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionClose = QtWidgets.QAction(GasComb)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout = QtWidgets.QAction(GasComb)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label_10.setBuddy(self.lineEdit_T_in)
        self.label_13.setBuddy(self.lineEdit_P_in)
        self.label_14.setBuddy(self.lineEdit_RH_in)

        self.retranslateUi(GasComb)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.pushButtonCalculate.clicked.connect(GasComb.calculateButtonClicked)
        self.pushButton_Lambda.clicked.connect(GasComb.lambdaButtonClicked)
        self.pushButtonEval_in.clicked.connect(GasComb.evalInButtonClicked)
        self.actionClose.triggered.connect(GasComb.close)
        self.pushButtonSpecies.clicked.connect(GasComb.speciesButtonClicked)
        self.pushButtonSetNG.clicked.connect(GasComb.NGButtonClicked)
        self.pushButtonSetAir.clicked.connect(GasComb.airButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(GasComb)
        GasComb.setTabOrder(self.lineEdit_T_in, self.lineEdit_Flow_in)
        GasComb.setTabOrder(self.lineEdit_Flow_in, self.lineEdit_P_in)
        GasComb.setTabOrder(self.lineEdit_P_in, self.lineEdit_RH_in)
        GasComb.setTabOrder(self.lineEdit_RH_in, self.checkBox_VolFr_in)
        GasComb.setTabOrder(self.checkBox_VolFr_in, self.tableWidget_In1)
        GasComb.setTabOrder(self.tableWidget_In1, self.plainTextEdit_Stream1_out)
        GasComb.setTabOrder(self.plainTextEdit_Stream1_out, self.lineEdit_2)
        GasComb.setTabOrder(self.lineEdit_2, self.pushButton_Lambda)
        GasComb.setTabOrder(self.pushButton_Lambda, self.lineEdit_3)
        GasComb.setTabOrder(self.lineEdit_3, self.pushButtonEval_in)
        GasComb.setTabOrder(self.pushButtonEval_in, self.lineEdit_tepl)
        GasComb.setTabOrder(self.lineEdit_tepl, self.lineEdit_mf)
        GasComb.setTabOrder(self.lineEdit_mf, self.lineEdit_Vf)
        GasComb.setTabOrder(self.lineEdit_Vf, self.lineEdit_VfN)
        GasComb.setTabOrder(self.lineEdit_VfN, self.lineEdit_density)
        GasComb.setTabOrder(self.lineEdit_density, self.lineEdit_visc)
        GasComb.setTabOrder(self.lineEdit_visc, self.lineEdit_cp)
        GasComb.setTabOrder(self.lineEdit_cp, self.tabWidget)
        GasComb.setTabOrder(self.tabWidget, self.tableWidget_Real)
        GasComb.setTabOrder(self.tableWidget_Real, self.pushButtonCalculate)
        GasComb.setTabOrder(self.pushButtonCalculate, self.comboBoxFlow1)
        GasComb.setTabOrder(self.comboBoxFlow1, self.tableWidget_Dry)
        GasComb.setTabOrder(self.tableWidget_Dry, self.tableWidget_RefO2)

    def retranslateUi(self, GasComb):
        _translate = QtCore.QCoreApplication.translate
        GasComb.setWindowTitle(_translate("MainWindow", "GasComb"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Inputs"))
        self.label.setText(_translate("MainWindow", "Choose Mechanism"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Gas Streams"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Inputs"))
        self.lineEdit_T_in.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Temperature [°C]"))
        self.comboBoxFlow1.setItemText(0, _translate("MainWindow", "Mass Flow Rate [kg/s]"))
        self.comboBoxFlow1.setItemText(1, _translate("MainWindow", "Vol. Flow Rate [Nm3/h]"))
        self.lineEdit_Flow_in.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "Pressure [Pa]"))
        self.lineEdit_P_in.setToolTip(_translate("MainWindow", "<html><head/><body><p>Absolute pressure.</p></body></html>"))
        self.lineEdit_P_in.setText(_translate("MainWindow", "101325"))
        self.label_14.setText(_translate("MainWindow", "Relative Humidity [%]"))
        self.lineEdit_RH_in.setToolTip(_translate("MainWindow", "<html><head/><body><p>If more than 0 -&gt; uit will overwrite dry species concentrations and add water vapour concentration.</p></body></html>"))
        self.lineEdit_RH_in.setText(_translate("MainWindow", "0"))
        self.pushButtonSetAir.setText(_translate("MainWindow", "Air"))
        self.pushButtonSetNG.setText(_translate("MainWindow", "Natural Gas"))
        self.pushButtonSpecies.setText(_translate("MainWindow", "Choose Species"))
        self.checkBox_VolFr_in.setText(_translate("MainWindow", "Vol. Fraction"))
        item = self.tableWidget_In1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Species Name"))
        item = self.tableWidget_In1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vol. Fraction"))
        self.groupBox.setTitle(_translate("MainWindow", "Properties - Stream 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Stream 1"))
        self.pushButton_Lambda.setToolTip(_translate("MainWindow", "<html><head/><body><p>Use only if you want to set air flow rate based on required Air-Fuel equivalence ratio. It adjusts only Stream 1 mass flow which has to be oxidizer.</p><p><span style=\" font-style:italic;\">λ</span> = 1.0 is at stoichiometry, rich mixtures <span style=\" font-style:italic;\">λ</span> &lt; 1.0, and lean mixtures <span style=\" font-style:italic;\">λ</span> &gt; 1.0. </p></body></html>"))
        self.pushButton_Lambda.setText(_translate("MainWindow", "Set Lambda"))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Air-Fuel equivalence ratio. <span style=\" font-style:italic;\">λ</span> = 1.0 is at stoichiometry, rich mixtures <span style=\" font-style:italic;\">λ</span> &lt; 1.0, and lean mixtures <span style=\" font-style:italic;\">λ</span> &gt; 1.0. </p></body></html>"))
        self.lineEdit_2.setText(_translate("MainWindow", "-"))
        self.label_11.setText(_translate("MainWindow", "Lambda"))
        self.label_12.setText(_translate("MainWindow", "Reference O2 [%]"))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Insert required reference O2 which will be used to compute species concentration in results. Allowed values are &lt;0;1&gt; or &lt;0;100&gt;.</p></body></html>"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.pushButtonEval_in.setText(_translate("MainWindow", "Evaluate inputs"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Results"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Physical variables"))
        self.label_2.setText(_translate("MainWindow", "Temperature [°C]"))
        self.label_4.setText(_translate("MainWindow", "Mass Flow Rate [kg/s]"))
        self.label_7.setText(_translate("MainWindow", "Volume Flow Rate [m3/h]"))
        self.label_8.setText(_translate("MainWindow", "Volume Flow Rate [Nm3/h]"))
        self.lineEdit_Vf.setText(_translate("MainWindow", "0"))
        self.lineEdit_VfN.setToolTip(_translate("MainWindow", "<html><head/><body><p>Volume flow rate at normal conditions: 0 °C, 101 325 Pa.</p></body></html>"))
        self.lineEdit_VfN.setText(_translate("MainWindow", "0"))
        self.lineEdit_mf.setText(_translate("MainWindow", "0"))
        self.lineEdit_tepl.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Density [kg/m3]"))
        self.label_5.setText(_translate("MainWindow", "Dynamic Viscosity [Pa-s]"))
        self.lineEdit_density.setText(_translate("MainWindow", "0"))
        self.lineEdit_visc.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Specific Heat [kJ/kg-K]"))
        self.lineEdit_cp.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Species"))
        self.tableWidget_Real.setSortingEnabled(True)
        item = self.tableWidget_Real.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nový řádek"))
        item = self.tableWidget_Real.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Species Name"))
        item = self.tableWidget_Real.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vol. Fraction"))
        item = self.tableWidget_Real.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mass Fraction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_real), _translate("MainWindow", "Real"))
        self.tableWidget_Dry.setSortingEnabled(True)
        item = self.tableWidget_Dry.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nový řádek"))
        item = self.tableWidget_Dry.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Species Name"))
        item = self.tableWidget_Dry.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vol. Fraction"))
        item = self.tableWidget_Dry.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mass Fraction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Dry), _translate("MainWindow", "Dry"))
        self.tableWidget_RefO2.setSortingEnabled(True)
        item = self.tableWidget_RefO2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nový řádek"))
        item = self.tableWidget_RefO2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Species Name"))
        item = self.tableWidget_RefO2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vol. Fraction"))
        item = self.tableWidget_RefO2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mass Fraction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Ref), _translate("MainWindow", "Reference O2"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Calculate"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open ..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as ..."))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GasComb = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(GasComb)
    GasComb.show()
    sys.exit(app.exec_())

