from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('portugues/index.html')

@app.route('/contato')
def contato():
    return render_template('portugues/contato.html')

@app.route('/projetos')
def projetos():
    return render_template('portugues/projetos.html')

@app.route('/curriculo')
def curriculo():
    return render_template('portugues/curriculo.html')

if __name__ == '__main__':
    app.run()
