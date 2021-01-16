import requests

res = requests.get(url='http://api.open-notify.org/iss-now.json')

if res.status_code != 200:
    raise Exception('Bad response from ISS API')

# Colocando em JSON
data = res.json()
# print(data)

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

posicao_iss = (longitude, latitude)
