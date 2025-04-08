import pyautogui
import time
import pandas

# passo 1: entrar no sistema da Organização
# passo 2: Login
# passo 3: Importar a base de dados
# passo 4: cadastrar 1 produto
# Passo 5: repetir
# pyautogi - permite fazer automacao
# pyautogi.hotkey("ctrl","c") - combinação de teclas

site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
# Entre todos os comandos realiza um Pause
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(site)
pyautogui.press('enter')

# Espera 2 segundos
time.sleep(2)

# Evento de Click
pyautogui.click(x=490, y=406)
pyautogui.write("python3@gmail.com")
pyautogui.press('tab')
pyautogui.write("123456()*)T1239123")
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

# Importando a Base de Dados
tabela = pandas.read_csv('Automacao-de-tarefas\\produtos.csv')
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=442, y=288)

    # Preenchendo Dados
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press('tab')


    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press('tab')


    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')


    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

    # Scroll
    pyautogui.scroll(10000)
