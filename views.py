import db_conexao
from app import app
from flask import request, jsonify, render_template
from models import Cadastro

@app.route('/')
def visualizar():
    return render_template('cadastro.html')

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
    # sexo = req_data['sex'],
    email = req_data['email'],
    senha = req_data['password']

    user = Cadastro(nome, rg, cpf, data_nascimento, 'M', email, senha)
    db_conexao.insert(user)
    return jsonify({
        'res': serialize(user),
        'status': '201',
    })

def serialize(self):
    return {
        'name': self.nome,
        'rg': self.rg,
        'cpf': self.cpf,
        'data_nascimento': self.data_nascimento,
        'sexo': self.sexo,
        'email': self.email,
        'senha': self.senha
    }


# @app.route('/users', methods=['GET'])
# def getRequest():
#     content_type = request.headers.get('Content-Type')
#     users = [b.serialize() for b in db_conexao.view()]
#     if (content_type == 'application/json'):
#         json = request.json
#         for b in users:
#             if b['id'] == int(json['id']):
#                 return jsonify({
#                     # 'error': '',
#                     'data': b,
#                     'status': '200',
#                     'msg': 'Success getting all books in library!👍😀'
#                 })
#         return jsonify({
#             'error': f"Error ⛔❌! Book with id '{json['id']}' not found!",
#             'data': '',
#             'status': '404'
#         })
#     else:
#         return jsonify({
#                     # 'error': '',
#                     'data': users,
#                     'status': '200',
#                     'msg': 'Success getting all books in library!👍😀',
#                     'no_of_books': len(users)
#                 })


# @app.route('/user', methods=['GET'])
# def user_create():
#     if request.method == 'GET':
#         return render_template('cadastro.html')
#
#     if request.method == 'POST':
#         nome = request.form['name']
#         rg= request.form['rg']
#         cpf = request.form['cpf']
#         data_nascimento = request.form['bithday']
#         sexo = request.form['sex']
#         email = request.form['email']
#         senha = request.form['password']
#         # cadastro = Cadastro(nome, rg, cpf,data_nascimento,sexo, email, senha)
#         # db.session.add(cadastro)
#         # db.session.commit()
#         return redirect('/user')