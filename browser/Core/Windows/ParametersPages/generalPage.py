#!/usr/bin/python3.7
# coding: utf-8

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QMessageBox, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

from Core.Widgets.pushButton import PushButton


class GeneralPage(QWidget):
    def __init__(self, parent):
        super(GeneralPage, self).__init__()
        self.parent = parent
        self.grid = QVBoxLayout()

        self.listeMoteur = ["Google", "Duckduckgo", "Ecosia", "Yahoo", "Bing"]
        moteurAcc = self.parent.parent.dbConnection.executewithreturn("""SELECT moteur FROM parameters""")[0][0]
        for i in range(len(self.listeMoteur)):
            if self.listeMoteur[i] == moteurAcc:
                self.listeMoteur[i], self.listeMoteur[0] = self.listeMoteur[0], self.listeMoteur[i]
        jsAcc = self.parent.parent.dbConnection.executewithreturn("""SELECT js FROM parameters""")[0][0]
        if jsAcc == "Active":
            self.listejs = ["Active", "Deactive"]
        else:
            self.listejs = ["Deactive", "Active"]

        self.lAccueil = QLabel("Home Page")
        self.lAccueil.setAlignment(Qt.AlignHCenter)
        self.urlAccueil = QLineEdit(
            self.parent.parent.dbConnection.executewithreturn("""SELECT home FROM parameters""")[0][0])
        self.urlAccueil.setAlignment(Qt.AlignHCenter)
        self.lMoteur = QLabel("Search Engine")
        self.lMoteur.setAlignment(Qt.AlignHCenter)
        self.moteurBox = QComboBox()
        self.moteurBox.addItems(self.listeMoteur)
        self.lJS = QLabel("Javascript")
        self.lJS.setAlignment(Qt.AlignHCenter)
        self.jsbox = QComboBox()
        self.jsbox.addItems(self.listejs)

        self.endSpacerItem = QSpacerItem(20, 600)
        self.paramSpacerItem = QSpacerItem(20, 25)
        self.bValid = PushButton("Save")

        self.bValid.clicked.connect(self.valider)

        self.grid.addWidget(self.lAccueil)
        self.grid.addWidget(self.urlAccueil)
        self.grid.addItem(self.paramSpacerItem)
        self.grid.addWidget(self.lMoteur)
        self.grid.addWidget(self.moteurBox)
        self.grid.addItem(self.paramSpacerItem)
        self.grid.addWidget(self.lJS)
        self.grid.addWidget(self.jsbox)
        self.grid.addItem(self.endSpacerItem)
        self.grid.addWidget(self.bValid)
        self.setLayout(self.grid)
    
    def valider(self):
        parameters = self.parent.parent.dbConnection.executewithreturn("""SELECT * FROM parameters""")
        self.parent.parent.dbConnection.executewithoutreturn(
            """UPDATE parameters SET home = ? WHERE id = ?""", (self.urlAccueil.text(),parameters[0][0]))
        self.parent.parent.dbConnection.executewithoutreturn(
            """UPDATE parameters SET moteur = ? WHERE id = ?""",
            (self.listeMoteur[self.moteurBox.currentIndex()],
             parameters[0][0]))
        self.parent.parent.dbConnection.executewithoutreturn(
            """UPDATE parameters SET js = ? WHERE id = ?""",
            (self.listejs[self.jsbox.currentIndex()],
             parameters[0][0]))
        if self.listejs[self.jsbox.currentIndex()] == "Active":
            QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        else:
            QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.JavascriptEnabled, False)
        QMessageBox().about(self, "Preferences Updated")
