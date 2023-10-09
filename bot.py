import time
import pyautogui
import pandas as pd
import pyperclip

pyautogui.PAUSE = 0.5 #Define tempo de espera entre cada comando

tabela = pd.read_json('data_usuarios')


# Abrir Sistema
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.click(x=373, y=76)
pyautogui.write('http://localhost:3000/')
pyautogui.press('enter')

time.sleep(2) #tempo de espera para carregar

# Fazer login
pyautogui.click(x=773, y=483)
pyautogui.write("ls_fonseca@hotmail.com")
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')

# loop de cadastro
for linha in tabela.index:
    
    pyautogui.click(x=307, y=258, clicks=3)
    nome = str(tabela.loc[linha, 'nome']) #procura na linha da tabela 'nome' e grava como str na variavel
    pyperclip.copy(nome) # Copiar o texto para a área de transferência
    pyautogui.hotkey('ctrl', 'v') #cola o texto
#     A solução acima foi usada para que o caracter especial dos nomes seja colado corretamente
#     A função .write não escreve caracteres especiais
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'rg']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'cpf']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'data_nascimento']))
    pyautogui.press('tab')
    if tabela.loc[linha, 'sexo'] == 'Masculino':
            # Campo já inicia marcado como masculino, logo não precisa executar nada
            pyautogui.press('tab')
    elif tabela.loc[linha, 'sexo'] == 'Feminino':
            pyautogui.press('down')
            pyautogui.press('tab')
    else:
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('tab')
    
    pyautogui.write(str(tabela.loc[linha, 'email']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'senha']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.scroll(200) #Retorna barra de rolagem pra cima