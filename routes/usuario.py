from flask import Blueprint, request, render_template, redirect, url_for
from database.usuario import USUARIO, MUSICA

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/login', methods=['GET', 'POST'])
def login_usuario():
    return validar_login() if request.method == 'POST' else render_template('forms.html')

def validar_login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario_autenticado = next(
        (usuario for usuario in USUARIO if usuario['email'] == email and usuario['senha'] == int(senha)),
        None
    )

    return (
        redirect(url_for('usuario.perfil', nome=usuario_autenticado['nome']))
        if usuario_autenticado
        else render_template('forms.html', erro="Email ou senha incorretos")
    )

@usuario_route.route('/perfil/<nome>', methods=['GET', 'POST'])
def perfil(nome):
    if request.method == 'POST':
        nome_musica = request.form.get('nome')
        MUSICA.append({"id": len(MUSICA) + 1, "nome": nome_musica})
        return redirect(url_for('usuario.perfil', nome=nome))

    return render_template('lista_musica.html', nome=nome, musicaLista=MUSICA)
