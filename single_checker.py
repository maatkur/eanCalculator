import sys
from PySide6.QtWidgets import *
from PySide6 import QtCore
from PyQt6.QtWidgets import QMessageBox
from eanCalculatorGui import Ui_MainWindow
from checker import ean_validation


class Ui_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Validador EAN")
        self.ean_receiver.installEventFilter(self)
        self.ean_checker.installEventFilter(self)
        self.validation_button.installEventFilter(self)
        self.new_validation.installEventFilter(self)
        self.validation_button.clicked.connect(self.set_field_info)
        self.new_validation.clicked.connect(self.clean_fields)

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
                if widget == self.ean_receiver:
                    self.set_field_info()

    def set_field_info(self):
        ean = ean_validation(self.ean_receiver.text())
        self.ean_checker.setText(ean)

        if self.ean_receiver.text() == self.ean_checker.text():
            self.ean_checker.setStyleSheet('background: green; '
                                           'color:white;'
                                           )
        else:
            self.ean_checker.setStyleSheet('color: red')

    def clean_fields(self):
        self.ean_checker.setText("")
        self.ean_receiver.setText("")
        self.ean_checker.setStyleSheet('color: white')

#7894200156161
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    app.exec()