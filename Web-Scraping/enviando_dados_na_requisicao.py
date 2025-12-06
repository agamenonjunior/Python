import requests

# 1 - dados em dicionário
dados = {
    'userId': 1,
    'id': 1,
    'title': 'Meu primeiro post',
    'body': 'Conteúdo do meu primeiro post'
}

# 2 - endpoint da API
link = 'https://jsonplaceholder.typicode.com/posts'

# 3 - enviando os dados via POST
requisicao = requests.post(link, json=dados)

print(requisicao.status_code)

# 4 - mostrando a resposta da requisição
resposta_json = requisicao.json()
print(resposta_json)
for chave, valor in resposta_json.items():
    print(f'{chave}: {valor}')