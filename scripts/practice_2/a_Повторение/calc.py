
from PySide6 import QtWidgets, QtGui, QtCore
from scripts.practice_2.ui.calc import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setting = QtCore.QSettings('App')
        self.ui.lineEdit.setText(self.setting.value('App', '0'))

        self.ui.pushButton_1.clicked.connect(lambda: self.add_text('1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.add_text('2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.add_text('3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.add_text('4'))
        self.ui.pushButton_5.clicked.connect(lambda: self.add_text('5'))
        self.ui.pushButton_6.clicked.connect(lambda: self.add_text('6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.add_text('7'))
        self.ui.pushButton_8.clicked.connect(lambda: self.add_text('8'))
        self.ui.pushButton_9.clicked.connect(lambda: self.add_text('9'))
        self.ui.pushButton_0.clicked.connect(lambda: self.add_text('0'))
        self.ui.pushButton_plus.clicked.connect(lambda: self.add_text('+'))
        self.ui.pushButton_minus.clicked.connect(lambda: self.add_text('-'))
        self.ui.pushButton_umnogenie.clicked.connect(lambda: self.add_text('*'))
        self.ui.pushButton_delenie.clicked.connect(lambda: self.add_text('/'))
        self.ui.pushButton_result.clicked.connect(self.result)
        self.ui.pushButton_C.clicked.connect(lambda: self.ui.lineEdit.clear())

    def add_text(self, text):
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + text)

    def result(self):
        self.ui.lineEdit.setText(str(eval(self.ui.lineEdit.text())))

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.text() in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+', '*', '/'):
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + event.text())
        elif event.text() in ('=', '\r'):
            self.result
        elif event.key() == QtGui.Qt.Key.Key_Escape:
            self.ui.lineEdit.setText(self.ui.lineEdit.text()[:-1])
        print(event.text())

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.pushButton_result:
            print(f"C кнопкой произошло {event}")

        return super(self).eventFilter(watched, event)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.setting.setValue('App', self.ui.lineEdit.text())
        print('Закрыли приложение')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

