from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QIcon
from PySide6.QtCore import QUrl
from urllib.parse import urlparse
import src.toolbar as toolbar
from src.palette import palette
import sys
import os
import requests

class BrowserTab(QWebEngineView):
    def __init__(self,url="web/newtab.html"):
        super().__init__()
        if not QUrl(url).isLocalFile():
            url = os.path.abspath(url)
            url = QUrl.fromLocalFile(url)
        else:
            url = QUrl(url)
        self.setUrl(url)
        profile = self.page().profile()
        profile.downloadRequested.connect(self.handle_download)

    def handle_download(self,download):
        suggested_name = download.downloadFileName()
        path, _ = QFileDialog.getSaveFileName(self,"Save file as:",suggested_name)
        if path:
            download.setDownloadFileName(path)
            download.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SearcherWeb")
        self.setGeometry(100,100,1050,700)
        self.setWindowIcon(QIcon("images/icon.png"))

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QTabWidget::pane {
                background-color: #ffffff;
            }
            QTabBar::tab:!last {
                background-color: #e0e0e0;
                padding: 5px;
                width: 100px;
                border: 1px solid #d0d0d0;
                border-top-left-radius: 12px;
                border-top-right-radius: 12px;
                text-align: left;
            }
            QTabBar::tab:last {
                background-color: #ffffff;
                padding: 5px;
                width: 16px;
                height: 16px;
                border-radius: 8 8 0 0px;
                margin-left: 2.5px;
                margin-top: 2.5px;
                text-align: right;
            }
            QTabBar::tab:last:hover {
                background-color: #ddd;
            }
            QTabBar::tab:last:pressed {
                background-color: #ccc;
            }
            QTabBar::tab:selected:!last {
                background-color: #ffffff;
                border-bottom: 1px solid #ffffff;
            }""")

        self.tabs = QTabWidget(tabsClosable=True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_title)

        self.new_tab_button = QPushButton("    +",flat=True)
        self.new_tab_button.setFixedWidth(30)
        self.new_tab_button.clicked.connect(lambda: self.add_new_tab())

        self.tabs.addTab(QWidget(),"")
        self.tabs.tabBar().setTabButton(self.tabs.count()-1,QTabBar.RightSide,self.new_tab_button)
        self.tabs.currentChanged.connect(lambda _: self.ensure_plus_tab())

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.tabs)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.add_new_tab()
        toolbar.add_toolbar(self)

    def ensure_plus_tab(self):
        if self.tabs.tabText(self.tabs.count()-1) != "":
            self.tabs.addTab(QWidget(),"")
            self.tabs.tabBar().setTabButton(self.tabs.count()-1,QTabBar.RightSide,self.new_tab_button)
        if self.tabs.currentIndex() == self.tabs.count()-1 and self.tabs.count() > 1:
            self.tabs.setCurrentIndex(self.tabs.count()-2)

    def add_new_tab(self, url="web/newtab.html"):
        try:
            response = requests.get("https://antonfdiaz.github.io/magnesium/version.txt",timeout=3)
            if response.text > "0.7":
                url = "web/update.html"
            if not QUrl(url).isLocalFile():
                url = os.path.abspath(url)
                url = QUrl.fromLocalFile(url)
            else:
                url = QUrl(url)
        except requests.RequestException:
            response = requests.get("https://antonfdiaz.github.io/searcherWeb/version.txt",timeout=3)
            if response.text > "0.7":
                url = "web/update.html"
            if not QUrl(url).isLocalFile():
                url = os.path.abspath(url)
                url = QUrl.fromLocalFile(url)
            else:
                url = QUrl(url)
        if response.status_code != 200:
            QMessageBox.critical(self,"Error","Failed to check for updates.")
        url = "web/newtab.html"
        url = os.path.abspath(url)
        url = QUrl.fromLocalFile(url)
        browser = BrowserTab(url.toString())
        browser.urlChanged.connect(self.url_changed)
        i = self.tabs.insertTab(self.tabs.count() - 1, browser, "New Tab")
        self.tabs.setCurrentIndex(i)
        self.webview = browser

    def close_tab(self, index):
        if self.tabs.tabText(index) == "" or self.tabs.count() <= 2:
            return
        self.tabs.removeTab(index)
        widget = self.tabs.currentWidget()
        if isinstance(widget, BrowserTab):
            self.webview = widget

    def url_changed(self, url):
        browser = self.tabs.currentWidget()
        if not isinstance(browser, BrowserTab): return
        self.webview = browser
        domain = urlparse(url.toString()).netloc or "New Tab"
        self.tabs.setTabText(self.tabs.currentIndex(), domain)
        self.update_title()

    def update_title(self):
        browser = self.tabs.currentWidget()
        if not isinstance(browser, BrowserTab):
            self.setWindowTitle("Magnesium")
            return
        domain = urlparse(browser.url().toString()).netloc
        self.setWindowTitle(f"{domain} - Magnesium" if domain else "Magnesium")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(palette)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())