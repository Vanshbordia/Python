#!/usr/bin/python3.7
# coding: utf-8

from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QSpacerItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from Core.Widgets.pushButton import PushButton


class InformationsPage(QWidget):
    def __init__(self, parent):
        super(InformationsPage, self).__init__()
        self.parent = parent

        self.bsite = PushButton("Site")
        self.ltitre = QLabel("Vansh Bordia")
        d = "Web Browser" \
            "Version : 1.0.0 DEV\n\n\nSite :"
        self.ldescription = QLabel(d)
        self.image = QPixmap("logo.png")

        self.bsite.clicked.connect(self.openwebsite)
        self.ltitre.setAlignment(Qt.AlignHCenter)
        self.ldescription.setAlignment(Qt.AlignHCenter)
        self.grid = QGridLayout()
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(self.image)
        self.imageLabel.setAlignment(Qt.AlignHCenter)
        self.titreSpacerItem = QSpacerItem(20, 25)
        self.endSpacerItem = QSpacerItem(20, 500)

        self.grid.addWidget(self.imageLabel, 1, 1)
        self.grid.addWidget(self.ltitre, 2, 1)
        self.grid.addItem(self.titreSpacerItem, 3, 1)
        self.grid.addWidget(self.ldescription, 4, 1)
        self.grid.addWidget(self.bsite, 5, 1)
        self.grid.addItem(self.endSpacerItem, 6, 1)
        self.setLayout(self.grid)

    def openwebsite(self):
        self.parent.parent.opennewongletwithurl("http://github.com/vanshbordia")
