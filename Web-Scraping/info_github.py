import requests

# consumindo API do github - API Events
link = "https://api.github.com/events"
response = requests.get(link)

if response.status_code == 200:
    print(response.json())

# verificando versao da API
version = 'https://api.github.com/versions'
version_response = requests.get(version)
print("Versão da API:",version_response.json())




