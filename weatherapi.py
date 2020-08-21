import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()

city_id = json_data['id'] 
temp = json_data['main']['temp']
humi = json_data['main']['humidity']
des = json_data['weather'][0]['description']
deg = json_data['wind']['deg']
fah = (deg*1.8)+32  #fahreheit
cel = round((deg - 32)*5/9,1) #celsius

if fah != fah:
    print("F")
else:
    print("C")


print(city_id,temp,humi, des)
