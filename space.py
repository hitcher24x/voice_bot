import requests
import json

url = 'http://api.open-notify.org/astros.json'
data = requests.get(url).json()
print(data)

