# Repositório para estudos com flask

## Atividade 01

### Para iniciar o projeto
#### Para criação da .venv

```bash

python3 -m venv .venv

```

#### Para ativa o ambiente de densevolvimento e .venv

```python

.venv\Scripts\activate

```

### Estrutura da atividade 01:

```bash
Flask_study/
├── database/
│   └── usuario.py
├── routes/
│   └── usuario.py
├── static/
│   └── cru.js
├── templates/
│   ├── forms.html
│   ├── index.html
│   └── test.html
├── main.py
└── README.md
```

---

### database/usuario.py

#### Banco com lista de dicionário

```python
USUARIO = [
    {"id": 1,"nome": "jaygarcia" ,"email": "jaygarcia@gmail.com", "senha":123},
    {"id": 2,"nome": "ouken","email": "oukenikidori@gmail.com", "senha":123},
    {"id": 3,"nome": "saturn" ,"email": "saintjaygarciasaturn@gmail.com", "senha":123}
]

MUSICA = [
    {"id" : 1, "nome":"One piece is my favorite anime"},
]
```

---

### routes/usuario.py

#### Blueprint de usuário

```python
from flask import Blueprint, request, render_template, redirect, url_for
from database.usuario import USUARIO, MUSICA

usuario_route = Blueprint('usuario', __name__)
```

---

#### Rota: `/login`

* **Métodos**: `GET`, `POST`
* **Descrição**: Rota responsável por exibir o formulário de login e processar as credenciais do usuário.

```python
@usuario_route.route('/login', methods=['GET', 'POST'])
def login_usuario():
    return validar_login() if request.method == 'POST' else render_template('forms.html')
```

---

#### Função auxiliar: `validar_login()`

```python
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
```

---

#### Rota: `/perfil/<nome>`

* **Métodos**: `GET`, `POST`
* **Descrição**: Tela de perfil onde é possível cadastrar novas músicas e visualizar a lista existente.

```python
@usuario_route.route('/perfil/<nome>', methods=['GET', 'POST'])
def perfil(nome):
    if request.method == 'POST':
        nome_musica = request.form.get('nome')
        MUSICA.append({"id": len(MUSICA) + 1, "nome": nome_musica})
        return redirect(url_for('usuario.perfil', nome=nome))

    return render_template('lista_musica.html', nome=nome, musicaLista=MUSICA)
```

---
