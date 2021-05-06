from Function_UnitConverter import UnitConverter

Conversion_Item={}


while True:
    Wert = float(input("zu konvertierende zahl (abbruch mit 0):"))
    if Wert == 0:
        break
    Conversion_Item["Wert"] = Wert
    Conversion_Item["BasisEinheit"] = input("Basiseinheit:")
    Conversion_Item["ZielEinheit"] = input("Zieleinheit:")

    Conversion_Item["Result"] = UnitConverter(Conversion_Item["BasisEinheit"], Conversion_Item["ZielEinheit"], Conversion_Item ["Wert"])

    print (Conversion_Item)