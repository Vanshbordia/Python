#!/usr/bin/python3.7
# coding: utf-8

import sys
import shlex
import pip 

try:
    import PyQt5
except Exception:
    try:
        cmd = "install PyQt5"
        pip.main(shlex.split(cmd))
    except:
        
        sys.exit()
try:
    import PyQt5.QtWebEngine
except Exception:
    
    sys.exit()

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from Core.browser import Browser


def launch(sys):
    app = QApplication(sys.argv)
    icon = QIcon('logo.png')
    app.setWindowIcon(icon)

    Browser()

    app.exec_()


if __name__ == '__main__':
    launch(sys)
