"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtGui, QtCore
from scripts.practice_2.ui.d_eventfilter_settings_form import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QtCore.QSettings("value")
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        value = self.settings.value('value', [])
        self.ui.lcdNumber.display(int(value))
        self.ui.dial.setValue(int(value))
        self.ui.horizontalSlider.setValue(int(value))

        self.ui.dial.valueChanged.connect(lambda: self.ui.lcdNumber.display(self.ui.dial.value()))
        self.ui.dial.valueChanged.connect(lambda: self.ui.horizontalSlider.setValue(self.ui.dial.value()))
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.ui.lcdNumber.display(self.ui.horizontalSlider.value()))
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.ui.dial.setValue(self.ui.horizontalSlider.value()))

        self.ui.comboBox.addItem('oct')
        self.ui.comboBox.addItem('hex')
        self.ui.comboBox.addItem('bin')
        self.ui.comboBox.addItem('dec')

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.text() == '+':
            self.ui.dial.setValue(int(self.ui.dial.value()) + 1)
        if event.text() == '-':
            self.ui.dial.setValue(int(self.ui.dial.value()) - 1)
        print(self.ui.dial.value())

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.settings.setValue('value', self.ui.lcdNumber.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
