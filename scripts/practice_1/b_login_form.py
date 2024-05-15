import sys
from PySide6 import QtWidgets


class MyMainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        # menuBar отсутствует у QWidgets
        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction("Open")
        self.fileMenu.addAction("New")
        self.fileMenu.addAction("Save")

        # toolBar отсутствует у QWidgets
        self.toolBarFirst = self.addToolBar("First")
        self.toolBarFirst.addAction("Edit_1")
        self.toolBarFirst.addAction("Edit_1_1")

        self.toolBarSec = self.addToolBar("Second")
        self.toolBarSec.addAction("Edit_2")
        self.toolBarSec.addAction("Edit_3")

        # statusBar отсутствует у QWidgets
        self.appStatusBar = self.statusBar()
        self.appStatusBar.showMessage("Status: Ok!")



        label = QtWidgets.QLabel("Login")
        line = QtWidgets.QLineEdit("put login")

        label2 = QtWidgets.QLabel("Password")
        line2 = QtWidgets.QLineEdit("enter password")

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line)

        layout2 = QtWidgets.QHBoxLayout()
        layout2.addWidget(label2)
        layout2.addWidget(line2)

        layout3 = QtWidgets.QVBoxLayout()
        layout3.addLayout(layout)
        layout3.addLayout(layout2)

        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout3)
        self.setCentralWidget(centralWidget)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myWindow = MyMainWindow()
    myWindow.show()

    app.exec()
