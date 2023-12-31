import pytest
import celBr

class TestClass:

    def test_quando_telefone_recebe_71981296060_deve_retornar_formatado(self):
        entrada = '71981296060' #Given-Contexto
        esperado = '(71) 98129-6060'

        teste_resultado = celBr.validar_telefone(entrada) #When-Ação
        
        assert teste_resultado == esperado #Then-Desfecho


    def test_quando_telefone_recebe_981296060_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = '981296060'  # Given-Contexto

            teste_resultado = celBr.validar_telefone(entrada)  # When-Ação

            assert teste_resultado  # Then-Desfecho