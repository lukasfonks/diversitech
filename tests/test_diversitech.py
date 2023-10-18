from telefonesBr import TelefonesBr

class TestClass:
    def test_quando_telefone_recebe_7133812599_deve_retornar_7133812599_validado_e_formatado(self):
        entrada = '7133812599' #Given-Contexto
        esperado = '(71)3381-2599'

        telefone_teste_resultado = TelefonesBr(entrada)
        
        assert telefone_teste_resultado == esperado

