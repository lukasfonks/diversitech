from validate_docbr import CPF,CNPJ

class Documento:

    @staticmethod
    def tipoDoc(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade digitos invalida')

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

class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido')

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        verificador = CNPJ()
        return verificador.validate(documento)

    def formata(self):
        fatia_um = self.cnpj[:2]
        fatia_dois = self.cnpj[2:5]
        fatia_tres = self.cnpj[5:8]
        fatia_quatro = self.cnpj[8:12]
        fatia_cinco = self.cnpj[12:14]
        return f'{fatia_um}.{fatia_dois}.{fatia_tres}/{fatia_quatro}-{fatia_cinco}'
