from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect

from bck.objetos import *


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

      return redirect(url_for('success',catalogo = crudcatalogo.listarcatalogo()))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


@app.route('/validate', methods=["POST"])
def validate():
    if request.method == 'POST' and request.form['pass'] == 'jtp':
        return redirect(url_for("success"))
    return redirect(url_for("login"))


@app.route('/success')
def success():
    return "logged in successfully"

if __name__ == '__main__':
    app.run()