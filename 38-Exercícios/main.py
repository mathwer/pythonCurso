import requests
from datetime import datetime
from dados import dados

# APIS utilizadas: nutritionix / sheety

APP_ID = dados['nutrition_ID']
APP_KEY = dados['nutrition_KEY']
URL = dados['url']


#  ---------   Pegando as informações do exercício

nutrition_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercicio_feito = input('Tell me what you did: ')

params = {
    'query': exercicio_feito,
    'gender': 'male'
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'Content-Type': 'application/json'
}

res = requests.post(nutrition_endpoint, headers=headers, json=params)
res = res.json()

# ---------  Colocando na planilha do google

hoje = datetime.now()
hora = hoje.strftime('%H:%M')
dia = hoje.strftime('%d/%m/%Y')


for exercise in res['exercises']:
    planilha = {
        'workout': {
            "date": dia,
            "time": hora,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


# --------- Incluindo alguma segurança
header = {
    'Authorization': dados['auth']
}

p_res = requests.post(url=URL, json=planilha, headers=header)
print(p_res.text)
