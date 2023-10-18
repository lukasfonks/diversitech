import re

class TelefonesBr:

    def __init__(self, telefone):
        if self.procura_tel(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número inválido')

    def __str__(self):
        return self.formata_tel()

    def procura_tel(self, telefone):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        buscador = re.search(padrao, telefone)
        if buscador:
            return True
        else:
            return False

    def formata_tel(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        buscador = re.search(padrao, self.numero)
        telFormatado = f'+{buscador.group(1)}({buscador.group(2)}){buscador.group(3)}-{buscador.group(4)}'
        return telFormatado
