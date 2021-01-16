import requests

res = requests.get(url='https://api.kanye.rest')

data = res.json()
print(data)
