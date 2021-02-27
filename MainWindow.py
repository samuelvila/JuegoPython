# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1320, 884)
        MainWindow.setStyleSheet("background-color: rgb(98, 75, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(1250, 700))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(22)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabMenu = QtWidgets.QWidget()
        self.tabMenu.setObjectName("tabMenu")
        self.widget = QtWidgets.QWidget(self.tabMenu)
        self.widget.setGeometry(QtCore.QRect(30, 20, 1191, 621))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 2, 0, 1, 1)
        self.btnOpciones = QtWidgets.QPushButton(self.widget)
        self.btnOpciones.setMinimumSize(QtCore.QSize(0, 50))
        self.btnOpciones.setStyleSheet("background-color: rgb(200, 203, 131);\n"
"font: 75 14pt \"Impact\";")
        self.btnOpciones.setObjectName("btnOpciones")
        self.gridLayout_5.addWidget(self.btnOpciones, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 2, 7, 1)
        self.lblJugador = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblJugador.sizePolicy().hasHeightForWidth())
        self.lblJugador.setSizePolicy(sizePolicy)
        self.lblJugador.setMinimumSize(QtCore.QSize(10, 50))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        self.lblJugador.setFont(font)
        self.lblJugador.setStyleSheet("background-color: rgba(255, 0, 0, 0);")
        self.lblJugador.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblJugador.setObjectName("lblJugador")
        self.gridLayout_5.addWidget(self.lblJugador, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(200, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/diamond/bfiamond.png"))
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 2, 1)
        self.btnCargarJugador = QtWidgets.QPushButton(self.widget)
        self.btnCargarJugador.setEnabled(True)
        self.btnCargarJugador.setMinimumSize(QtCore.QSize(0, 50))
        self.btnCargarJugador.setStyleSheet("background-color: rgb(200, 203, 131);\n"
"font: 15pt \"Impact\";")
        self.btnCargarJugador.setObjectName("btnCargarJugador")
        self.gridLayout_5.addWidget(self.btnCargarJugador, 0, 3, 1, 1)
        self.editNombre = QtWidgets.QLineEdit(self.widget)
        self.editNombre.setMinimumSize(QtCore.QSize(0, 40))
        self.editNombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.editNombre.setObjectName("editNombre")
        self.gridLayout_5.addWidget(self.editNombre, 0, 4, 1, 1)
        self.btnRecargar = QtWidgets.QPushButton(self.widget)
        self.btnRecargar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/recargar/recargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRecargar.setIcon(icon)
        self.btnRecargar.setIconSize(QtCore.QSize(32, 32))
        self.btnRecargar.setObjectName("btnRecargar")
        self.gridLayout_5.addWidget(self.btnRecargar, 0, 5, 1, 1)
        self.tablaJugadores = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablaJugadores.sizePolicy().hasHeightForWidth())
        self.tablaJugadores.setSizePolicy(sizePolicy)
        self.tablaJugadores.setMinimumSize(QtCore.QSize(481, 0))
        self.tablaJugadores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tablaJugadores.setStyleSheet("background-color: rgb(197, 253, 255);")
        self.tablaJugadores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaJugadores.setShowGrid(True)
        self.tablaJugadores.setObjectName("tablaJugadores")
        self.tablaJugadores.setColumnCount(4)
        self.tablaJugadores.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tablaJugadores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tablaJugadores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tablaJugadores.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Impact")
        item.setFont(font)
        self.tablaJugadores.setHorizontalHeaderItem(3, item)
        self.tablaJugadores.horizontalHeader().setDefaultSectionSize(116)
        self.tablaJugadores.verticalHeader().setDefaultSectionSize(30)
        self.tablaJugadores.verticalHeader().setMinimumSectionSize(30)
        self.gridLayout_5.addWidget(self.tablaJugadores, 1, 3, 7, 4)
        self.btnBuscar = QtWidgets.QPushButton(self.widget)
        self.btnBuscar.setStyleSheet("")
        self.btnBuscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/lupa/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon1)
        self.btnBuscar.setIconSize(QtCore.QSize(32, 32))
        self.btnBuscar.setObjectName("btnBuscar")
        self.gridLayout_5.addWidget(self.btnBuscar, 0, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 0, 1, 1, 1)
        self.btnEmpezar = QtWidgets.QPushButton(self.widget)
        self.btnEmpezar.setEnabled(False)
        self.btnEmpezar.setMinimumSize(QtCore.QSize(0, 50))
        self.btnEmpezar.setStyleSheet("background-color: rgb(200, 203, 131);\n"
"font: 75 14pt \"Impact\";")
        self.btnEmpezar.setCheckable(False)
        self.btnEmpezar.setAutoExclusive(False)
        self.btnEmpezar.setAutoDefault(False)
        self.btnEmpezar.setDefault(False)
        self.btnEmpezar.setFlat(False)
        self.btnEmpezar.setObjectName("btnEmpezar")
        self.gridLayout_5.addWidget(self.btnEmpezar, 4, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 3, 0, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.widget)
        self.btnSalir.setMinimumSize(QtCore.QSize(0, 50))
        self.btnSalir.setStyleSheet("background-color: rgb(200, 203, 131);\n"
"font: 75 14pt \"Impact\";")
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout_5.addWidget(self.btnSalir, 7, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem7, 8, 0, 1, 7)
        self.tabWidget.addTab(self.tabMenu, "")
        self.tabOpciones = QtWidgets.QWidget()
        self.tabOpciones.setObjectName("tabOpciones")
        self.widget1 = QtWidgets.QWidget(self.tabOpciones)
        self.widget1.setGeometry(QtCore.QRect(30, 20, 1201, 631))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblJugador_5 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.lblJugador_5.setFont(font)
        self.lblJugador_5.setStyleSheet("background-color: rgba(255, 0, 0, 0);")
        self.lblJugador_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblJugador_5.setObjectName("lblJugador_5")
        self.gridLayout_3.addWidget(self.lblJugador_5, 6, 1, 1, 1)
        self.SliderEfectos = QtWidgets.QSlider(self.widget1)
        self.SliderEfectos.setStyleSheet("")
        self.SliderEfectos.setMaximum(100)
        self.SliderEfectos.setSliderPosition(100)
        self.SliderEfectos.setOrientation(QtCore.Qt.Horizontal)
        self.SliderEfectos.setObjectName("SliderEfectos")
        self.gridLayout_3.addWidget(self.SliderEfectos, 4, 2, 1, 1)
        self.lblJugador_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.lblJugador_3.setFont(font)
        self.lblJugador_3.setStyleSheet("background-color: rgba(255, 0, 0, 0);")
        self.lblJugador_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblJugador_3.setObjectName("lblJugador_3")
        self.gridLayout_3.addWidget(self.lblJugador_3, 4, 1, 1, 1)
        self.lblJugador_7 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.lblJugador_7.setFont(font)
        self.lblJugador_7.setStyleSheet("background-color: rgba(255, 0, 0, 0);")
        self.lblJugador_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblJugador_7.setObjectName("lblJugador_7")
        self.gridLayout_3.addWidget(self.lblJugador_7, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/diamond/bfiamond.png"))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.btnGuardarCambios = QtWidgets.QPushButton(self.widget1)
        self.btnGuardarCambios.setMinimumSize(QtCore.QSize(0, 50))
        self.btnGuardarCambios.setStyleSheet("background-color: rgb(200, 203, 131);\n"
"font: 75 14pt \"Impact\";")
        self.btnGuardarCambios.setObjectName("btnGuardarCambios")
        self.gridLayout_3.addWidget(self.btnGuardarCambios, 8, 1, 1, 2)
        self.cmbResolucion = QtWidgets.QComboBox(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbResolucion.sizePolicy().hasHeightForWidth())
        self.cmbResolucion.setSizePolicy(sizePolicy)
        self.cmbResolucion.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        self.cmbResolucion.setFont(font)
        self.cmbResolucion.setStyleSheet("")
        self.cmbResolucion.setFrame(True)
        self.cmbResolucion.setObjectName("cmbResolucion")
        self.gridLayout_3.addWidget(self.cmbResolucion, 6, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem8, 3, 2, 1, 1)
        self.SliderMusica = QtWidgets.QSlider(self.widget1)
        self.SliderMusica.setMaximum(100)
        self.SliderMusica.setSliderPosition(100)
        self.SliderMusica.setOrientation(QtCore.Qt.Horizontal)
        self.SliderMusica.setObjectName("SliderMusica")
        self.gridLayout_3.addWidget(self.SliderMusica, 2, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 7, 1, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 1, 1, 1, 2)
        self.lblJugador_6 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblJugador_6.sizePolicy().hasHeightForWidth())
        self.lblJugador_6.setSizePolicy(sizePolicy)
        self.lblJugador_6.setStyleSheet("background-color: rgba(255, 0, 0, 0);\n"
"font: 8pt \"Impact\";")
        self.lblJugador_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lblJugador_6.setObjectName("lblJugador_6")
        self.gridLayout_3.addWidget(self.lblJugador_6, 0, 1, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem11, 5, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 0, 3, 12, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem13, 1, 0, 11, 1)
        self.tabWidget.addTab(self.tabOpciones, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOpciones.setText(_translate("MainWindow", "OPCIONES"))
        self.lblJugador.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.btnCargarJugador.setText(_translate("MainWindow", "Añadir jugador"))
        item = self.tablaJugadores.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "JUGADOR"))
        item = self.tablaJugadores.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PUNTOS"))
        item = self.tablaJugadores.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NIVEL"))
        item = self.tablaJugadores.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "FECHA"))
        self.btnEmpezar.setText(_translate("MainWindow", "Empezar"))
        self.btnSalir.setText(_translate("MainWindow", "salir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMenu), _translate("MainWindow", "Menu"))
        self.lblJugador_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600;\">RESOLUCIÓN</span></p></body></html>"))
        self.lblJugador_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600;\">VOLUMEN DE EFECTOS</span></p></body></html>"))
        self.lblJugador_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600;\">VOLUMEN DE MÚSICA</span></p></body></html>"))
        self.btnGuardarCambios.setText(_translate("MainWindow", "GUARDAR CAMBIOS"))
        self.lblJugador_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">MENÚ DE OPCIONES</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOpciones), _translate("MainWindow", "Opciones"))
import diamond_rc
import lupa_rc
import recargar_rc
