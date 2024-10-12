# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rule.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(299, 76)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.rule = QCheckBox(Form)
        self.rule.setObjectName(u"rule")
        font = QFont()
        font.setPointSize(12)
        self.rule.setFont(font)

        self.gridLayout.addWidget(self.rule, 0, 0, 1, 1)

        self.editRuleBtn = QPushButton(Form)
        self.editRuleBtn.setObjectName(u"editRuleBtn")
        self.editRuleBtn.setMaximumSize(QSize(32, 48))
        font1 = QFont()
        font1.setPointSize(10)
        self.editRuleBtn.setFont(font1)
        self.editRuleBtn.setStyleSheet(u"")
        self.editRuleBtn.setFlat(False)

        self.gridLayout.addWidget(self.editRuleBtn, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.rule.setText(QCoreApplication.translate("Form", u"ruleName", None))
        self.editRuleBtn.setText(QCoreApplication.translate("Form", u"edit", None))
    # retranslateUi

