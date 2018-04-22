import requests

api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid=748c43a69b737e8b0c4eee77214db49f&q='
city = input("City Name:")

url = api_adress + city

json_data = requests.get(url).json()

print(json_data)