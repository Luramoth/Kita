# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 484)
        self.actionPress_this_for_me_to_say_skrew_u = QAction(MainWindow)
        self.actionPress_this_for_me_to_say_skrew_u.setObjectName(u"actionPress_this_for_me_to_say_skrew_u")
        self.actionWhat = QAction(MainWindow)
        self.actionWhat.setObjectName(u"actionWhat")
        self.actionspitspit = QAction(MainWindow)
        self.actionspitspit.setObjectName(u"actionspitspit")
        self.actionwhy_did_you_go_through_all_this = QAction(MainWindow)
        self.actionwhy_did_you_go_through_all_this.setObjectName(u"actionwhy_did_you_go_through_all_this")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 410, 181, 18))
        font = QFont()
        font.setFamilies([u"Hack"])
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 80, 121, 51))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 88, 34))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 803, 30))
        self.menuKita = QMenu(self.menubar)
        self.menuKita.setObjectName(u"menuKita")
        self.menufartspit = QMenu(self.menubar)
        self.menufartspit.setObjectName(u"menufartspit")
        self.menuspitfart = QMenu(self.menufartspit)
        self.menuspitfart.setObjectName(u"menuspitfart")
        self.menufartfart = QMenu(self.menuspitfart)
        self.menufartfart.setObjectName(u"menufartfart")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuKita.menuAction())
        self.menubar.addAction(self.menufartspit.menuAction())
        self.menuKita.addAction(self.actionWhat)
        self.menufartspit.addAction(self.menuspitfart.menuAction())
        self.menuspitfart.addAction(self.actionspitspit)
        self.menuspitfart.addAction(self.menufartfart.menuAction())
        self.menufartfart.addAction(self.actionwhy_did_you_go_through_all_this)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kita", None))
        self.actionPress_this_for_me_to_say_skrew_u.setText(QCoreApplication.translate("MainWindow", u"Press this for me to say skrew u", None))
        self.actionWhat.setText(QCoreApplication.translate("MainWindow", u"What", None))
        self.actionspitspit.setText(QCoreApplication.translate("MainWindow", u"spitspit", None))
        self.actionwhy_did_you_go_through_all_this.setText(QCoreApplication.translate("MainWindow", u"why did you go through all this", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kita Pre-Beta 0.0.1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"yes", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.menuKita.setTitle(QCoreApplication.translate("MainWindow", u"Kita", None))
        self.menufartspit.setTitle(QCoreApplication.translate("MainWindow", u"fartspit", None))
        self.menuspitfart.setTitle(QCoreApplication.translate("MainWindow", u"spitfart", None))
        self.menufartfart.setTitle(QCoreApplication.translate("MainWindow", u"fartfart", None))
    # retranslateUi

