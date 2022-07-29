# -*- coding: utf-8 -*-

"""
File is part of GasComb software. See licence file of the project.
Copyright 2022 Jiri Vondal
"""
__author__ = "Jiří Vondál"
__copyright__ = "Copyright 2022, Jiri Vondal"
__version__ = '0.2.0'
__name__ = "GasComb"
__email__ = "vondal@fme.vutbr.cz"

import sys
# from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from GS_MainWindow import GS_MainWindow

def run_app():
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    MainWindow = QMainWindow()
    win = GS_MainWindow(MainWindow, __version__)
    win.show()
    app.exec_()
        
run_app()


# if __name__ == "__main__":
    # def run_app():
        ##app = QApplication(sys.argv)
        # if not QApplication.instance():
            # app = QApplication(sys.argv)
        # else:
            # app = QApplication.instance()
        # MainWindow = QMainWindow()
        # win = GS_MainWindow(MainWindow)
        # win.show()
        # app.exec_()
        
    # run_app()
