# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(353, 213)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_C = QPushButton(Form)
        self.pushButton_C.setObjectName(u"pushButton_C")

        self.horizontalLayout.addWidget(self.pushButton_C)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_plus = QPushButton(Form)
        self.pushButton_plus.setObjectName(u"pushButton_plus")

        self.horizontalLayout_2.addWidget(self.pushButton_plus)

        self.pushButton_minus = QPushButton(Form)
        self.pushButton_minus.setObjectName(u"pushButton_minus")

        self.horizontalLayout_2.addWidget(self.pushButton_minus)

        self.pushButton_umnogenie = QPushButton(Form)
        self.pushButton_umnogenie.setObjectName(u"pushButton_umnogenie")

        self.horizontalLayout_2.addWidget(self.pushButton_umnogenie)

        self.pushButton_delenie = QPushButton(Form)
        self.pushButton_delenie.setObjectName(u"pushButton_delenie")

        self.horizontalLayout_2.addWidget(self.pushButton_delenie)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_result = QPushButton(Form)
        self.pushButton_result.setObjectName(u"pushButton_result")

        self.verticalLayout.addWidget(self.pushButton_result)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_C.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_plus.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_minus.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_umnogenie.setText(QCoreApplication.translate("Form", u"*", None))
        self.pushButton_delenie.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_result.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi

