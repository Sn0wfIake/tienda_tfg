import json
import re
from typing import re

import MySQLdb
from flask import Flask, render_template, request, url_for, session
from flask_mysqldb import MySQL
from werkzeug.utils import redirect

from bck.objetos.conector import crudcatalogo

app = Flask(__name__, template_folder='template')
app.secret_key = 'super secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tienda_online'

mysql = MySQL(app)


@app.route('/')
def index():
    if not session.get("user"):
        # Si tiene sesion te redirige a tu sesion
        return redirect("/login")

    return render_template("loginhecho.html")


@app.route('/nenes')
def nenes():
    if not session.get("user"):
        # Si tiene sesion te redirige a tu sesion
        return redirect("/nenelogin")
    return render_template("nenes.html")


@app.route('/nenelogin')
def nenelogin():
    return render_template("nenelogin.html")


@app.route('/hombres')
def hombres():
    if not session.get("user"):
        # Si tiene sesion te redirige a tu sesion
        return redirect("/hombrelogin")
    return render_template("hombres.html")


@app.route('/hombrelogin')
def hombrelogin():
    return render_template("hombrelogin.html")


@app.route('/mujeres')
def mujeres():
    if not session.get("user"):
        # Si tiene sesion te redirige a tu sesion
        return redirect("/mujerlogin")
    return render_template("mujeres.html")


@app.route('/mujerlogin')
def mujerlogin():
    return render_template("mujerlogin.html")


@app.route('/catalogo')
def catalogo():
    if not session.get("user"):
        # Si tiene sesion te redirige a tu sesion
        return redirect("/cataloglogin")
    return render_template("catalogo.html")


@app.route('/cataloglogin')
def cataloglogin():
    return render_template("cataloglogin.html")


@app.route('/listacatalogoh', methods=['GET'])
def catalogoenteroh():
    st = crudcatalogo()
    listausu = st.listarcatalogoh()

    response = json.dumps(listausu)
    return response


@app.route('/listacatalogom', methods=['GET'])
def catalogoenterom():
    st = crudcatalogo()
    listausu = st.listarcatalogom()

    response = json.dumps(listausu)
    return response


@app.route('/listacatalogou', methods=['GET'])
def catalogoenterou():
    st = crudcatalogo()
    listausu = st.listarcatalogou()

    response = json.dumps(listausu)
    return response


@app.route('/listacatalogo', methods=['GET'])
def catalogoentero():
    st = crudcatalogo()
    listausu = st.listarcatalogo()

    response = json.dumps(listausu)
    return response


# LOGIN

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'user' in request.form and 'passwd' in request.form:
        user = request.form['user']
        passwd = request.form['passwd']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios WHERE correo = % s AND passwd = % s', (user, passwd,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['passwd'] = account['passwd']
            session['user'] = account['nombre']
            msg = 'Logged in successfully !'
            return render_template('loginhecho.html', msg=msg)
        else:
            msg = 'USUARIO O CONTRASEÑA INCORRECTOS'
    return render_template('index.html', msg=msg)


@app.route('/registrohecho', methods=['GET', 'POST'])
def registrofin():

    return render_template('indexregistro.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user', None)
    session.pop('passwd', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'correo' in request.form and 'apellido' in request.form and 'clave' in request.form and 'nombre' in request.form:
        correo = request.form['correo']
        passwd = request.form['clave']
        apellido = request.form['apellido']
        nombre = request.form['nombre']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios WHERE correo = % s', (correo,))
        account = cursor.fetchone()
        if account:
            msg = 'Ya existe!'

        else:
            cursor.execute('INSERT INTO usuarios (nombre, apellidos, correo, passwd) VALUES (%s , %s, %s , %s)',
                           (nombre, apellido, correo, passwd,))
            mysql.connection.commit()
            msg = 'Registrado correctamente!'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return redirect(url_for('registrofin'))


@app.route('/test', methods=['GET', 'POST'])
def test():
    salida = request.get_json()
    if salida is not None:
        actualizacatalogo(salida)
        return redirect(url_for('exito'))


@app.route('/exito')
def exito():
    return render_template("exito.html")


def actualizacatalogo(salida):
    st = crudcatalogo()
    for x in salida:
        st.update(x)
        print("vuelta " + x)


if __name__ == '__main__':
    app.run()
