import pyautogui
import time
# passo 1: entrar no sistema da Organização
# passo 2: Login
# passo 3: Importar a base de dados
# passo 4: cadastrar 1 produto
# Passo 5: repetir
# pyautogi - permite fazer automacao
# pyautogi.hotkey("ctrl","c") - combinação de teclas

# Entre todos os comandos realiza um Pause
pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Espera 2 segundos
time.sleep(2)

# Evento de Click
pyautogui.click(x=490, y=406)
pyautogui.write("python3@gmail.com")
pyautogui.press('tab')
pyautogui.write("123456")
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

