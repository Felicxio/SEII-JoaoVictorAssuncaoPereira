from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)

@app.route('/', methods= ["GET", "POST"])
def index():
    variavel = 'Game: Adivinhe o número correto'
    if request.method =="GET":
        return render_template("index.html", variavel=variavel)
    else:
        numero = randint(1,20)
        palpite = int(request.form.get('name'))
        if numero == palpite:
            return "<h1> Resultado: Você Ganhou</h1>"
        else:
            return "<h1> Resultado: Você Perdeu</h1>"

@app.route('/<string:nome>')
def error(nome):
    variavel = f'Página ({nome} não existe'
    return render_template("erro.html", variavel = variavel)