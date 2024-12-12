from flask import Flask, render_template
import urllib.request
import json
import random
from space import people_space
from weather import get_weather
from hp import get_char

app = Flask('app')

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/sms')
def send_sms(): 
  #this is the space all the code is pasted
  import os
  from twilio.rest import Client
  account_sid = os.environ["TWILIO_ACCOUNT_SID"]
  auth_token = os.environ["TWILIO_AUTH_TOKEN"]
  client = Client(account_sid, auth_token)

  student = {
      "Emml": {
          "name": "Emml",
          "number": "+17059889043", #Virtual number
          "lucky": random.randint(1, 100),
          "location": "sudbury"
      },
      "Hajia": {
          "name": "Hajia",
          "number": "+17059889043",
          "lucky": random.randint(1, 100),
          "location": "accra"     
      }  
  }
  for key, value in student.items():
    msg=f'Hello {value["name"].title()}, your lucky number is {value["lucky"]} and {people_space()}. The temperature in {value["location"].title()} is {get_weather(value["location"])}C, and the HP Character details {get_char()}'

  print(msg)
  message = client.messages.create(
     body=msg,
     from_="+19382044277", #is my virtual number
     to=value["number"], #receiver's number
  )
  with open('message.json','w') as outfile: #saving the file
    json.dump(message.sid,outfile)

  print(message.body)
  return render_template("success.html")
  
app.run(host='0.0.0.0', port=8080)
