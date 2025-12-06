import requests

# cotação de dólar
link = 'https://www.google.com/search?q=cotacao+dolar'
requisicao = requests.get(link)
print(requisicao.status_code)
print(requisicao.text) 

