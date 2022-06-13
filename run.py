import json

from flask import Flask, request, render_template, url_for, jsonify
from werkzeug.utils import redirect

from bck.objetos import *
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

@app.route('/mujeres',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':

      return redirect(url_for('success', 'mujeres.html'))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


@app.route('/validate', methods=["POST"])
def validate():
    if request.method == 'POST' and request.form['pass'] == 'jtp':
        return redirect(url_for("success"))
    return redirect(url_for("login"))

@app.route('/listacatalogo', methods = ['GET'])
def catalogoentero():
    db = database()
    st = crudcatalogo()
    listausu = st.listarcatalogo()

    response = json.dumps(listausu)
    return response


@app.route('/success')
def success():
    return render_template("mujeres.html")

if __name__ == '__main__':
    app.run()