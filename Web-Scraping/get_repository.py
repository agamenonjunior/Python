import requests

# Mapeando Informações de Repositórios do GitHub
headers = {'X-GitHub-Api-Version': '2022-11-28'}
base_api_url = "https://api.github.com"
user = "google"
url = f'{base_api_url}/users/{user}/repos'

# Fazendo a requisição GET para obter os repositórios do usuário
response = requests.get(url, headers=headers)
print(response.status_code)

print("Quantidade de repositórios:", len(response.json()))
for repository in response.json():
    print("Nome do repositório:", repository['name'])
    print("Descrição:", repository['description'])
    print("Linguagem principal:", repository['language'])
    print("URL do repositório:", repository['html_url'])
    print("Data de criação:", repository['created_at'])
    print("Última atualização:", repository['updated_at'])
    print("-" * 40)