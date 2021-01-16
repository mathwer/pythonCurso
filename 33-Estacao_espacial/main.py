import requests
from datetime import datetime
import time
import smtplib

LAT_RIO = -22.906847
LONG_RIO = -43.172897


parametros = {
    'lat': LAT_RIO,
    'lng': LONG_RIO,
    'formatted': 0
}


def noite():
    res = requests.get(
        url='https://api.sunrise-sunset.org/json', params=parametros)
    res.raise_for_status()

    data = res.json()
    # print(data)
    nascer_sol = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    print(nascer_sol)
    por_sol = int(data['results']['sunset'].split('T')[1].split(':')[0])

    hora_agora = datetime.now()

    if hora_agora >= por_sol or hora_agora <= nascer_sol:
        return True


# Vendo se a IRSS está passando pelo Rio
def irss_perto():
    res = requests.get(url='http://api.open-notify.org/iss-now.json')
    res.raise_for_status()
    if res.status_code != 200:
        raise Exception('Bad response from ISS API')

    # Colocando em JSON
    data = res.json()
    # print(data)

    irss_longitude = float(data['iss_position']['longitude'])
    irss_latitude = float(data['iss_position']['latitude'])

    posicao_iss = (irss_longitude, irss_latitude)

    if LONG_RIO - 5 <= irss_longitude <= LONG_RIO + 5 and LAT_RIO - 5 <= irss_latitude <= LAT_RIO + 5:
        return True


def enviar_email():
    pass


procurar_irss = True
while procurar_irss:
    irss_perto() and noite()
    time.sleep(60)
