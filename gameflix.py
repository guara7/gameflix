from flask import Flask, render_template, request, redirect, session, flash, url_for

class Game:
    def __init__(self,nome,categoria,console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

listaJogos = [Game('Mario', 'Plataforma', 'Nintendo'),
                  Game('CS GO', 'Tiro', 'PC'),
                  Game('Last Of Us', 'Ação', 'PlayStation')]

class Usuario:
    def __init__(self,nome,apelido,senha):
        self.nome =nome
        self.apelido = apelido
        self.senha = senha

usuario1 =Usuario("Ericsson", "guara","miau")
usuario2 =Usuario("João", "vex","auau")
usuario3 =Usuario("Maria", "lacroix","pipi")

usuarios = { usuario1.apelido : usuario1,
             usuario2.apelido : usuario2,
             usuario3.apelido : usuario3 }


app = Flask(__name__)
app.secret_key = 'overgame'

@app.route('/')
def home():
    return render_template('lista.html', titulo='Games',jogos=listaJogos)

@app.route('/novo')
def novo1():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('logar',proxima=url_for('novo1')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar1():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novoJogo = Game(nome,categoria,console)
    listaJogos.append(novoJogo)
    return redirect(url_for('home'))

@app.route('/login')
def logar():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def auntenticar1():
    if request.form['usuario'] in usuarios:
        chaveUsuario = usuarios[request.form['usuario']]
        if request.form['senha'] == chaveUsuario.senha:
            session['usuario_logado'] = chaveUsuario.apelido
            flash(chaveUsuario.apelido + ' logado com sucesso')
            proximaPagina = request.form['proxima']
            return redirect(proximaPagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('logar'))

@app.route('/logout')
def deslogar():
    session['usuario_logado'] = None
    flash('Saiu com sucesso')
    return redirect(url_for('home'))

app.run(debug=True)
