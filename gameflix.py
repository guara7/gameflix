from flask import Flask, render_template, request, redirect, session, flash

class Game:
    def __init__(self,nome,categoria,console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

listaJogos = [Game('Mario', 'Plataforma', 'Nintendo'),
                  Game('CS GO', 'Tiro', 'PC'),
                  Game('Last Of Us', 'Ação', 'PlayStation')]

app = Flask(__name__)
app.secret_key = 'overgame'

@app.route('/')
def home():
    return render_template('lista.html', titulo='Games',jogos=listaJogos)

@app.route('/novo')
def novo1():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar1():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novoJogo = Game(nome,categoria,console)
    listaJogos.append(novoJogo)
    return redirect('/')

@app.route('/login')
def logar():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def auntenticar1():
    if 'miau' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso')
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')

@app.route('/logout')
def deslogar():
    session['usuario_logado'] = None
    flash('Saiu com sucesso')
    return redirect('/')

app.run(debug=True)
