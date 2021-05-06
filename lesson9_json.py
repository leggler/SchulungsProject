import json

# Bsp. json file wurde lokal herunter geladen

# filestream öffenen
with open("lesson9_example.json") as file:
# daten laden
    data = json.load(file)

# alles unformatiert printen
print(data)

# zugriff auf spezifische keys im json
# kann gesehen werden wie ein filter, mit dem man durch die ebenen des jsons durch switchen kann
print(data["quiz"]["sport"]["q1"])
print(data["quiz"]["sport"]["q1"]["question"])
print(data["quiz"]["sport"]["q1"]["options"])
print(data["quiz"]["sport"]["q1"]["answer"])




#direktes anzapfen von jsons über API  End Point




