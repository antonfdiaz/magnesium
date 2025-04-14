from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
import src.config
import webbrowser

class InputDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)

        QBtn = (
            QDialogButtonBox.Ok|QDialogButtonBox.Cancel
        )

        self.setWindowTitle("Change")
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.change)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Type an URL in the box below:")
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Type an URL...")
        layout.addWidget(message)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
    def change(self):
        src.config.home_url = self.line_edit.text()
        print(src.config.home_url)
        self.accept()

def show_about():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("About")
    msg_box.setText(
        "SearcherWeb\n\nA simple Python web browser."
    )
    msg_box.setIcon(QMessageBox.Information)
    logo = QPixmap("images/icon.png")
    msg_box.setIconPixmap(logo)
    msg_box.setStandardButtons(QMessageBox.Ok|QMessageBox.Help)
    msg_box.button(QMessageBox.Help).setText("Learn More")
    def on_learn_more():
        webbrowser.open("http://antonfdiaz.github.io/searcherWeb/web/index.html")
    msg_box.button(QMessageBox.Help).clicked.connect(on_learn_more)
    msg_box.exec()

def change_home(self):
    dlg = InputDialog(self)
    if dlg.exec():
        return True
    else:
        return False

if __name__ == "__main__":
    app = QApplication([])
    show_about()