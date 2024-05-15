"""
Файл для повторения темы генерации сигналов и передачи данных из одного виджета в другой

Напомнить про работу с пользовательскими сигналами.

Предлагается создать 2 формы:
* На первый форме label с надписью "Пройдите регистрацию" и pushButton с текстом "Зарегистрироваться"
* На второй (QDialog) форме:
  * lineEdit с placeholder'ом "Введите логин"
  * lineEdit с placeholder'ом "Введите пароль"
  * pushButton "Зарегистрироваться"

  при нажатии на кнопку, данные из lineEdit'ов передаются в главное окно, в
  котором надпись "Пройдите регистрацию", меняется на "Добро пожаловать {данные из lineEdit с логином}"
  (пароль можно показать в терминале в захешированном виде)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initchildwindow()
        self.initSignals()

    def initUi(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.labelreg = QtWidgets.QLabel("Пройдите регистрацию")
        self.pushbuttonreg = QtWidgets.QPushButton("Зарегистрироваться")
        main_layout.addWidget(self.labelreg)
        main_layout.addWidget(self.pushbuttonreg)
        self.setLayout(main_layout)

    def initSignals(self):
        self.pushbuttonreg.clicked.connect(self.childwindow.show)
        self.childwindow.user_signal.connect(self.childwindowsignalActivated)

    def initchildwindow(self):
        self.childwindow = OtherWindow()

    def childwindowsignalActivated(self, text):
        self.labelreg.setText(text)


class OtherWindow(QtWidgets.QDialog):
    user_signal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        self.lineeditlog = QtWidgets.QLineEdit()
        self.lineeditlog.setPlaceholderText("Введите логин")
        self.lineeditpas = QtWidgets.QLineEdit()
        self.lineeditpas.setPlaceholderText("Введите пароль")
        self.lineeditpas.setEchoMode(self.lineeditpas.EchoMode.Password)
        self.pushButtonzareg = QtWidgets.QPushButton("Зарегистрироваться")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineeditlog)
        layout.addWidget(self.lineeditpas)
        layout.addWidget(self.pushButtonzareg)
        self.setLayout(layout)

        self.pushButtonzareg.clicked.connect(self.changedLineEditText)

    def changedLineEditText(self) -> None:
        self.user_signal.emit(f"Добро пожаловать {self.lineeditlog.text()}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
