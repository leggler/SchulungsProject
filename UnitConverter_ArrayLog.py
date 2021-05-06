#ewige schleife mit abfrage was umgerechnet werden soll zb kWh in kJ = "a", kJ in kWh "b"
#input(), while: while True: etc schleifen

import json


#Conversion_Item = {"Wert": 8.5, "BasisEinheit": "KWh/kJ", "ZielEinheit": "kWh/kJ", "ZielWert": 555.22}
#Conversion_List = [Conversion_Item1, ConversionItem2...]

Conversion_Item = {}
Conversion_List = []


while True:
    Wert = float(input("zu konvertierende zahl (abbruch mit 0):"))
    if Wert == 0:
        break
    Conversion_Item["Wert"] = Wert
    Conversion_Item["BasisEinheit"] = input("Basiseinheit (kWh oder kJ):")
    Conversion_Item["ZielEinheit"] = input("Zieleinheit: (kWh oder kJ)")

    #Umrechnung in Zwischeneinheit kWh
    if Conversion_Item["BasisEinheit"] == "kWh":
        ZwischenZahl = Conversion_Item["Wert"]
    elif Conversion_Item["BasisEinheit"] == "kJ":
        ZwischenZahl = Conversion_Item["Wert"] / 3600
    else:
        print("Unbekannte Basis Einheit - break")
        break

    #Umrechnung Zwischeneinheit in Zieleinheit
    if Conversion_Item["ZielEinheit"] == "kWh":
        Conversion_Item["ZielWert"] = ZwischenZahl
    elif Conversion_Item["ZielEinheit"] == "kJ":
        Conversion_Item["ZielWert"] = ZwischenZahl * 3600
    else:
        print("Unbekannte Ziel Einheit - break")
        break

    with open("Calculator_log.txt", "a") as calc_log:
        calc_log.write(json.dumps(Conversion_Item))
        calc_log.write(",\n")




#PROBLEM: Append() überschreibt ALLE Items in List --> wert wird nur referenziert!
#    print(Conversion_List)
#    print(Conversion_Item)
#    Conversion_List.append(Conversion_Item)
#    print(Conversion_List)

#with open("Calculator_log.txt", "w") as calc_log: #"w" zum überschreiben, "a" zum appenden
#    calc_log.write(json.dumps(Conversion_List))
