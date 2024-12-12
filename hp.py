import urllib.request
import json
import random

def get_char():
  #Characters in Harry Porter
  url=f'https://hp-api.herokuapp.com/api/characters'
  request=urllib.request.urlopen(url)
  result=json.loads(request.read())
  #print(result)
  char = random.randint(1,40)
  print(char)

  if result[char]["wizard"]== True:
    return f"{result[char]['name']} is in the house wizard and the actor is {result[char]['actor']} and the picture of the character is {result[char]['image']}"

  else:
    return f"{result[char]['name']} is not in the house wizard and the actor is {result[char]['actor']} and the picture of the character is {result[char]['image']}"
