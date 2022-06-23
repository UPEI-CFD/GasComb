# -*- coding: utf-8 -*-

import sys
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from GS_MainWindow import GS_MainWindow

def run_app():
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    MainWindow = QMainWindow()
    win = GS_MainWindow(MainWindow)
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
