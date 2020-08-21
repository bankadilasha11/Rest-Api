import xlwings as xw
import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()

code = json_data['sys']['country']
city_id = json_data['id'] 
temp = json_data['main']['temp']
humi = json_data['main']['humidity']
city_name = json_data['name'] 
des = json_data['weather'][0]['description']
deg = json_data['wind']['deg']
fah = (deg*1.8)+32  #fahreheit
cel = round((deg - 32)*5/9,1) #celsius


wbtest = xw.Book('Book1.xlsx')

ws1 = wbtest.sheets['sheet1']
ws2 = wbtest.sheets['sheet2'] 
ws3 = wbtest.sheets['sheet3']

ws1.range('A4').value = code
ws1.range('B4').value = city_id
ws1.range('C4').value = temp
ws1.range('D4').value = humi
ws1.range('E4').value = des
ws1.range('F4').value = ("C")

ws2.range('A4').value = city_name
ws2.range('B4').value = code
ws2.range('C4').value = city_id


