from MainWindow import *
from VentanaSalir import *

import var, sys, metodos


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisoSalir = Ui_DialogAvisoSalir()
        var.avisoSalir.setupUi(self)
        var.avisoSalir.buttonBoxSalir.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(metodos.Metodos.salir)



class Main(QtWidgets.QMainWindow):
    def __init__(self):

        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        QtWidgets.QAction(self).triggered.connect(self.close)
        var.avisoSalir = DialogSalir()


        ''' BOTONES '''
        var.ui.btnCargarJugador.clicked.connect(metodos.Metodos.cargar_jugadores)
        var.ui.btnEmpezar.clicked.connect(metodos.Metodos.lanzar_juego)
        var.ui.btnEmpezar.clicked.connect(metodos.Metodos.ocultar_ventana)

        var.ui.btnCargarJugador.clicked.connect(metodos.Metodos.mostrar_nombre_jugadores)
        var.ui.btnBuscar.clicked.connect(metodos.Metodos.mostrar_jugador_tabla)
        var.ui.btnRecargar.clicked.connect(metodos.Metodos.mostrar_nombre_jugadores)
        var.ui.btnSalir.clicked.connect(metodos.Metodos.salir)
        var.ui.btnGuardarCambios.clicked.connect(metodos.Metodos.cargar_config)
        #var.ui.btnOpciones.clicked.connect()
        metodos.Metodos.cargar_cmb_res()


        ''' CONEXIÓN BBDD '''
        metodos.Metodos.conexion_base_de_datos(var.archivoDB)


        ''' MOSTRAR DATOS EN LA TABLA '''
        metodos.Metodos.mostrar_nombre_jugadores()
        var.ui.tablaJugadores.clicked.connect(metodos.Metodos.seleccion_jugador)
        var.ui.tablaJugadores.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.setWindowTitle("Black Dyamonds")
    window.showNormal()
    sys.exit(app.exec())