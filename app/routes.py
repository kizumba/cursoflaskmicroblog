from flask import redirect, render_template
from app import app
from flask import request
from flask import flash
from flask import redirect


@app.route('/')
@app.route('/index/', defaults={"nome":"usuário"})
@app.route('/index/<nome>/<profissao>/<idade>')
def index(nome, profissao, idade):
    dados = {"profissao": profissao, "idade": idade}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario=='admin' and senha=='123':
        return "usuario: {} e senha: {}".format(usuario, senha)
    else:
        flash("Dados inválidos")
        flash("Senha ou usuário inválidos!")
        return redirect('/login')
