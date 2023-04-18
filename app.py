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




if __name__ == '__main__':
    app.run()
