import requests
import json
import os

response =  requests.get("http://worldtimeapi.org/api/ip")
datetime = response.json()['datetime']
date = datetime.split("T")
date[0] = date[0].split("-")
date[1] = date[1].split(":")
date[1][2] = date[1][2].split(".")
dateCommand = "date "+date[0][2] +"-"+date[0][1]+"-"+ date[0][0]
timeCommand = "time " +date[1][0] +":"+ date[1][1]+":"+date[1][2][0]
os.system(dateCommand)
os.system(timeCommand)
