import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'country=fr&'
       'apiKey=1c87776f5070430ebd76a0910326f28e')
response = requests.get(url)
print(response.json)
