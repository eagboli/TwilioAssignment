import urllib.request
import json

def people_space():
#Number of People in Space
  url='http://api.open-notify.org/astros.json'
  request=urllib.request.urlopen(url)
  result=json.loads(request.read())
  return(f"There are {result['number']} people in space right now")