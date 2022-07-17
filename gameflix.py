from flask import Flask, render_template, request, redirect

class Game:
    def __init__(self,nome,categoria,console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

listaJogos = [Game('Mario', 'Plataforma', 'Nintendo'),
                  Game('CS GO', 'Tiro', 'PC'),
                  Game('Last Of Us', 'Ação', 'PlayStation')]

app = Flask(__name__)

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

app.run(debug=True)
