import re


def validar_telefone(numero):
    # Remover caracteres não numéricos
    numero = re.sub(r'\D', '', numero)

    # Verificar se o número tem 11 dígitos (incluindo o DDD)
    if len(numero) != 11:
        raise Exception('Número de digitos inválido')

    # Formatar o número: (XX) 9XXXX-XXXX
    numero_formatado = f'({numero[:2]}) {numero[2:7]}-{numero[7:]}'

    return numero_formatado


# Exemplo de uso
# telefone = input("Digite o número de telefone brasileiro: ")

# numero_formatado = validar_telefone(telefone)

# if numero_formatado:
#     print(f"Número formatado: {numero_formatado}")
# else:
#     print("Número de telefone inválido.")
