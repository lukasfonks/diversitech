# from validacoes.valida_cep import BuscaEndereco
# from validacoes.valida_cpf import DocCpf
# from validacoes.valida_email import Email

# class Login:
#     def __init__(self, cpf, senha):
#         self.cpf = cpf
#         self.senha = senha

# class Recrutadores:
#     def __init__(self, cpf, nome, email, senha, empresa):
#         self.cpf = DocCpf(cpf)
#         self.nome = nome
#         self.email = Email(email)
#         self.senha = senha
#         self.empresa = empresa

#     def __str__(self):
#         return (f'CPF:{self.cpf}\n'
#                 f'NOME:{self.nome}\n'
#                 f'EMAIL:{self.email}\n'
#                 f'EMPRESA:{self.empresa}')

class Candidatos:
    def __init__(self, cpf, nome, email, senha, endereco, bairro,
                 cidade, estado, cep, sexo, data_nascimento, profissao):
        self.cpf = DocCpf(cpf)
        self.nome = nome
        self.email = Email(email)
        self.senha = senha
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = BuscaEndereco(cep)
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.profissao = profissao

    def __str__(self):
        return (f'CPF:{self.cpf}\n'
                f'NOME:{self.nome}\n'
                f'EMAIL:{self.email}\n'
                f'ENDEREÇO:{self.endereco}, BAIRRO:{self.bairro}, CIDADE:{self.cidade}, ESTADO:{self.estado}\n'
                f'SEXO: {self.sexo}\n'
                f'DATA DE NASCIMENTO:{self.data_nascimento}\n'
                f'PROFISSÃO:{self.profissao}')

class Vagas:
    def __init__(self, empresa, descricao_vaga, qtd, localidade, modalidade, remuneracao, nivel_cargo, beneficios):
        self.empresa = empresa
        self.descricao_vaga = descricao_vaga
        self.qtd = qtd
        self.localidade = localidade
        self.modalidade = modalidade
        self.remuneracao = remuneracao
        self.nivel_cargo = nivel_cargo
        self.beneficios = beneficios

    def __str__(self):
        return (f'EMPRESA:{self.empresa}\n'
                f'DESCRIÇÃO DA VAGA:{self.descricao_vaga}\n'
                f'QUANTIDADE:{self.qtd}\n'
                f'LOCALIDADE:{self.localidade}\n'
                f'MODALIDADE:{self.modalidade}\n'
                f'REMUNERAÇÃO:{self.remuneracao}\n'
                f'NIVEL DO CARGO:{self.nivel_cargo}\n'
                f'BENEFÍCIOS:{self.beneficios}')

# objeto_recrutador = Recrutadores('66434331932', 'Lucas Fonks', 'ls.fonseca@hotmail.com', '1234', 'DIversitech')
# print(objeto_recrutador)

# objeto_candidato = Candidatos('66434331932', 'Lukas Fonks', 'ls-fonseca@hotmail.com',
#                               '1234', 'Rua Nilson','vila laura', 'salvador', 'BA',
#                               '40270550', 'M', '05/11/1992', 'engneheriro')
# print(objeto_candidato)

# objeto_vaga = Vagas('Diversitech', 'Vaga para Desenvolvedor JR', '02', 'Salvador', 'Hibrido', 2000.0, 'Jr', 'Cartao Alimentação')
# print(objeto_vaga)
