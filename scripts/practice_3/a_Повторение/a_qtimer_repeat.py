"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtCore
from time import sleep

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QtCore.QTimer
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.long_proc)
        self.timer.start()

    def long_proc(self):
        sleep(0.5)
        print('Прошла секунда')




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
