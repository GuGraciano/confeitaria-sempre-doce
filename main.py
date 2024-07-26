from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')



if __name__ == '__main__':
    app.run()
