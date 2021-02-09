from config import dados  # Esses dados não foram para o git por questões de segurança
import requests
from twilio.rest import Client


apiKey = dados['apiKey']
lat = dados['lat']
long = dados['long']
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
sendPhone = dados['sendPhone']
telefone = dados['telefone']
TSID = dados['accountSID']
TAUTH = dados['accountKey']

parametros = {
    'lat': lat,
    'lon': long,
    'appid': apiKey,
    'exclude': 'minutely,daily,current'
}

resposta = requests.get(OWM_Endpoint, params=parametros)
resposta.raise_for_status()
data = resposta.json()

# print(data)
vai_chover = False
i = 0
for hora in data['hourly'][:12]:

    if hora['weather'][0]['id'] < 700:
        vai_chover = True

if vai_chover:
    client = Client(TSID, TAUTH)
    message = client.messages.create(
        body='Hoje a previsão é pra chuva ☂️',
        from_=sendPhone,
        to=telefone
    )
print(message.status)
