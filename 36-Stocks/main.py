from dados import dados
import requests
from twilio.rest import Client
from datetime import datetime, timedelta


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NKEY = dados['newsAPI']
SKEY = dados['stockKey']

TSID = dados['accountSID']
TAUTH = dados['accountKey']

sendPhone = dados['sendPhone']
telefone = dados['telefone']

# STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.

parametros = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': SKEY
}

ontem = datetime.now() - timedelta(1)
ontem = datetime.strftime(ontem, '%Y-%m-%d')

anteontem = datetime.now() - timedelta(2)
anteontem = datetime.strftime(anteontem, '%Y-%m-%d')

resposta = requests.get(STOCK_ENDPOINT, params=parametros)
resposta.raise_for_status()
data = resposta.json()
# print(data)

abertura = float(data["Time Series (Daily)"][ontem]['4. close'])
fechamento = float(data["Time Series (Daily)"][anteontem]['4. close'])

diferença = ((abertura - fechamento)/fechamento)*100


# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator

parametros = {
    'q': COMPANY_NAME,
    'apiKey': NKEY,
    'sortBy': 'relevancy',
    'pageSize': 3
}

resposta = requests.get(NEWS_ENDPOINT, parametros)
data = resposta.json()
print(data)
artigos = data['articles']

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.

for artigo in artigos:
    titulo = artigo['title']
    descricao = artigo['description']

    if diferença > 5:
        client = Client(TSID, TAUTH)
        message = client.messages.create(
            body=f'{STOCK}: 🔺{diferença}% \n Headline: {titulo} \nDescription: {descricao}',
            from_=sendPhone,
            to=telefone
        )

    if diferença < -5:
        client = Client(TSID, TAUTH)
        message = client.messages.create(
            body=f'{STOCK}: 🔻{diferença}% \n Headline: {titulo} \nDescription: {descricao}',
            from_=sendPhone,
            to=telefone
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were  HedgeFunds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
