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
