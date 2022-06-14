import json

from flask import Flask, request, render_template, url_for, jsonify
from werkzeug.utils import redirect

from bck.objetos.conector import crudcatalogo, database, crudusuarios

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/nenes')
def nenes():
    return render_template("nenes.html")


@app.route('/hombres')
def hombres():
    return render_template("hombres.html")


@app.route('/mujeres')
def mujeres():
    return render_template("mujeres.html")


@app.route('/catalogo')
def catalogo():
    return render_template("catalogo.html")


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


@app.route('/success')
def success():
    return render_template("mujeres.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        return redirect(url_for('success', 'mujeres.html'))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/validate', methods=["POST"])
def validate():
    if request.method == 'POST' and request.form['pass'] == 'jtp':
        return redirect(url_for("success"))
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run()
