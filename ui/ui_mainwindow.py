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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1654, 845)
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

        self.folderViewer = QListView(self.centralwidget)
        self.folderViewer.setObjectName(u"folderViewer")

        self.verticalLayout.addWidget(self.folderViewer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.ruleLayout = QVBoxLayout()
        self.ruleLayout.setObjectName(u"ruleLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.ruleLayout.addWidget(self.label)

        self.ruleBtnViewer = QHBoxLayout()
        self.ruleBtnViewer.setObjectName(u"ruleBtnViewer")
        self.deleteRuleBtn = QPushButton(self.centralwidget)
        self.deleteRuleBtn.setObjectName(u"deleteRuleBtn")

        self.ruleBtnViewer.addWidget(self.deleteRuleBtn)

        self.addRuleBtn = QPushButton(self.centralwidget)
        self.addRuleBtn.setObjectName(u"addRuleBtn")

        self.ruleBtnViewer.addWidget(self.addRuleBtn)


        self.ruleLayout.addLayout(self.ruleBtnViewer)

        self.ruleViewer = QListWidget(self.centralwidget)
        self.ruleViewer.setObjectName(u"ruleViewer")

        self.ruleLayout.addWidget(self.ruleViewer)


        self.horizontalLayout.addLayout(self.ruleLayout)

        self.ruleEditor = QGroupBox(self.centralwidget)
        self.ruleEditor.setObjectName(u"ruleEditor")
        self.verticalLayout_3 = QVBoxLayout(self.ruleEditor)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ruleNameViewer = QHBoxLayout()
        self.ruleNameViewer.setObjectName(u"ruleNameViewer")
        self.ruleNameLabel = QLabel(self.ruleEditor)
        self.ruleNameLabel.setObjectName(u"ruleNameLabel")

        self.ruleNameViewer.addWidget(self.ruleNameLabel)

        self.ruleNameEdit = QLineEdit(self.ruleEditor)
        self.ruleNameEdit.setObjectName(u"ruleNameEdit")

        self.ruleNameViewer.addWidget(self.ruleNameEdit)


        self.verticalLayout_3.addLayout(self.ruleNameViewer)

        self.ifLabel = QLabel(self.ruleEditor)
        self.ifLabel.setObjectName(u"ifLabel")

        self.verticalLayout_3.addWidget(self.ifLabel)

        self.ifViewer = QGroupBox(self.ruleEditor)
        self.ifViewer.setObjectName(u"ifViewer")
        self.horizontalLayout_3 = QHBoxLayout(self.ifViewer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ruleComboBox = QComboBox(self.ifViewer)
        self.ruleComboBox.addItem("")
        self.ruleComboBox.addItem("")
        self.ruleComboBox.setObjectName(u"ruleComboBox")

        self.horizontalLayout_3.addWidget(self.ruleComboBox)

        self.verbComboBox = QComboBox(self.ifViewer)
        self.verbComboBox.addItem("")
        self.verbComboBox.addItem("")
        self.verbComboBox.addItem("")
        self.verbComboBox.setObjectName(u"verbComboBox")

        self.horizontalLayout_3.addWidget(self.verbComboBox)

        self.lineEdit = QLineEdit(self.ifViewer)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_3.addWidget(self.ifViewer)

        self.thenLabel = QLabel(self.ruleEditor)
        self.thenLabel.setObjectName(u"thenLabel")

        self.verticalLayout_3.addWidget(self.thenLabel)

        self.thenGroupBox = QGroupBox(self.ruleEditor)
        self.thenGroupBox.setObjectName(u"thenGroupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.thenGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.actionComboBox = QComboBox(self.thenGroupBox)
        self.actionComboBox.addItem("")
        self.actionComboBox.setObjectName(u"actionComboBox")

        self.horizontalLayout_2.addWidget(self.actionComboBox)

        self.toFolderLabel = QLabel(self.thenGroupBox)
        self.toFolderLabel.setObjectName(u"toFolderLabel")

        self.horizontalLayout_2.addWidget(self.toFolderLabel)

        self.destBtn = QPushButton(self.thenGroupBox)
        self.destBtn.setObjectName(u"destBtn")

        self.horizontalLayout_2.addWidget(self.destBtn)


        self.verticalLayout_3.addWidget(self.thenGroupBox)

        self.applyViewer = QHBoxLayout()
        self.applyViewer.setObjectName(u"applyViewer")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.applyViewer.addItem(self.horizontalSpacer)

        self.applyBtn = QPushButton(self.ruleEditor)
        self.applyBtn.setObjectName(u"applyBtn")

        self.applyViewer.addWidget(self.applyBtn)


        self.verticalLayout_3.addLayout(self.applyViewer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.ruleEditor)

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
        self.deleteRuleBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.addRuleBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.ruleNameLabel.setText(QCoreApplication.translate("MainWindow", u"Rule name:", None))
        self.ifLabel.setText(QCoreApplication.translate("MainWindow", u"If any of the following conditions are met:", None))
        self.ruleComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"File", None))
        self.ruleComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Extension", None))

        self.verbComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"contains", None))
        self.verbComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"is", None))
        self.verbComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"begins with", None))

        self.thenLabel.setText(QCoreApplication.translate("MainWindow", u"Do the following to the matched folder:", None))
        self.actionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Move", None))

        self.toFolderLabel.setText(QCoreApplication.translate("MainWindow", u"to folder:", None))
        self.destBtn.setText(QCoreApplication.translate("MainWindow", u"Choose Folder", None))
        self.applyBtn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
    # retranslateUi

