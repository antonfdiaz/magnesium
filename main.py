from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import *
from PySide6.QtCore import *
import src.toolbar as toolbar
from src.palette import palette
from urllib.parse import urlparse
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SearcherWeb")
        self.setGeometry(100,100,1050,700)
        icon = QIcon()
        icon.addFile("images/icon.png")
        self.setWindowIcon(icon)
        self.webview = QWebEngineView()
        self.webview.setUrl("https://www.google.com")
        self.webview.urlChanged.connect(self.url_changed)
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.webview)
        widget = QWidget()
        widget.setLayout(layout)
        toolbar.add_toolbar(self)
        self.setCentralWidget(widget)
    def url_changed(self,url):
        self.old_url = url
        domain = urlparse(url.toString()).netloc
        if domain:
            self.setWindowTitle(f"{domain} - SearcherWeb")
        else:
            self.setWindowTitle("SearcherWeb")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(palette)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())