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



@app.route("/dolaratual1", methods=["POST"])
def valorUSD_BRL():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    dic_requisicao = requisicao.json()
    dolaratual = dic_requisicao['USDBRL']['bid']
    return render_template("index.html", dolaratual=dolaratual)


@app.route("/cnpj", methods=["POST"])
def consulta_cnpj(cnpj): 
    
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)
    response1 = response.json()
    cnpj_show = response1['capital_social']
    #['nome']['municipio']['uf']
    #resp = json.loads(response.text)
    #print(response.text)
    #print(resp['atividade_principal'])
    #resp['capital_social'], resp['nome'], resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'], resp['municipio'], resp['uf'], resp['cep'], resp['telefone'], resp['email']    
    return render_template("index.html", cnpj_show = cnpj_show)
consulta_cnpj('22685341000180')







if __name__ == '__main__':
    app.run()
