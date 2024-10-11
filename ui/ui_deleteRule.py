# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(313, 101)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.deleteMsgLabel = QLabel(Dialog)
        self.deleteMsgLabel.setObjectName(u"deleteMsgLabel")

        self.verticalLayout.addWidget(self.deleteMsgLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelDeleteBtn = QPushButton(Dialog)
        self.cancelDeleteBtn.setObjectName(u"cancelDeleteBtn")

        self.horizontalLayout.addWidget(self.cancelDeleteBtn)

        self.confirmDeleteBtn = QPushButton(Dialog)
        self.confirmDeleteBtn.setObjectName(u"confirmDeleteBtn")

        self.horizontalLayout.addWidget(self.confirmDeleteBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.deleteMsgLabel.setText(QCoreApplication.translate("Dialog", u"Are you sure you want to delete {ruleName}?", None))
        self.cancelDeleteBtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.confirmDeleteBtn.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
    # retranslateUi

