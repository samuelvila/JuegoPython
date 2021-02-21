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
    def ModificarJugador(nombre,tiempo,puntos):

        if nombre != '':
            query = QtSql.QSqlQuery()
            query.prepare('update Jugadores set tiempo=:tiempo, puntos=:puntos where nombre=:nombre')

            query.bindValue(':nombre', str(nombre))
            query.bindValue(':tiempo', int(tiempo))
            query.bindValue(':puntos', int(puntos))

            if query.exec_():
                Metodos.MostrarNombreJugadores()
                Metodos.MostrarTop5()
                print('Update Correcto')
            else:
                print('Error modificar jugadores:', query.lastError().text())


    @staticmethod
    def BorrarJugadores(nombre):

        if nombre != '':
            query = QtSql.QSqlQuery()
            query.prepare('delete from Jugadores where nombre = :nombreJugador')
            query.bindValue(':nombreJugador', str(nombre))
            if query.exec_():
                Metodos.MostrarNombreJugadores()
            else:
                print('Error al borrar jugador')
        else :
            print('No hay nombre')


    @staticmethod
    def BuscarJugador(nombre):

        if nombre != '':
            query = QtSql.QSqlQuery()
            query.prepare('select * from Jugadores where nombre = :nombreJugador')
            query.bindValue(':nombreJugador', str(nombre))
            if query.exec_():
                while query.next():
                    datos = [str(query.value(0)),str(query.value(1)),str(query.value(2))]
                    return datos
            else:
                datos = ["","",""]
                return datos


    @staticmethod
    def ListaJugadores():

        datos = []
        query = QtSql.QSqlQuery()
        query.prepare('select * from Jugadores')
        if query.exec_():
            while query.next():
                datos.append({'Nombre':query.value(0),'Tiempo':query.value(1),'Puntos':query.value(2)})
            datos.sort(key=lambda x: x.get('Puntos'), reverse=True)
            return datos
        else:
            return []
            print('Error al listar jugadores')


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

