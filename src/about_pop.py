from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QPixmap
import webbrowser

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
if __name__ == "__main__":
    app = QApplication([])
    show_about()