from MainWindow import *
from VentanaSalir import *

import var, sys, metodos


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisoSalir = Ui_DialogAvisoSalir()
        var.avisoSalir.setupUi(self)
        var.avisoSalir.buttonBoxSalir.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(metodos.Metodos.Salir)



class Main(QtWidgets.QMainWindow):
    def __init__(self):

        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        QtWidgets.QAction(self).triggered.connect(self.close)
        var.avisoSalir = DialogSalir()

        ''' BOTONES '''
        var.ui.btnCargarJugador.clicked.connect(metodos.Metodos.CargarJugadores)
        var.ui.btnCargarJugador.clicked.connect(metodos.Metodos.MostrarNombreJugadores)
        var.ui.btnBuscar.clicked.connect(metodos.Metodos.BuscarJugadorBtn)
        var.ui.btnRecargar.clicked.connect(metodos.Metodos.MostrarNombreJugadores)
        var.ui.btnSalir.clicked.connect(metodos.Metodos.Salir)


        ''' CONEXIÓN BBDD '''
        metodos.Metodos.conexionBaseDeDatos(var.archivoDB)


        ''' MOSTRAR DATOS EN LA TABLA '''
        metodos.Metodos.MostrarNombreJugadores()
        var.ui.tablaJugadores.clicked.connect(metodos.Metodos.seleccionJugador)
        var.ui.tablaJugadores.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showNormal()
    sys.exit(app.exec())