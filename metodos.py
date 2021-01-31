from PyQt5 import QtSql, QtWidgets, QtCore

import var




class Metodos():
    def conexionBaseDeDatos(name):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(name)
        if not db.open():
            QtWidgets.QMessageBox.Critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer la conexión. \n'
                                           'Haz Click para Cancelar.', QtWidgets.QMessageBox.Cancel)
            print('Error conexion')
            return False
        else:
            print('Conexion bien')
        return True


    @staticmethod
    def CargarJugadores():
        nombreJugador = var.ui.editNombre.text()

        if nombreJugador == '':
            print('Nombre del jugador vacio')
        else :
            query = QtSql.QSqlQuery()
            query.prepare('insert into Jugadores (nombre, tiempo, puntos)'
                            'VALUES (:nombre, :tiempo, :puntos)')
            query.bindValue(':nombre',str(nombreJugador))
            query.bindValue(':tiempo', 0)
            query.bindValue(':puntos', 0)
            print(nombreJugador)
            if query.exec_():
                print('Insercción Correcta')
            else:
                print('Error alta jugadores:', query.lastError().text())


    @staticmethod
    def MostrarNombreJugadores():

        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select nombre from Jugadores order by puntos desc')
        if query.exec_():
            while query.next():
                nombre = str(query.value(0))

                var.ui.tablaJugadores.setRowCount(index + 1)

                var.ui.tablaJugadores.setItem(index, 0, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tablaJugadores.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                index +=1
        else:
            print('Error en mostrar los jugadores')


    @staticmethod
    def MostrarTop5():

        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select * from Jugadores order by puntos desc')
        if query.exec_():
            while query.next():

                if(index<5):
                    nombre = str(query.value(0))
                    tiempo = str(query.value(1))
                    puntos = str(query.value(2))

                    var.ui.tablaTop.setRowCount(index + 1)

                    var.ui.tablaTop.setItem(index, 0, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tablaTop.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)

                    var.ui.tablaTop.setItem(index, 1, QtWidgets.QTableWidgetItem(tiempo))
                    var.ui.tablaTop.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)

                    var.ui.tablaTop.setItem(index, 2, QtWidgets.QTableWidgetItem(puntos))
                    var.ui.tablaTop.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                    index +=1
                else:
                    query.finish()
                    print('fin')
        else:
            print('Error en mostrar los jugadores')

    @staticmethod
    def seleccionJugador():
        try:
            fila = var.ui.tablaJugadores.selectedItems()
            if fila:
                fila = [dato.text() for dato in fila]
            var.ui.lblJugador.setText(str(fila[0]))
        except Exception as error:
            print('Error al seleccionar jugador : '+error)

