import mysql.connector

class database:
    my_db = my_cursor = None

    def __init__(self):
        global my_db, my_cursor
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tienda_online"
        )
        my_cursor = my_db.cursor()


class crudusuarios(database):
    def listausuarios(self, mode='DESC'):
        sql = "SELECT * FROM `usuarios`".format(mode)

        try:
            my_cursor.execute(sql)
            listausu = my_cursor.fetchall()
        except Exception as e:
            return e

        return listausu

    def buscaid(self, id_usuario, mode='DESC'):
        sql = "SELECT * FROM usuarios WHERE id_usuario = {}".format(id_usuario)

        try:
            my_cursor.execute(sql)
            usuario = my_cursor.fetchall()
        except Exception as e:
            return e

        return usuario

    def insertausu(self, data):

        sql = "INSERT INTO usuarios (nombre, apellidos, correo, passwd, preferencias) VALUES (%s , %s, %s , %s, %s)"

        try:
            my_cursor.execute(sql, data)
            my_db.commit()
        except Exception as e:
            return e

        return my_cursor.lastrowid

    def delete(self, id_usuario):
        sql = "DELETE FROM usuarios WHERE id_usuario = {}".format(id_usuario)

        try:
            my_cursor.execute(sql)
            my_db.commit()
        except Exception as e:
            return e

    def update(self, id_usuario, data):


        sql = "UPDATE usuarios SET nombre = %s ,apellidos = %s, correo = %s, passwd = %s, preferencias = %s WHERE id_usuario = {}".format(
            id_usuario)

        val = (data[0], data[1], data[2], data[3], data[4])

        try:
            my_cursor.execute(sql, val)
            my_db.commit()
        except Exception as e:
            return e

class crudusuarios(database):
    def listausuarios(self, mode='DESC'):
        sql = "SELECT * FROM `usuarios`".format(mode)

        try:
            my_cursor.execute(sql)
            listausu = my_cursor.fetchall()
        except Exception as e:
            return e

        return listausu

    def buscaid(self, id_usuario, mode='DESC'):
        sql = "SELECT * FROM usuarios WHERE id_usuario = {}".format(id_usuario)

        try:
            my_cursor.execute(sql)
            usuario = my_cursor.fetchall()
        except Exception as e:
            return e

        return usuario

    def insertausu(self, data):

        sql = "INSERT INTO usuarios (nombre, apellidos, correo, passwd, preferencias) VALUES (%s , %s, %s , %s, %s)"

        try:
            my_cursor.execute(sql, data)
            my_db.commit()
        except Exception as e:
            return e

        return my_cursor.lastrowid

    def delete(self, id_usuario):
        sql = "DELETE FROM usuarios WHERE id_usuario = {}".format(id_usuario)

        try:
            my_cursor.execute(sql)
            my_db.commit()
        except Exception as e:
            return e

    def update(self, id_usuario, data):


        sql = "UPDATE usuarios SET nombre = %s ,apellidos = %s, correo = %s, passwd = %s, preferencias = %s WHERE id_usuario = {}".format(
            id_usuario)

        val = (data[0], data[1], data[2], data[3], data[4])

        try:
            my_cursor.execute(sql, val)
            my_db.commit()
        except Exception as e:
            return e
class crudcatalogo(database):
    def listarcatalogo(self, mode='DESC'):
        sql = "SELECT * FROM `catalogo`".format(mode)

        try:
            my_cursor.execute(sql)
            listacatalogo = my_cursor.fetchall()
        except Exception as e:
            return e

        return listacatalogo

    def buscaid(self, id_prenda, mode='DESC'):
        sql = "SELECT * FROM catalogo WHERE id_usuario = {}".format(id_prenda)

        try:
            my_cursor.execute(sql)
            usuario = my_cursor.fetchall()
        except Exception as e:
            return e

        return usuario

    def insertausu(self, data):

        sql = "INSERT INTO catalogo (stock, tipo_prenda, estilo, color, precio, foto) VALUES (%s , %s, %s , %s, %s, %s)"

        try:
            my_cursor.execute(sql, data)
            my_db.commit()
        except Exception as e:
            return e

        return my_cursor.lastrowid

    def delete(self, id_prenda):
        sql = "DELETE FROM catalogo WHERE id_usuario = {}".format(id_prenda)

        try:
            my_cursor.execute(sql)
            my_db.commit()
        except Exception as e:
            return e

    def update(self, id_prenda, data):


        sql = "UPDATE catalogo SET stock = %s ,tipo_prenda = %s, estilo = %s, color = %s, precio = %s, foto = %s WHERE id_usuario = {}".format(
            id_prenda)

        val = (data[0], data[1], data[2], data[3], data[4])

        try:
            my_cursor.execute(sql, val)
            my_db.commit()
        except Exception as e:
            return e

class crudtransacciones(database):
    def listatransacciones(self, mode='DESC'):
        sql = "SELECT * FROM `transacciones`".format(mode)

        try:
            my_cursor.execute(sql)
            listausu = my_cursor.fetchall()
        except Exception as e:
            return e

        return listausu

    def buscatransaccion(self, id_transaccion, mode='DESC'):
        sql = "SELECT * FROM transacciones WHERE id_transaccion = {}".format(id_transaccion)

        try:
            my_cursor.execute(sql)
            usuario = my_cursor.fetchall()
        except Exception as e:
            return e

        return usuario

    def insertausu(self, data):

        sql = "INSERT INTO transacciones (nombre, apellidos, correo, passwd, preferencias) VALUES (%s , %s, %s , %s, %s)"

        try:
            my_cursor.execute(sql, data)
            my_db.commit()
        except Exception as e:
            return e

        return my_cursor.lastrowid

    def delete(self, id_transaccion):
        sql = "DELETE FROM transacciones WHERE id_transaccion = {}".format(id_transaccion)

        try:
            my_cursor.execute(sql)
            my_db.commit()
        except Exception as e:
            return e

    def update(self, id_transaccion, data):


        sql = "UPDATE transacciones SET nombre = %s ,apellidos = %s, correo = %s, passwd = %s, preferencias = %s WHERE id_usuario = {}".format(
            id_transaccion)

        val = (data[0], data[1], data[2], data[3], data[4])

        try:
            my_cursor.execute(sql, val)
            my_db.commit()
        except Exception as e:
            return e

#METODO QUE RESTA STOCK POR CADA COMPRA
    def updatestock(self, id_transaccion, data):


        sql = "UPDATE catalogo SET stock WHERE id_prenda = {}".format(
            id_transaccion)

        val = (data[0], data[1], data[2], data[3], data[4])

        try:
            my_cursor.execute(sql, val)
            my_db.commit()
        except Exception as e:
            return e