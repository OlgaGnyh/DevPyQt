"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets, QtCore, QtGui
import datetime
from scripts.practice_2.ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        self.ui.pushButtonGetData.clicked.connect(lambda: self.setdata())
        self.ui.pushButtonLT.clicked.connect(lambda: self.move(0, 0))
        self.ui.pushButtonLB.clicked.connect(lambda: self.move(0, QtWidgets.QApplication.primaryScreen().size().height() - self.height()))
        self.ui.pushButtonRT.clicked.connect(lambda: self.move(QtWidgets.QApplication.primaryScreen().size().width() - self.width(), 0))
        self.ui.pushButtonRB.clicked.connect(lambda: self.move(QtWidgets.QApplication.primaryScreen().size().width() - self.width(),
                                                               QtWidgets.QApplication.primaryScreen().size().height() - self.height()))
        self.ui.pushButtonCenter.clicked.connect(lambda: self.move((QtWidgets.QApplication.primaryScreen().size().width() - self.width())/2,
                                                                   (QtWidgets.QApplication.primaryScreen().size().height() - self.height())/2))
        self.ui.pushButtonMoveCoords.clicked.connect(lambda: self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value()))

    def setdata(self):
        self.ui.plainTextEdit.setPlainText(
            f'{self.ui.plainTextEdit.toPlainText()}\n'
            f'----------------------------------------\n'
            f'{datetime.datetime.now()}\n'
            f'Экран: {QtWidgets.QApplication.screens()}\n'
            f'Текущее основное окно: {QtWidgets.QApplication.activeWindow()}\n'
            f'Разрешение экрана: ширина: {QtWidgets.QApplication.primaryScreen().size().width()}, высота: {QtWidgets.QApplication.primaryScreen().size().height()}\n'
            f'Окно находится на экране: {self.screen()}\n'
            f'Размеры окна: ширина: {self.width()}, высота: {self.height()}\n'
            f'Минимальные размеры окна: ширина:{self.minimumSize().width()}, высота: {self.minimumSize().height()}\n'
            f'Текущее положение (координаты) окна: x: {self.x()}, y: {self.y()}\n'
            f'Координаты центра приложения: x: {self.width() / 2 + self.x()} , y: {self.height() / 2 + self.y()}\n'
            f'Состояния окна: {self.windowState()}\n')

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        print(self.x(), self.y())
        print(self.size())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
