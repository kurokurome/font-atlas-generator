# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledRpyITM.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QAbstractSpinBox, QFrame, QLabel, QPushButton,
                               QSpinBox, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(840, 590)
        MainWindow.setMinimumSize(QSize(840, 590))
        MainWindow.setMaximumSize(QSize(840, 590))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.MainContent = QWidget(MainWindow)
        self.MainContent.setObjectName(u"MainContent")
        self.MainContent.setStyleSheet(u"")
        self.OpenOutputFolderButton = QPushButton(self.MainContent)
        self.OpenOutputFolderButton.setObjectName(u"OpenOutputFolderButton")
        self.OpenOutputFolderButton.setGeometry(QRect(30, 480, 201, 41))
        self.OpenOutputFolderButton.setAutoFillBackground(False)
        self.OpenOutputFolderButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(40, 40, 40); \n"
"color: white; \n"
"border-radius: 15;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"}")
        self.FontFrame = QFrame(self.MainContent)
        self.FontFrame.setObjectName(u"FontFrame")
        self.FontFrame.setGeometry(QRect(10, 10, 240, 330))
        self.FontFrame.setStyleSheet(u"background-color: rgb(63, 63, 63);\n"
"border-radius: 20px;")
        self.FontFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.FontFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.FontFrame.setLineWidth(1)
        self.FontFrame.setMidLineWidth(0)
        self.SettingsLabel = QLabel(self.FontFrame)
        self.SettingsLabel.setObjectName(u"SettingsLabel")
        self.SettingsLabel.setGeometry(QRect(20, 10, 201, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(16)
        font.setBold(False)
        self.SettingsLabel.setFont(font)
        self.SettingsLabel.setAutoFillBackground(False)
        self.SettingsLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.SettingsLabel.setFrameShape(QFrame.Shape.Box)
        self.SettingsLabel.setFrameShadow(QFrame.Shadow.Plain)
        self.SettingsLabel.setLineWidth(1)
        self.SettingsLabel.setTextFormat(Qt.TextFormat.AutoText)
        self.SettingsLabel.setScaledContents(False)
        self.SettingsLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.SettingsLabel.setMargin(0)
        self.SeparatorLine_2 = QFrame(self.FontFrame)
        self.SeparatorLine_2.setObjectName(u"SeparatorLine_2")
        self.SeparatorLine_2.setGeometry(QRect(10, 50, 221, 2))
        self.SeparatorLine_2.setMaximumSize(QSize(221, 5))
        self.SeparatorLine_2.setAutoFillBackground(False)
        self.SeparatorLine_2.setStyleSheet(u"background-color: rgb(23, 22, 28);")
        self.SeparatorLine_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.SeparatorLine_2.setLineWidth(0)
        self.SeparatorLine_2.setFrameShape(QFrame.Shape.HLine)
        self.FontSizeLabel = QLabel(self.FontFrame)
        self.FontSizeLabel.setObjectName(u"FontSizeLabel")
        self.FontSizeLabel.setGeometry(QRect(20, 140, 191, 21))
        font1 = QFont()
        font1.setPointSize(9)
        self.FontSizeLabel.setFont(font1)
        self.FontSizeLabel.setStyleSheet(u"color: white;")
        self.FontPaddingLabel = QLabel(self.FontFrame)
        self.FontPaddingLabel.setObjectName(u"FontPaddingLabel")
        self.FontPaddingLabel.setGeometry(QRect(20, 230, 191, 21))
        self.FontPaddingLabel.setFont(font1)
        self.FontPaddingLabel.setStyleSheet(u"color: white;")
        self.FontSize = QSpinBox(self.FontFrame)
        self.FontSize.setObjectName(u"FontSize")
        self.FontSize.setGeometry(QRect(20, 170, 91, 41))
        self.FontSize.setFont(font1)
        self.FontSize.setStyleSheet(u"QSpinBox{\n"
"border-color: rgb(255, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(62, 58, 122);\n"
"background-color: rgb(40, 40, 40);\n"
"border-radius: 10;\n"
"border: 1px solid rgb(63, 63, 63);\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"}\n"
"")
        self.FontSize.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FontSize.setReadOnly(False)
        self.FontSize.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.FontSize.setMinimum(24)
        self.FontSize.setMaximum(150)
        self.FontSize.setValue(48)
        self.FontPaddingSize = QSpinBox(self.FontFrame)
        self.FontPaddingSize.setObjectName(u"FontPaddingSize")
        self.FontPaddingSize.setGeometry(QRect(20, 260, 91, 41))
        self.FontPaddingSize.setFont(font1)
        self.FontPaddingSize.setStyleSheet(u"QSpinBox{\n"
"border-color: rgb(255, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(62, 58, 122);\n"
"background-color: rgb(40, 40, 40);\n"
"border-radius: 10;\n"
"border: 1px solid rgb(63, 63, 63);\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"}")
        self.FontPaddingSize.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FontPaddingSize.setReadOnly(False)
        self.FontPaddingSize.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.FontPaddingSize.setMinimum(1)
        self.FontPaddingSize.setMaximum(10)
        self.FontPaddingSize.setValue(4)
        self.SelectFontButton = QPushButton(self.FontFrame)
        self.SelectFontButton.setObjectName(u"SelectFontButton")
        self.SelectFontButton.setGeometry(QRect(20, 70, 201, 41))
        self.SelectFontButton.setFont(font1)
        self.SelectFontButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(40, 40, 40); \n"
"color: white; \n"
"border-radius: 15;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"}\n"
"")
        self.ProcessFrame = QFrame(self.MainContent)
        self.ProcessFrame.setObjectName(u"ProcessFrame")
        self.ProcessFrame.setGeometry(QRect(10, 350, 241, 231))
        self.ProcessFrame.setStyleSheet(u"background-color: rgb(63, 63, 63);\n"
"border-radius: 20px;")
        self.ProcessFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.ProcessFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.SeparatorLine = QFrame(self.ProcessFrame)
        self.SeparatorLine.setObjectName(u"SeparatorLine")
        self.SeparatorLine.setGeometry(QRect(10, 180, 221, 2))
        self.SeparatorLine.setMaximumSize(QSize(221, 5))
        self.SeparatorLine.setAutoFillBackground(False)
        self.SeparatorLine.setStyleSheet(u"background-color: rgb(23, 22, 28);")
        self.SeparatorLine.setFrameShadow(QFrame.Shadow.Sunken)
        self.SeparatorLine.setLineWidth(0)
        self.SeparatorLine.setFrameShape(QFrame.Shape.HLine)
        self.ExportButton = QPushButton(self.ProcessFrame)
        self.ExportButton.setObjectName(u"ExportButton")
        self.ExportButton.setGeometry(QRect(20, 60, 201, 41))
        self.ExportButton.setFont(font1)
        self.ExportButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(40, 40, 40); \n"
