# Usando beautifulSoup e um site fornecido pelo curso

from bs4 import BeautifulSoup

with open('website.html', encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# o soup é um objeto que representa o arquivo html na sua totalidade
soup = BeautifulSoup(conteudo, 'html.parser')

# Esse método faz a identação do arquivo, para ficar com mais cara de html
# print(soup.prettify())

# print(soup.title)
print(soup.title.string)

anchor_tags = soup.find_all(name='a')

for tag in anchor_tags:

 #   print(tag.get('href'))
    pass

heading = soup.find(name='h1', id='name')
# print(heading)
# É usado class_ pois o class é uma palavra reservada do python
section_heading = soup.find(name='h3', class_='heading')

# print(section_heading)

nome = soup.select_one(selector='#name')
# print(nome)

headings = soup.select('.heading')
# print(headings)
