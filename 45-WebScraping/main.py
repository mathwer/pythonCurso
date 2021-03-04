from bs4 import BeautifulSoup
import requests

# Usando uma versão de webarchive, pois houve uma modificação no site onde ele não retorna os títulos.
response = requests.get(
    'https://web.archive.org/web/20200514054348/https://www.empireonline.com/movies/features/best-movies-2/')
text = response.text
site = BeautifulSoup(text, 'html.parser')

filmes = site.find_all(name='h3')
# print(filmes)

melhores_filmes = [filme.getText() for filme in filmes]
melhores_filmes.reverse()
# print(melhores_filmes)

with open('filmes.txt', 'w') as arquivo:
    for filme in melhores_filmes:
        arquivo.write(filme)
        arquivo.write('\n')