"color: white; \n"
"border-radius: 15;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"}\n"
"")
        self.GenerateButton = QPushButton(self.ProcessFrame)
        self.GenerateButton.setObjectName(u"GenerateButton")
        self.GenerateButton.setGeometry(QRect(20, 10, 201, 41))
        self.GenerateButton.setFont(font1)
        self.GenerateButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(40, 40, 40); \n"
"color: white; \n"
"border-radius: 15;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"}\n"
"")
        self.ExitButton = QPushButton(self.ProcessFrame)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setGeometry(QRect(160, 190, 61, 31))
        self.ExitButton.setFont(font1)
        self.ExitButton.setAutoFillBackground(False)
        self.ExitButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(40, 40, 40); \n"
"color: white; \n"
"border-radius: 15;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(25, 25, 25);\n"
"}\n"
"")
        self.ExitButton.setAutoDefault(True)
        self.ExitButton.setFlat(False)
        self.PreviewFrame = QFrame(self.MainContent)
        self.PreviewFrame.setObjectName(u"PreviewFrame")
        self.PreviewFrame.setGeometry(QRect(260, 10, 571, 571))
        self.PreviewFrame.setStyleSheet(u"background-color: rgb(63, 63, 63);\n"
"border-radius: 20px;")
        self.PreviewFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PreviewFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.Preview = QLabel(self.MainContent)
        self.Preview.setObjectName(u"Preview")
        self.Preview.setGeometry(QRect(290, 40, 512, 512))
        font2 = QFont()
        font2.setPointSize(12)
        self.Preview.setFont(font2)
        self.Preview.setFrameShape(QFrame.Shape.Box)
        self.Preview.setFrameShadow(QFrame.Shadow.Plain)
        self.Preview.setLineWidth(1)
        self.Preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Background = QFrame(self.MainContent)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 841, 591))
        self.Background.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.Background.setFrameShape(QFrame.Shape.StyledPanel)
        self.Background.setFrameShadow(QFrame.Shadow.Raised)
        MainWindow.setCentralWidget(self.MainContent)
        self.Background.raise_()
        self.FontFrame.raise_()
        self.ProcessFrame.raise_()
        self.OpenOutputFolderButton.raise_()
        self.PreviewFrame.raise_()
        self.Preview.raise_()

        self.retranslateUi(MainWindow)

        self.ExitButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Atlas Generator", None))
        self.OpenOutputFolderButton.setText(QCoreApplication.translate("MainWindow", u"Open Output Folder", None))
        self.SettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.FontSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Font Size:", None))
        self.FontPaddingLabel.setText(QCoreApplication.translate("MainWindow", u"Font Padding:", None))
        self.FontSize.setSpecialValueText("")
        self.FontSize.setSuffix(QCoreApplication.translate("MainWindow", u"px", None))
        self.FontSize.setPrefix("")
        self.FontPaddingSize.setSpecialValueText("")
        self.FontPaddingSize.setSuffix(QCoreApplication.translate("MainWindow", u"px", None))
        self.FontPaddingSize.setPrefix("")
        self.SelectFontButton.setText(QCoreApplication.translate("MainWindow", u"Select Font", None))
        self.ExportButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.GenerateButton.setText(QCoreApplication.translate("MainWindow", u"Generate Atlas", None))
        self.ExitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.Preview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
    # retranslateUi

