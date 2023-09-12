from app import db
class Cadastro(db.Model):
    nome = db.Column(db.String(50), nullable=False)
    rg = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(20), primary_key=True, nullable=False)
    data_nascimento = db.Column(db.String(20), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(45), nullable=True)

    def __init__(self, nome, rg, cpf, data_nascimento, sexo, email, senha):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.email = email
        self.senha = senha

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

    def __repr__(self):
        return '<Name %r>' % self.name