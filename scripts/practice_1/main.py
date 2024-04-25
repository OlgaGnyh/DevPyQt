import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
from main_window import MainWindow
from ui.b_login import Ui_Form

class Window(QtWidgets.QWidget):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_Form()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
# app = QtWidgets.QApplication()

window = Window()
window.show()

sys.exit(app.exec())
