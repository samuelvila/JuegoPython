from MainWindow import *

import var, sys, metodos




class Main(QtWidgets.QMainWindow):
    def __init__(self):

        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        QtWidgets.QAction(self).triggered.connect(self.close)

        var.ui.btnCargarJugador.clicked.connect(metodos.Metodos.CargarJugadores)


        metodos.Metodos.conexionBaseDeDatos(var.archivoDB)

        metodos.Metodos.MostrarNombreJugadores()
        var.ui.tablaJugadores.clicked.connect(metodos.Metodos.seleccionJugador)

        metodos.Metodos.MostrarTop5()
        var.ui.tablaTop.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())