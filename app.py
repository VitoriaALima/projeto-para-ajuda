from flask import Flask, render_template, request, redirect

app = Flask(__name__)
filmes = []

@app.route('/')
def index():  # put application's code here
    return render_template('index.html', filmes=filmes)


@app.route('/adicionarr')
def adicionarr():
    return render_template('adicionar.html')


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        codigo = len(filmes)
        filmes.append([nome, genero, codigo])
        return render_template('index.html', filmes=filmes)
    else:
        return render_template('adicionar.html')  # Renderiza o formulário de adicionar contato


@app.route('/editar/<int:codigo>', methods=['GET', 'POST'])
def editar(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        filmes[codigo] = [codigo, nome, genero]
        return redirect('/index')  # Redireciona de volta para a página inicial
    else:
        filme = filmes[codigo]
        return render_template('editar.html', filme=filme)  # Renderiza o formulário de edição

@app.route('/apagar_filme/<int:codigo>')
def apagar_filme(codigo):
    del filmes[codigo]
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
