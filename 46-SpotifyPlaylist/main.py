# Esse programa cria uma playlist baseada nas músicas mais tocadas emm um dia específico de acordo com o site billboard

import requests
from bs4 import BeautifulSoup
from dados import dados
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

pp = pprint.PrettyPrinter(indent=4)

# ------- Pegando as músicas

data = input('Qual o dia da sua playlist? (YYYY-MM-DD): ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{data}')
texto = response.text
site = BeautifulSoup(texto, 'html.parser')

musicas = site.find_all(name='span', class_='chart-element__information__song')
artistas = site.find_all(
    name='span', class_='chart-element__information__artist')

lista_musicas = [musica.getText() for musica in musicas]
lista_artistas = [artista.getText() for artista in artistas]
# print(lista_musicas)


# ------- Parte do Spotify

client_id = dados['client_id']
client_secret = dados['client_secret']
redirect_url = 'http://example.com'

scope = 'playlist-modify-private'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url, show_dialog=True))

user_id = sp.current_user()["id"]

i = 0
sp_musicas = []
ano = data.split('-')[0]
for musica in lista_musicas:
    artista = lista_artistas[i]
    musica_sp = sp.search(
        q=f'track:{musica} year:{ano}', type="track")
    try:
        uri = musica_sp["tracks"]["items"][0]["uri"]
        sp_musicas.append(uri)
        print(uri)

    except:
        print('Erro ao procurar a música, ela não existe no spotify')

    i += 1

usuario = sp.current_user()
pp.pprint(sp_musicas)

playlist = sp.user_playlist_create(
    user=usuario['id'], public=False, name=f'{data} Billboard', description=f'As músicas que estavam em alta no dia {data}.')

sp.playlist_add_items(
    playlist_id=playlist['id'], items=sp_musicas)
