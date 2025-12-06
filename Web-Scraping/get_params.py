import requests

# 1 - API JsonPlaceholder com parâmetros na URL
link = 'https://jsonplaceholder.typicode.com/posts' 

# 2- adicionando o payload com os parâmetros
payload = {
    'id': [ 1,2,3,4,5],
    'userId': 1    
    
}

# 3 - requisição GET com parâmetros
requisicao = requests.get(link, params = payload)

print(requisicao)

# 4 - mostrando a requisição completa
requisicao_json = requisicao.json()
for i in requisicao_json:
    print('\n')
    print(i)