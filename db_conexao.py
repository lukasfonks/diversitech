import mysql.connector

from models import Cadastro


def conexaoAbrir():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='db_diversitech',
    )
    return conexao

def insert(user):
    conexao = conexaoAbrir()

    cursor = conexao.cursor()
    comando = (f'INSERT INTO usuarios (nome, rg, cpf, data_nascimento, sexo, email, senha) '
               f'VALUES ("{user.nome}", "{user.rg}", "{user.cpf}", "{user.data_nascimento}", "{user.sexo}", "{user.email}", "{user.senha}")')

    cursor.execute(comando)

    conexao.commit() # edita o banco de dados

    cursor.close()
    conexao.close()


def view():
    conexao = conexaoAbrir()
    users = []
    cursor = conexao.cursor()
    comando = ("SELECT * FROM db_diversitech.usuarios")

    cursor.execute(comando)

    resultado = cursor.fetchall()

    for i in resultado:
        user = Cadastro(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        users.append(user)

    cursor.close()
    conexao.close()

    return users

# READ

# comando = f'SELECT * FROM vagas'
#
# cursor.execute(comando)
#
# resultado = cursor.fetchall() # ler o banco de dados
#
# print(resultado)

#
# # UPDATE
#
# quantidade = 3
#
# comando = f'UPDATE vagas SET quantidade = {quantidade} WHERE ID_VAGA = "{1}"'
#
# cursor.execute(comando)
#
# conexao.commit() # edita o banco de dados

#

#
# # DELETE

# nome_produto = "todynho"
#
# comando = f'DELETE FROM vagas WHERE ID_VAGA = "{2}"'
#
# cursor.execute(comando)
#
# conexao.commit() # edita o banco de dados

