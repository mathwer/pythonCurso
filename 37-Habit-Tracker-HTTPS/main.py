import requests
from datetime import datetime
from dados import dados

USUARIO = dados['usuario']
TOKEN = dados['token']


pixela_endpoint = 'https://pixe.la/v1/users'  # para criar um usuário novo

# ---------- Criando um usuario

params_user = {
    'token': TOKEN,
    'username': USUARIO,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# Vai voltar um erro, pois o usuário já foi criado
#resposta = requests.post(url=pixela_endpoint, json=params_user)

# print(resposta.text)

# ------------ Criando um gráfico

graph_endpoint = f'{pixela_endpoint}/{USUARIO}/graphs'

params_graph = {
    'id': 'a1',
    'name': 'Teste1',
    'unit': 'Km',
    'type': 'float',
    'color': 'momiji'
}

header = {
    'X-USER-TOKEN': TOKEN
}

#resposta = requests.post(url=graph_endpoint, json=params_graph, headers=header)
# print(resposta)

# --------- Criando um pixel no gráfico

pixel_endpoint = f'{pixela_endpoint}/{USUARIO}/graphs/a1'

hoje = datetime.now()

params_pixel = {
    'date': hoje.strftime('%Y%m%d'),
    'quantity': '12.9'
}

resposta = requests.post(url=pixel_endpoint, json=params_pixel, headers=header)
print(resposta)
