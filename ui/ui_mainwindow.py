# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(401, 484)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ruleLayout = QVBoxLayout()
        self.ruleLayout.setObjectName(u"ruleLayout")
        self.rulesTitle = QLabel(self.centralwidget)
        self.rulesTitle.setObjectName(u"rulesTitle")
        font = QFont()
        font.setPointSize(16)
        self.rulesTitle.setFont(font)
        self.rulesTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ruleLayout.addWidget(self.rulesTitle)

        self.ruleView = QListView(self.centralwidget)
        self.ruleView.setObjectName(u"ruleView")

        self.ruleLayout.addWidget(self.ruleView)

        self.ruleBtnViewer = QHBoxLayout()
        self.ruleBtnViewer.setObjectName(u"ruleBtnViewer")
        self.deleteRuleBtn = QPushButton(self.centralwidget)
        self.deleteRuleBtn.setObjectName(u"deleteRuleBtn")

        self.ruleBtnViewer.addWidget(self.deleteRuleBtn)

        self.addRuleBtn = QPushButton(self.centralwidget)
        self.addRuleBtn.setObjectName(u"addRuleBtn")

        self.ruleBtnViewer.addWidget(self.addRuleBtn)


        self.ruleLayout.addLayout(self.ruleBtnViewer)


        self.gridLayout.addLayout(self.ruleLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rulesTitle.setText(QCoreApplication.translate("MainWindow", u"File Rules", None))
        self.deleteRuleBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.addRuleBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

