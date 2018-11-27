#!/usr/bin/python3.7
# coding: utf-8

from PyQt5.QtWidgets import QMenu


class ContextMenu(QMenu):
    def __init__(self, onglet, hittest):
        super(ContextMenu, self).__init__()
        self.onglet = onglet
        contextmenudata = self.onglet.page.contextMenuData()
        hittest.updateWithContextMenuData(contextmenudata)
        self.addAction("Back", self.onglet.back)
        self.addAction("Forward", self.onglet.forward)
        self.addAction("Reload", self.onglet.reload)
        self.addAction("VSource", self.onglet.page.vsource)
        self.addSeparator()
        bookmarks = self.onglet.parent.dbConnection.executewithreturn("""SELECT * FROM bookmarks""")
        find = False
        for i in bookmarks:
            if i[2] == self.onglet.parent.browserWidget.url().toString():
                find = True
        if find:
            self.addAction("Delete Favourite", self.onglet.parent.fav)
        else:
            self.addAction("Add Favourite", self.onglet.parent.fav)
        if hittest.isContentEditable():
            self.addSeparator()
            self.addAction("Cut", self.onglet.page.cutaction)
            self.addAction("Copy", self.onglet.page.copyaction)
            self.addAction("Paste", self.onglet.page.pasteaction)
        if hittest.imageUrl() != "":
            self.addSeparator()
            self.addAction("Your Image", lambda: self.onglet.parent.opennewongletwithurl(hittest.imageUrl()))
        self.addSeparator()
        clickedurl = hittest.linkUrl()
        baseurl = hittest.baseUrl()
        if clickedurl != baseurl and clickedurl != '':
            if 'http://' in clickedurl or 'https://' in clickedurl:
                url = clickedurl
            elif clickedurl == "#":
                url = baseurl + clickedurl
            else:
                url = "http://" + baseurl.split("/")[2] + clickedurl
            self.addAction("Open New Tab", lambda: self.onglet.parent.opennewongletwithurl(url))
