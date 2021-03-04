from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
text = response.text
site = BeautifulSoup(text, 'html.parser')

links = site.find_all(name='a', class_='storylink')

nomes_artigos = []
link_artigos = []

for link in links:
    nome = link.string
    url = link.get('href')
    nomes_artigos.append(nome)
    link_artigos.append(url)

votos = [int(voto.getText().split()[0])
         for voto in site.find_all(name='span', class_='score')]

indice_max = votos.index(max(votos))

melhor_artigo = [nomes_artigos[indice_max],
                 link_artigos[indice_max], votos[indice_max]]

print(melhor_artigo)
