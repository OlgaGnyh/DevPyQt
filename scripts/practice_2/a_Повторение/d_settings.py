"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.savedtexttt_settings = QtCore.QSettings("text")
        self.initUi()

    def initUi(self):
        layout = QtWidgets.QVBoxLayout()

        savedtexttt = self.savedtexttt_settings.value("text", [])

        self.texttt = QtWidgets.QPlainTextEdit()
        self.texttt.setPlainText(str(savedtexttt))

        layout.addWidget(self.texttt)
        self.setLayout(layout)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.savedtexttt_settings.setValue("text", self.texttt.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

