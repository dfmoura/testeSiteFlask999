import json
import requests

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mostrar", methods=["POST"])
def mostrar():
    mensagem = "é somente um teste oficial..."
    return render_template("index.html", msg=mensagem)



@app.route("/dolarptax", methods=["POST"])
def dolarptax():
    ptax = "Ainda não!!!requests.args.get(usdbrl)"
    return render_template("index.html", ptax=ptax)





if __name__ == '__main__':
    app.run()
