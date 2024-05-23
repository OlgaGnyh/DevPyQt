"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets
import a_threads


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QHBoxLayout()
        self.labelTime = QtWidgets.QLabel('Время задержки')
        self.lineEditTime = QtWidgets.QLineEdit()
        layout.addWidget(self.labelTime)
        layout.addWidget(self.lineEditTime)

        layout2 = QtWidgets.QHBoxLayout()
        self.labelCPU = QtWidgets.QLabel('Загрузка CPU')
        self.lineEditCPU = QtWidgets.QLineEdit()
        layout2.addWidget(self.labelCPU)
        layout2.addWidget(self.lineEditCPU)

        layout3 = QtWidgets.QHBoxLayout()
        self.labelRAM = QtWidgets.QLabel('Загрузка RAM')
        self.lineEditRAM = QtWidgets.QLineEdit()
        layout3.addWidget(self.labelRAM)
        layout3.addWidget(self.lineEditRAM)

        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addLayout(layout)
        mainlayout.addLayout(layout2)
        mainlayout.addLayout(layout3)

        self.setLayout(mainlayout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
