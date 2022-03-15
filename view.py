# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tablaGHeqUJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(769, 608)
        self.personas = QListWidget(Dialog)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        QListWidgetItem(self.personas)
        self.personas.setObjectName(u"personas")
        self.personas.setGeometry(QRect(70, 10, 321, 251))
        self.botonMostrar = QPushButton(Dialog)
        self.botonMostrar.setObjectName(u"botonMostrar")
        self.botonMostrar.setGeometry(QRect(450, 100, 121, 41))
        self.textGenero = QLabel(Dialog)
        self.textGenero.setObjectName(u"textGenero")
        self.textGenero.setGeometry(QRect(80, 280, 51, 21))
        self.botonAceptar = QPushButton(Dialog)
        self.botonAceptar.setObjectName(u"botonAceptar")
        self.botonAceptar.setGeometry(QRect(440, 190, 181, 51))
        self.TextAF = QLabel(Dialog)
        self.TextAF.setObjectName(u"TextAF")
        self.TextAF.setGeometry(QRect(80, 360, 81, 21))
        self.textEstatura = QLabel(Dialog)
        self.textEstatura.setObjectName(u"textEstatura")
        self.textEstatura.setGeometry(QRect(80, 320, 71, 21))
        self.textEdad = QLabel(Dialog)
        self.textEdad.setObjectName(u"textEdad")
        self.textEdad.setGeometry(QRect(80, 340, 71, 21))
        self.textPeso = QLabel(Dialog)
        self.textPeso.setObjectName(u"textPeso")
        self.textPeso.setGeometry(QRect(80, 300, 71, 21))
        self.textAlimentos = QLabel(Dialog)
        self.textAlimentos.setObjectName(u"textAlimentos")
        self.textAlimentos.setGeometry(QRect(80, 410, 141, 21))
        self.labelEstatura = QLabel(Dialog)
        self.labelEstatura.setObjectName(u"labelEstatura")
        self.labelEstatura.setGeometry(QRect(140, 320, 331, 21))
        self.labelAF = QLabel(Dialog)
        self.labelAF.setObjectName(u"labelAF")
        self.labelAF.setGeometry(QRect(190, 360, 331, 21))
        self.labelPeso = QLabel(Dialog)
        self.labelPeso.setObjectName(u"labelPeso")
        self.labelPeso.setGeometry(QRect(140, 300, 331, 21))
        self.labelGenero = QLabel(Dialog)
        self.labelGenero.setObjectName(u"labelGenero")
        self.labelGenero.setGeometry(QRect(140, 280, 331, 21))
        self.labelEdad = QLabel(Dialog)
        self.labelEdad.setObjectName(u"labelEdad")
        self.labelEdad.setGeometry(QRect(140, 340, 331, 21))
        self.tableAlimentos = QTableWidget(Dialog)
        if (self.tableAlimentos.columnCount() < 1):
            self.tableAlimentos.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableAlimentos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableAlimentos.setObjectName(u"tableAlimentos")
        self.tableAlimentos.setGeometry(QRect(230, 390, 391, 191))


        
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))

        __sortingEnabled = self.personas.isSortingEnabled()
        self.personas.setSortingEnabled(False)
        ___qlistwidgetitem = self.personas.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"Persona 1", None));
        ___qlistwidgetitem1 = self.personas.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"Persona 2", None));
        ___qlistwidgetitem2 = self.personas.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"Persona 3", None));
        ___qlistwidgetitem3 = self.personas.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"Persona 4", None));
        ___qlistwidgetitem4 = self.personas.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"Persona 5", None));
        ___qlistwidgetitem5 = self.personas.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Dialog", u"Persona 6", None));
        ___qlistwidgetitem6 = self.personas.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Dialog", u"Persona 7", None));
        ___qlistwidgetitem7 = self.personas.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Dialog", u"Persona 8", None));
        ___qlistwidgetitem8 = self.personas.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Dialog", u"Persona 9", None));
        ___qlistwidgetitem9 = self.personas.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Dialog", u"Persona 10", None));
        ___qlistwidgetitem10 = self.personas.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Dialog", u"Persona 11", None));
        ___qlistwidgetitem11 = self.personas.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Dialog", u"Persona 12 ", None));
        ___qlistwidgetitem12 = self.personas.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Dialog", u"Persona 13", None));
        ___qlistwidgetitem13 = self.personas.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Dialog", u"Persona 14", None));
        ___qlistwidgetitem14 = self.personas.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Dialog", u"Persona 15", None));
        ___qlistwidgetitem15 = self.personas.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Dialog", u"Persona 16", None));
        ___qlistwidgetitem16 = self.personas.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Dialog", u"Persona 17", None));
        ___qlistwidgetitem17 = self.personas.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Dialog", u"Persona 18", None));
        ___qlistwidgetitem18 = self.personas.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Dialog", u"Persona 19", None));
        ___qlistwidgetitem19 = self.personas.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Dialog", u"Persona 20", None));
        ___qlistwidgetitem20 = self.personas.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Dialog", u"Persona 21", None));
        ___qlistwidgetitem21 = self.personas.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Dialog", u"Persona 22", None));
        ___qlistwidgetitem22 = self.personas.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Dialog", u"Persona 23", None));
        ___qlistwidgetitem23 = self.personas.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Dialog", u"Persona 24", None));
        ___qlistwidgetitem24 = self.personas.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Dialog", u"Persona 25", None));
        self.personas.setSortingEnabled(__sortingEnabled)

        self.botonMostrar.setText(QCoreApplication.translate("Dialog", u"Mostrar", None))
        self.textGenero.setText(QCoreApplication.translate("Dialog", u"Genero: ", None))
        self.botonAceptar.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.TextAF.setText(QCoreApplication.translate("Dialog", u"Actividad Fisica: ", None))
        self.textEstatura.setText(QCoreApplication.translate("Dialog", u"Estatura: ", None))
        self.textEdad.setText(QCoreApplication.translate("Dialog", u"Edad: ", None))
        self.textPeso.setText(QCoreApplication.translate("Dialog", u"Peso: ", None))
        self.textAlimentos.setText(QCoreApplication.translate("Dialog", u"Alimentos que no le gusta: ", None))
        self.labelEstatura.setText("")
        self.labelAF.setText("")
        self.labelPeso.setText("")
        self.labelGenero.setText("")
        self.labelEdad.setText("")
        ___qtablewidgetitem = self.tableAlimentos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Alimentos", None));
    # retranslateUi

