import mysql.connector

from models import Cadastro

def login(email, senha):
    conexao = conexao_abrir()
    user = {}
    cursor = conexao.cursor()
    # seleciona do banco de dados todos usuarios que possuem o email e senha passados
    comando = (f'SELECT * FROM db_diversitech.usuarios WHERE email="{email}" and senha="{senha}"')
    cursor.execute(comando)

    i = cursor.fetchall() # ler o banco de dados
    # valida se recebeu alguma informação de volta do banco de dados
    if len(i) > 0:
        # Pega apenas o primeiro item da lista retornada. Organiza na classe Cadastro,
        # aplica o método serialize e retorna pro views.py
        i = i[0]
        user = Cadastro(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
        user = user.serialize()
       
    cursor.close()
    conexao.close()

    return user

def conexao_abrir():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='db_diversitech',
    )
    return conexao

def insert(user):
    conexao = conexao_abrir()

    cursor = conexao.cursor()
    comando = (f'INSERT INTO usuarios (nome, rg, cpf, data_nascimento, sexo, email, senha) '
               f'VALUES ("{user.nome[0]}", "{user.rg[0]}", "{user.cpf[0]}", "{user.data_nascimento[0]}", "{user.sexo[0]}", "{user.email[0]}", "{user.senha}")')

    cursor.execute(comando)

    conexao.commit() # edita o banco de dados

    cursor.close()
    conexao.close()
    return comando

def view():
    conexao = conexao_abrir()
    users = []
    cursor = conexao.cursor()
    comando = ("SELECT * FROM db_diversitech.usuarios")
    cursor.execute(comando)

    resultado = cursor.fetchall() # ler o banco de dados

    for i in resultado:
        user = Cadastro(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
        users.append(user)

    cursor.close()
    conexao.close()

    return users

def update(user):
    conexao = conexao_abrir()
    cursor = conexao.cursor()

    comando = (f'UPDATE db_diversitech.usuarios SET nome="{user.nome[0]}", rg="{user.rg[0]}", '
               f'cpf="{user.cpf[0]}", data_nascimento="{user.data_nascimento[0]}", sexo="{user.sexo[0]}", '
               f'email="{user.email[0]}", senha="{user.senha}" WHERE id= {user.id}')
    
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados

    cursor.close()
    conexao.close()
       # return user

def delete(id):
    conexao = conexao_abrir()
    cursor = conexao.cursor()

    comando = (f"DELETE FROM db_diversitech.usuarios WHERE id={id}")
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados

    cursor.close()
    conexao.close()