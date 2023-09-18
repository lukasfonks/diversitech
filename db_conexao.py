import mysql.connector

from models import Cadastro


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
               f'VALUES ("{user.nome}", "{user.rg}", "{user.cpf}", "{user.data_nascimento}", "{user.sexo}", "{user.email}", "{user.senha}")')

    cursor.execute(comando)

    conexao.commit() # edita o banco de dados

    cursor.close()
    conexao.close()


def view():
    conexao = conexao_abrir()
    users = []
    cursor = conexao.cursor()
    comando = ("SELECT * FROM db_diversitech.usuarios")

    cursor.execute(comando)

    resultado = cursor.fetchall() # ler o banco de dados

    for i in resultado:
        user = Cadastro(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        users.append(user)

    cursor.close()
    conexao.close()

    return users

def update(user):
    conexao = conexao_abrir()
    cursor = conexao.cursor()

    comando = ("UPDATE db_diversitech.usuarios SET nome= user.name, rg= user.rg, cpf= user.cpf,"
               "data_nascimento= user.data_nascimento, sexo= user.sexo, email= user.email, "
               "senha= user.senha WHERE id= user.id")
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados

    cursor.close()
    conexao.close()

def delete(id):
    conexao = conexao_abrir()
    cursor = conexao.cursor()

    comando = ('DELETE FROM db_diversitech.usuarios WHERE id= id')
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados

    cursor.close()
    conexao.close()

