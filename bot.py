import pyautogui
import pandas as pd

pyautogui.PAUSE = 1 #Define tempo de espera entre cada comando

tabela = pd.read_json('data_usuarios')

# Abrir Sistema
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('http://localhost:3000/')
pyautogui.press('enter')

time.sleep(3) #tempo de espera para carregar

# Fazer login
pyautogui.click('loc do mouse')
pyautogui.write("ls_fonseca@hotmail.com")
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')

for linha in tabela.index:
    pyautogui.click('loc do mouse')
    pyautogui.write(str(tabela.loc[linha, 'nome'])) #procura na linha da tabela 'nome' e escreve no campo
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'rg']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'cpf']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'data_nascimento']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'sexo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'email']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'senha']))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(-200) #Retorna barra de rolagem pra cima





