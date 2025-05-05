from flask import Flask,render_template
from routes.usuario import usuario_route


app = Flask(__name__)

app.register_blueprint(usuario_route)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/musicas')
def musicas():
    return render_template('lista_musica.html')


app.run(debug=True)