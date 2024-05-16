"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

from PySide6 import QtWidgets, QtCore
from time import sleep

class Worker(QtCore.QThread):
    progress = QtCore.Signal(list)
    def run(self):
        for i in range(10):
            sleep(1)
            print(i)
            self.progress.emit([i, 'message'])


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(500, 500, 300, 200)
        self.label = QtWidgets.QLabel('text')
        self.button = QtWidgets.QPushButton('push')
        self.line = QtWidgets.QLineEdit()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.work = Worker()
        self.button.clicked.connect(self.start_tread)
        self.work.progress.connect(self.set_data_in_label)
        # self.work.progress.connect(lambda data: self.label.setText(str(data[0])))

    def set_data_in_label(self, data):
        self.label.setText(str(data[0]))


    def start_tread(self):
        self.work.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
