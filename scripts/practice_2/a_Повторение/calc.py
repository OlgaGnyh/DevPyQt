from PySide6 import QtWidgets
from scripts.practice_2.ui.calc import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_1.clicked.connect(self.press_1)
        self.ui.pushButton_2.clicked.connect(self.press_2)
        self.ui.pushButton_3.clicked.connect(self.press_3)
        self.ui.pushButton_plus.clicked.connect(self.press_plus)
        self.ui.pushButton_result.clicked.connect(self.result)

    def press_1(self):
        line = self.ui.lineEdit.text()
        line += '1'
        self.ui.lineEdit.setText(line)

    def press_2(self):
        line = self.ui.lineEdit.text()
        line += '2'
        self.ui.lineEdit.setText(line)

    def press_3(self):
        line = self.ui.lineEdit.text()
        line += '3'
        self.ui.lineEdit.setText(line)

    def press_plus(self):
        line = self.ui.lineEdit.text()
        line += '+'
        self.ui.lineEdit.setText(line)


    def result(self):
        line = self.ui.lineEdit.text()
        if line.find('+'):
            list = line.split('+')
            result = int(list[0]) + int(list[1])
            self.ui.lineEdit.setText(str(result))



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

