import requests

# Api JsonPlaceholder
link = 'https://jsonplaceholder.typicode.com/posts/1'

# requisicao GET
requisicao = requests.get(link)
print(requisicao.status_code)

# exemplo de tratamento
if requisicao.status_code == 200:
    print(requisicao.json())    
else:
    print('Erro na requisição')
    print(requisicao.text)

# pegar os dados

resposta_json = requisicao.json()
print(resposta_json)