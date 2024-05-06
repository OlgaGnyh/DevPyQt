import sys

from PySide6 import QtWidgets
from main_window import MainWindow


# class MainWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Основное окно')
#         self.resize(300, 200)


app = QtWidgets.QApplication()

window = MainWindow()
window.show()

app.exec()
