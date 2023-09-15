from validate_docbr import CPF

class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido')

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        verificador = CPF()
        return verificador.validate(documento)

    def formata(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'