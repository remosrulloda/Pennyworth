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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 398)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.folderLabel = QLabel(self.centralwidget)
        self.folderLabel.setObjectName(u"folderLabel")
        font = QFont()
        font.setPointSize(16)
        self.folderLabel.setFont(font)

        self.verticalLayout.addWidget(self.folderLabel)

        self.addFolderBtn = QPushButton(self.centralwidget)
        self.addFolderBtn.setObjectName(u"addFolderBtn")

        self.verticalLayout.addWidget(self.addFolderBtn)

        self.folderView = QListView(self.centralwidget)
        self.folderView.setObjectName(u"folderView")

        self.verticalLayout.addWidget(self.folderView)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.addRule = QPushButton(self.centralwidget)
        self.addRule.setObjectName(u"addRule")

        self.verticalLayout_2.addWidget(self.addRule)

        self.ruleView = QListWidget(self.centralwidget)
        self.ruleView.setObjectName(u"ruleView")

        self.verticalLayout_2.addWidget(self.ruleView)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ruleEditorView = QListWidget(self.centralwidget)
        self.ruleEditorView.setObjectName(u"ruleEditorView")
        self.ruleEditorView.setMinimumSize(QSize(460, 0))

        self.verticalLayout_3.addWidget(self.ruleEditorView)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.folderLabel.setText(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.addFolderBtn.setText(QCoreApplication.translate("MainWindow", u"Add Folder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rules", None))
        self.addRule.setText(QCoreApplication.translate("MainWindow", u"New Rule", None))
    # retranslateUi

