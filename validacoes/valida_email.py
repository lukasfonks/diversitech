import re

class Email:
    def __init__(self, email):
        if self.valida_email(email):
            self.email = email
        else:
            raise ValueError('E-mail inválido')

    def __str__(self):
        return self.email

    def valida_email(self, email):
        padrao = '[\w\.-]{2,50}@\w{3,10}.\w{2,3}?.\w{2,3}'
        buscador = re.search(padrao, email)
        if buscador:
            return buscador
        else:
            return False


# email = 'ls_fonseca@hotmail.com'
# teste = Email(email)
# print(teste)
