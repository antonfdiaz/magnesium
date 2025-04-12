from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QPixmap

def show_about():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("About")
    msg_box.setText(
        "SearcherWeb\n\nA simple web browser for Mac.\n\n"
        "Website: Coming soon!"
    )
    msg_box.setIcon(QMessageBox.Information)
    logo = QPixmap("images/icon.png")
    msg_box.setIconPixmap(logo)
    msg_box.setStandardButtons(QMessageBox.Ok|QMessageBox.Help)
    msg_box.button(QMessageBox.Help).setText("Learn More")
    msg_box.exec()
if __name__ == "__main__":
    app = QApplication([])
    show_about()