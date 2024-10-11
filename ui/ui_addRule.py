# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addRule.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(595, 455)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ruleEditor = QGroupBox(Dialog)
        self.ruleEditor.setObjectName(u"ruleEditor")
        self.verticalLayout = QVBoxLayout(self.ruleEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ruleNameViewer = QHBoxLayout()
        self.ruleNameViewer.setObjectName(u"ruleNameViewer")
        self.ruleNameLabel = QLabel(self.ruleEditor)
        self.ruleNameLabel.setObjectName(u"ruleNameLabel")

        self.ruleNameViewer.addWidget(self.ruleNameLabel)

        self.ruleNameEdit = QLineEdit(self.ruleEditor)
        self.ruleNameEdit.setObjectName(u"ruleNameEdit")

        self.ruleNameViewer.addWidget(self.ruleNameEdit)


        self.verticalLayout.addLayout(self.ruleNameViewer)

        self.groupBox = QGroupBox(self.ruleEditor)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sourceBtn = QPushButton(self.groupBox)
        self.sourceBtn.setObjectName(u"sourceBtn")

        self.horizontalLayout.addWidget(self.sourceBtn)

        self.folderSourceLabel = QLabel(self.groupBox)
        self.folderSourceLabel.setObjectName(u"folderSourceLabel")
        self.folderSourceLabel.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.folderSourceLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.groupBox)

        self.ifLabel = QLabel(self.ruleEditor)
        self.ifLabel.setObjectName(u"ifLabel")

        self.verticalLayout.addWidget(self.ifLabel)

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


        self.verticalLayout.addWidget(self.ifViewer)

        self.chooseFolderLayout = QHBoxLayout()
        self.chooseFolderLayout.setObjectName(u"chooseFolderLayout")
        self.thenLabel = QLabel(self.ruleEditor)
        self.thenLabel.setObjectName(u"thenLabel")

        self.chooseFolderLayout.addWidget(self.thenLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.chooseFolderLayout.addItem(self.horizontalSpacer_2)

        self.destBtn = QPushButton(self.ruleEditor)
        self.destBtn.setObjectName(u"destBtn")

        self.chooseFolderLayout.addWidget(self.destBtn)


        self.verticalLayout.addLayout(self.chooseFolderLayout)

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

        self.destFolderLabel = QLabel(self.thenGroupBox)
        self.destFolderLabel.setObjectName(u"destFolderLabel")

        self.horizontalLayout_2.addWidget(self.destFolderLabel)


        self.verticalLayout.addWidget(self.thenGroupBox)

        self.applyViewer = QHBoxLayout()
        self.applyViewer.setObjectName(u"applyViewer")

        self.verticalLayout.addLayout(self.applyViewer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.confirmCancelLayout = QHBoxLayout()
        self.confirmCancelLayout.setObjectName(u"confirmCancelLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.confirmCancelLayout.addItem(self.horizontalSpacer_3)

        self.cancelBtn = QPushButton(self.ruleEditor)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.confirmCancelLayout.addWidget(self.cancelBtn)

        self.confirmBtn = QPushButton(self.ruleEditor)
        self.confirmBtn.setObjectName(u"confirmBtn")

        self.confirmCancelLayout.addWidget(self.confirmBtn)


        self.verticalLayout.addLayout(self.confirmCancelLayout)


        self.gridLayout.addWidget(self.ruleEditor, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ruleNameLabel.setText(QCoreApplication.translate("Dialog", u"Rule name:", None))
        self.groupBox.setTitle("")
        self.sourceBtn.setText(QCoreApplication.translate("Dialog", u"Folder Source", None))
        self.folderSourceLabel.setText("")
        self.ifLabel.setText(QCoreApplication.translate("Dialog", u"If any of the following conditions are met:", None))
        self.ruleComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"File", None))
        self.ruleComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Extension", None))

        self.verbComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"contains", None))
        self.verbComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"is", None))
        self.verbComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"begins with", None))

        self.thenLabel.setText(QCoreApplication.translate("Dialog", u"Do the following to the matched folder:", None))
        self.destBtn.setText(QCoreApplication.translate("Dialog", u"Choose Folder", None))
        self.actionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Move", None))

        self.toFolderLabel.setText(QCoreApplication.translate("Dialog", u"to folder:", None))
        self.destFolderLabel.setText("")
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.confirmBtn.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
    # retranslateUi

