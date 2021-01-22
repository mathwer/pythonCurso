import requests


def criar_questoes():
    data = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')

    data = data.json()
    # print(data)

    questoes = data['results']

    return questoes
