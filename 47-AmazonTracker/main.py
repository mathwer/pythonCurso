# Avisador de preço quando um produto da amazon cair abaixo do preço especificado.

import requests
from bs4 import BeautifulSoup
import smtplib

response = requests.get('https://www.amazon.com.br/Driving-Logitech-Joysticks-Controles-Computador/dp/B00Z0UWV3O/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=TLDBH959NPE4&dchild=1&keywords=cambio+g29&qid=1615990818&sprefix=cambio+%2Caps%2C381&sr=8-1',
                        headers={'Accept-Language': 'en-US,en;q=0.9', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})
text = response.text
site = BeautifulSoup(text, 'html.parser')

nome = site.find(id="productTitle").get_text().strip()

preco = site.find(name='span', class_='priceBlockSavingsString')
# print(preco)
preco = float(preco.getText().split('$')[1].replace(',', '.'))
print(preco)
print(nome)


# Pode usar o pacote smtp para enviar email pra você quando o valor estiver baixo
if preco <= 330:
    print(f'Preço está {preco}, compre agora!')

    # with smtplib.SMTP('o smtp do seu email aqui') as connection:
    #     email_user = 'Seu email aqui'
    #     senha = 'sua senha aqui '
    #     connection.starttls()
    #     connection.login(user=email_user, password=senha)
    #     connection.sendmail(from_addr=email_user, to_addr=email_user,
    #                         msg=f'Subject: Preço Baixo! \n\n O preço de {nome} está {preco}! Corre lá!')
