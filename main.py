from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def inicial():
    return render_template("index.html")


@app.route("/contatos")
def contato():
    return render_template("contatos.html")


@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")


@app.route("/sobre")
def sob():
    return render_template("sobre.html")


if __name__ == '__main__':
    app.run()