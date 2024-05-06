import sys
from PySide6 import QtWidgets
from ui.c_ship_parametrs import Ui_MainWindow


class Window(QtWidgets.QMainWindow):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication()

window = Window()
window.show()

sys.exit(app.exec())
