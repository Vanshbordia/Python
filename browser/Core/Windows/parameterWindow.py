#!/usr/bin/python3.7
# coding: utf-8

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTabWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from Core.Windows.ParametersPages.generalPage import GeneralPage
from Core.Windows.ParametersPages.historyPage import HistoryPage
from Core.Windows.ParametersPages.bookmarksPage import BookmarksPage
from Core.Windows.ParametersPages.informationsPage import InformationsPage
from Core.Windows.ParametersPages.raccourcisPage import RaccourcisPage


class ParameterWindow(QWidget):
    def __init__(self, parent):
        super(ParameterWindow, self).__init__()
        self.parent = parent
        self.setWindowTitle('Settings')
        self.grid = QGridLayout()
        
        self.title = QLabel("Settings")
        self.title.setAlignment(Qt.AlignHCenter)

        self.generalPage = GeneralPage(self)
        self.historyPage = HistoryPage(self)
        self.bookmarksPage = BookmarksPage(self)
        self.informationsPage = InformationsPage(self)
        self.raccourcisPage = RaccourcisPage(self)

        self.tabWidget = QTabWidget(self)
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.addTab(self.generalPage, QIcon("Icons/Parameters/General.png"), "")
        self.tabWidget.addTab(self.historyPage, QIcon("Icons/Parameters/History.png"), "")
        self.tabWidget.addTab(self.bookmarksPage, QIcon("Icons/Parameters/Fav.png"), "")
        self.tabWidget.addTab(self.raccourcisPage, QIcon("logo.png"), "")
        self.tabWidget.addTab(self.informationsPage, QIcon("Icons/Parameters/Info.png"), "")
        self.tabWidget.setTabToolTip(0, "Général")
        self.tabWidget.setTabToolTip(1, "Historique")
        self.tabWidget.setTabToolTip(2, "Favoris")
        self.tabWidget.setTabToolTip(3, "Raccourcis URL")
        self.tabWidget.setTabToolTip(4, "Informations")
        
        self.grid.addWidget(self.title, 0, 0)
        self.grid.addWidget(self.tabWidget, 1, 0)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setLayout(self.grid)
        self.setFixedSize(800, 800)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowTitleHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def ontabchange(self):
        self.historyPage.showUpdate()
        self.bookmarksPage.showUpdate()
