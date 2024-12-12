import urllib.request
import json


def get_weather(city):
#Temperature in Sudbury
#city='sudbury'
  api='bc448800d4c0db057fde7aafc4a36d6d'
  url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
  request=urllib.request.urlopen(url)
  result=json.loads(request.read())
  temp_c=round(result['main']['temp']-273.15,2)
  return temp_c