from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
import webbrowser
import requests

def show_about():
    updated = True
    response = requests.get("https://antonfdiaz.github.io/magnesium/version.txt",timeout=3)
    if float(response.text) > 0.9:
        updated = False

    msg_box = QMessageBox()
    msg_box.setWindowTitle("About")
    if updated:
        msg_box.setText(
            "Magnesium\n\nA simple Python web browser.\n\nVersion 0.8. Magnesium is updated."
        )
    else:
        msg_box.setText(
            "Magnesium\n\nA simple Python web browser.\n\nVersion 0.8. Magnesium is not updated."
        )

    msg_box.setIcon(QMessageBox.Information)
    logo = QPixmap("images/icon.png")
    msg_box.setIconPixmap(logo)
    msg_box.setStandardButtons(QMessageBox.Ok|QMessageBox.Help)
    msg_box.button(QMessageBox.Help).setText("Learn More")
    
    def on_learn_more():
        webbrowser.open("http://antonfdiaz.github.io/magnesium/web/index.html")
    msg_box.button(QMessageBox.Help).clicked.connect(on_learn_more)

    msg_box.exec()

if __name__ == "__main__":
    app = QApplication([])
    show_about()