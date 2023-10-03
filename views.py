import db_conexao
from app import app
from flask import request, jsonify, render_template, redirect, flash
import json
from models import Cadastro

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro_usuarios():
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.get_json('login')
    senha =request.get_json('password')
    with open('usuarios.json') as usuarios:
        lista = json.load(usuarios)
        cont = 0
        for usuario in lista:
            cont += 1
            if email == usuario['email'] and senha == usuario['senha']:
                print('LOGIN FEITO')
                return jsonify({
                    'status': '200'
                    })
            if cont >= len(lista):
                print('LOGIN NAO REALIZADO')
                flash('Usuário ou senha inválido')
                return jsonify(
                    error = 404, text = str('ERRO - NOT FOUND')
                )

@app.route('/cadastro_vagas')
def cadastro_vagas():
    return render_template('cadastro_vagas.html')



@app.route('/users', methods=['GET'])
def getRequest():
    content_type = request.headers.get('Content-Type')
    users_db = [b.serialize() for b in db_conexao.view()]
    return jsonify({
    'data': users_db,
    'status': '200',
    'msg': 'Success getting all books in library!👍😀'
})


@app.route("/users", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    nome = req_data['name'],
    rg= req_data['rg'],
    cpf = req_data['cpf'],
    data_nascimento = req_data['birthday'],
    sexo = req_data['sex'],
    email = req_data['email'],
    senha = req_data['password']

    user = Cadastro(nome, rg, cpf, data_nascimento, sexo, email, senha,'')
    a = db_conexao.insert(user)
    return jsonify({
        'res': a,
        'status': '201',
    })

@app.route('/users', methods=['PUT'])
def update_req():
    req_data = request.get_json()
    nome = req_data['name'],
    rg= req_data['rg'],
    cpf = req_data['cpf'],
    data_nascimento = req_data['birthday'],
    sexo = req_data['sex'],
    email = req_data['email'],
    senha = req_data['password']
    id = req_data['id']

    users_db = [b.serialize() for b in db_conexao.view()]
    for b in users_db:
        if b['id'] == id:
            user = Cadastro(nome, rg, cpf, data_nascimento, sexo, email, senha, id)
            print('new user: ', user.serialize())

            db_conexao.update(user)
            new_users = [b.serialize() for b in db_conexao.view()]
            print('books in lib: ', new_users)
            return jsonify({
                # 'error': '',
                'res': user.serialize(),
                'status': '200',
                'msg': f'Success updating the book titled {nome}!👍😀'
            })
    return jsonify({
        # 'error': '',
        'res': f'Error ⛔❌! Failed to update Book with title: {nome}!',
        'status': '404'
    })

@app.route('/users/<id>', methods=['DELETE'])
def delete_req(id):
    # Para acessar os dados de entrada no Flask, é necessário usar o objeto request(solicitação)
    # view_args: A dict of view arguments that matched the request. If an exception happened
    # when matching, this will be .None
    req_args = request.view_args
    db_conexao.delete(req_args['id'])
    
    return jsonify({
        'res': 'Deletou',
        'status': '404'
    })
    

# A serialização é o processo de conversão do estado de um objeto em um formulário
# que possa ser persistido ou transportado.
def serialize(self):
    return {
        'name': self.nome,
        'rg': self.rg,
        'cpf': self.cpf,
        'data_nascimento': self.data_nascimento,
        'sexo': self.sexo,
        'email': self.email,
        'senha': self.senha,
        'id': self.id
    }