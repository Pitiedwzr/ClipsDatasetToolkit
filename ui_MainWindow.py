# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1420, 775)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.clipsListWidget = QListWidget(self.centralwidget)
        self.clipsListWidget.setObjectName(u"clipsListWidget")
        self.clipsListWidget.setGeometry(QRect(30, 30, 581, 671))
        self.playerWidget = QVideoWidget(self.centralwidget)
        self.playerWidget.setObjectName(u"playerWidget")
        self.playerWidget.setGeometry(QRect(640, 30, 750, 422))
        self.clipsPathLineEdit = QLineEdit(self.centralwidget)
        self.clipsPathLineEdit.setObjectName(u"clipsPathLineEdit")
        self.clipsPathLineEdit.setGeometry(QRect(740, 520, 631, 21))
        self.c1PathLineEdit = QLineEdit(self.centralwidget)
        self.c1PathLineEdit.setObjectName(u"c1PathLineEdit")
        self.c1PathLineEdit.setGeometry(QRect(740, 560, 631, 21))
        self.c2PathLineEdit = QLineEdit(self.centralwidget)
        self.c2PathLineEdit.setObjectName(u"c2PathLineEdit")
        self.c2PathLineEdit.setGeometry(QRect(740, 600, 631, 21))
        self.c3PathLineEdit = QLineEdit(self.centralwidget)
        self.c3PathLineEdit.setObjectName(u"c3PathLineEdit")
        self.c3PathLineEdit.setGeometry(QRect(740, 640, 631, 21))
        self.c4PathLineEdit = QLineEdit(self.centralwidget)
        self.c4PathLineEdit.setObjectName(u"c4PathLineEdit")
        self.c4PathLineEdit.setGeometry(QRect(740, 680, 631, 21))
        self.clipsLabel = QLabel(self.centralwidget)
        self.clipsLabel.setObjectName(u"clipsLabel")
        self.clipsLabel.setGeometry(QRect(640, 520, 101, 21))
        self.c1Label = QLabel(self.centralwidget)
        self.c1Label.setObjectName(u"c1Label")
        self.c1Label.setGeometry(QRect(640, 560, 101, 21))
        self.c2Label = QLabel(self.centralwidget)
        self.c2Label.setObjectName(u"c2Label")
        self.c2Label.setGeometry(QRect(640, 600, 101, 21))
        self.c3Label = QLabel(self.centralwidget)
        self.c3Label.setObjectName(u"c3Label")
        self.c3Label.setGeometry(QRect(640, 640, 101, 21))
        self.c4Label = QLabel(self.centralwidget)
        self.c4Label.setObjectName(u"c4Label")
        self.c4Label.setGeometry(QRect(640, 680, 101, 21))
        self.clipsPathButton = QPushButton(self.centralwidget)
        self.clipsPathButton.setObjectName(u"clipsPathButton")
        self.clipsPathButton.setGeometry(QRect(1370, 520, 21, 21))
        self.c1PathButton = QPushButton(self.centralwidget)
        self.c1PathButton.setObjectName(u"c1PathButton")
        self.c1PathButton.setGeometry(QRect(1370, 560, 21, 21))
        self.c2PathButton = QPushButton(self.centralwidget)
        self.c2PathButton.setObjectName(u"c2PathButton")
        self.c2PathButton.setGeometry(QRect(1370, 600, 21, 21))
        self.c3PathButton = QPushButton(self.centralwidget)
        self.c3PathButton.setObjectName(u"c3PathButton")
        self.c3PathButton.setGeometry(QRect(1370, 640, 21, 21))
        self.c4PathButton = QPushButton(self.centralwidget)
        self.c4PathButton.setObjectName(u"c4PathButton")
        self.c4PathButton.setGeometry(QRect(1370, 680, 21, 21))
        self.timerFloatBox = QDoubleSpinBox(self.centralwidget)
        self.timerFloatBox.setObjectName(u"timerFloatBox")
        self.timerFloatBox.setGeometry(QRect(740, 480, 87, 22))
        self.timerLabel = QLabel(self.centralwidget)
        self.timerLabel.setObjectName(u"timerLabel")
        self.timerLabel.setGeometry(QRect(640, 480, 91, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1420, 33))
        self.menuFiles = QMenu(self.menubar)
        self.menuFiles.setObjectName(u"menuFiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CilpsDatasetToolkit", None))
        self.clipsLabel.setText(QCoreApplication.translate("MainWindow", u"Path to clips", None))
        self.c1Label.setText(QCoreApplication.translate("MainWindow", u"Category 1", None))
        self.c2Label.setText(QCoreApplication.translate("MainWindow", u"Category 2", None))
        self.c3Label.setText(QCoreApplication.translate("MainWindow", u"Category 3", None))
        self.c4Label.setText(QCoreApplication.translate("MainWindow", u"Category 4", None))
        self.clipsPathButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.c1PathButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.c2PathButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.c3PathButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.c4PathButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.timerLabel.setText(QCoreApplication.translate("MainWindow", u"Wait Seconds", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
    # retranslateUi

