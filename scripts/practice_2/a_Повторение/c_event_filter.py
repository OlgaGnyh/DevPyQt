"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.qlabel = QtWidgets.QLabel('<A style="color:red">Красивая</A> <B style="color:blue">кнопка</B>')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.qlabel)

        self.setLayout(layout)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:

        self.qlabel.setText("mousePressEvent")

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:

        self.qlabel.setText("mouseReleaseEvent")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
