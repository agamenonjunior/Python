import pyautogui
# passo 1: entrar no sistema da Organização
# passo 2: Login
# passo 3: Importar a base de dados
# passo 4: cadastrar 1 produto
# Passo 5: repetir
# pyautogi - permite fazer automacao
# pyautogi.hotkey("ctrl","c") - combinação de teclas

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')