
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1700, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabla_dieta = QTableWidget(self.centralwidget)
        self.tabla_dieta.setObjectName(u"tabla_dieta")
        self.tabla_dieta.setGeometry(QRect(100, 110, 1180, 500))

        self.tabla_datos = QTableWidget(self.centralwidget)
        self.tabla_datos.setObjectName(u"tabla_datos")
        self.tabla_datos.setGeometry(QRect(1350, 150, 300, 300))

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 221, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.label.setFont(font)

        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(1350, 100, 300, 51))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.label2.setFont(font)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 815, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DIETA DEL MES", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"Resultados/Datos de la persona: ", None))
    # retranslateUi

