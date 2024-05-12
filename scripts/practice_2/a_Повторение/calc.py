
from PySide6 import QtWidgets
from scripts.practice_2.ui.calc import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_1.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'4'))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'5'))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'7'))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'8'))
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'9'))
        self.ui.pushButton_0.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'0'))
        self.ui.pushButton_plus.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'+'))
        self.ui.pushButton_minus.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'-'))
        self.ui.pushButton_umnogenie.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'*'))
        self.ui.pushButton_delenie.clicked.connect(lambda: self.ui.lineEdit.setText(self.ui.lineEdit.text()+'/'))
        self.ui.pushButton_result.clicked.connect(self.result)
        self.ui.pushButton_C.clicked.connect(lambda: self.ui.lineEdit.clear())

    def result(self):
        line = self.ui.lineEdit.text()
        if '+' in line:
            list = line.split('+')
            result = int(list[0]) + int(list[1])
        elif '-' in line:
            list = line.split('-')
            result = int(list[0]) - int(list[1])
        elif '*' in line:
            list = line.split('*')
            result = int(list[0]) * int(list[1])
        elif '/' in line:
            list = line.split('/')
            result = int(list[0]) / int(list[1])

        return self.ui.lineEdit.setText(str(result))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

