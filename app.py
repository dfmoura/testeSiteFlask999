from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mostrar", methods=["POST"])
def mostrar():
    mensagem = "é somente um teste oficial..."
    return render_template("index.html", msg=mensagem)


if __name__ == '__main__':
    app.run()
