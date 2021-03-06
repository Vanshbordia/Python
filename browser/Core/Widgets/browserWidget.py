#!/usr/bin/python3.7
# coding: utf-8

from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl, Qt, QEvent, QEventLoop, QPoint, QPointF, QVariant, QTimer
from PyQt5.QtWidgets import QAction

from Core.Utils.webHitTestResult import WebHitTestResult
from Core.Utils.contextMenu import ContextMenu


class BrowserWidget(QWebEngineView):
    def __init__(self, parent):
        super(BrowserWidget, self).__init__(parent)
        self.parent = parent
        self.page = Page(self)
        self.setPage(self.page)
        self.load(QUrl("http://google.com"))
        self.urlChanged.connect(self.parent.urlInput.seturl)
        self.titleChanged.connect(self.parent.settitle)
        self.iconChanged.connect(self.parent.tabWidget.seticon)
        self.loadFinished.connect(self.parent.loadfinished)
        self.page.fullScreenRequested.connect(self.page.makefullscreen)
        self.viewSource = QAction(self)
        self.viewSource.setShortcut(Qt.Key_F2)
        self.viewSource.triggered.connect(self.page.vsource)
        self.addAction(self.viewSource)

    def event(self, event):
        if event.type() == QEvent.ChildAdded:
            child_ev = event
            widget = child_ev.child()

            if widget:
                widget.installEventFilter(self)
            return True

        return super(BrowserWidget, self).event(event)

    def contextMenuEvent(self, event):
        hit = self.page.hittestcontent(event.pos())
        menu = ContextMenu(self, hit)
        pos = event.globalPos()
        p = QPoint(pos.x(), pos.y() + 1)
        menu.exec_(p)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonRelease:
            if event.button() == Qt.MiddleButton:
                hit = self.page.hittestcontent(event.pos())
                clickedurl = hit.linkurl()
                baseurl = hit.baseUrl()
                if clickedurl != baseurl and clickedurl != '':
                    if 'http://' in clickedurl or 'https://' in clickedurl:
                        result = clickedurl
                    elif clickedurl == "#":
                        result = baseurl + clickedurl
                    else:
                        result = "http://" + baseurl.split("/")[2] + clickedurl
                    self.parent.opennewongletwithurl(result)
                event.accept()
                return True
        return super(BrowserWidget, self).eventFilter(obj, event)


class Page(QWebEnginePage):
    def __init__(self, view):
        super(Page, self).__init__()
        self.parent = view.parent
        self.view = view
        self.result = QVariant()
        self.fullView = QWebEngineView()
        self.exitFSAction = QAction(self.fullView)
        self.loop = None

    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        """Override javaScriptConsoleMessage to use debug log."""
        if level == QWebEnginePage.InfoMessageLevel:
            print("JS - INFO - Ligne {} : {}".format(line, msg))
        elif level == QWebEnginePage.WarningMessageLevel:
            print("JS - WARNING - Ligne {} : {}".format(line, msg))
        else:
            print("JS - ERROR - Ligne {} : {}".format(line, msg))

    def hittestcontent(self, pos):
        return WebHitTestResult(self, pos)

    def maptoviewport(self, pos):
        return QPointF(pos.x(), pos.y())

    def executejavaScript(self, scriptsrc):
        self.loop = QEventLoop()
        self.result = QVariant()
        QTimer.singleShot(250, self.loop.quit)

        self.runJavaScript(scriptsrc, self.callbackJS)
        self.loop.exec_()
        self.loop = None
        return self.result

    def callbackjs(self, res):
        if self.loop is not None and self.loop.isRunning():
            self.result = res
            self.loop.quit()

    def vsource(self):
        if "view-source:http" in self.url().toString():
            self.load(QUrl(self.url().toString().split("view-source:")[1]))
        else:
            self.triggerAction(self.ViewSource)

    def cutaction(self):
        self.triggerAction(self.Cut)

    def copyaction(self):
        self.triggerAction(self.Copy)

    def pasteaction(self):
        self.triggerAction(self.Paste)

    def exitfs(self):
        self.triggerAction(self.ExitFullScreen)

    def makefullscreen(self, request):
        if request.toggleOn():
            self.fullView = QWebEngineView()
            self.exitFSAction = QAction(self.fullView)
            self.exitFSAction.setShortcut(Qt.Key_Escape)
            self.exitFSAction.triggered.connect(self.exitfs)

            self.fullView.addAction(self.exitFSAction)
            self.setView(self.fullView)
            self.fullView.showFullScreen()
            self.fullView.raise_()
        else:
            del self.fullView
            self.setView(self.view)
        request.accept()
