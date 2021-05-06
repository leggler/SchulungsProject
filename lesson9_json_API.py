#direktes abfragen von infos aus einem json file über eine API

import json
#methode um link zu öffnen
from urllib.request import urlopen

#markus' API key
api_key="b01eaa00b72871f9b6a8927402389b58"

#lukas eigener account: leggler@gmail.com LKS3ggl3r
api_key="1ce31b4c36695fac98f0803d6038026a"

response = urlopen("http://api.openweathermap.org/data/2.5/weather?q=Paris&appid="+api_key).read()
print(response)

#json.load --> öffnet ein file
#json.loads --> öffnet einen string
data = json.loads(response)

#falls encoding einen fehler bringt, kann man den return string auch noch decodieren
#data = json.loads(response.decode('utf-8'))

print(data["weather"])
print(data["weather"][0]) #"weather" ist ein array von dictionaries
print(data["weather"][0]["description"])

print(data["main"])
