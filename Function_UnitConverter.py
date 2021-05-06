#homework: unit converter als funktion bauen
#aus seperater datei in einer schleife starten
#evtl. mit eigener funktion als .json oder .jsonl in datei schreiben



def UnitConverter (BaseUnit, TargetUnit, BaseNumber):
    ValidUnits = ("kWh", "kJ", "BTU", "kCal", "BTU")
    Conversion_Factors_2_kWh = {"kWh": 1, "kJ": 1/3600, "BTU": 0.000293071, "kCal": 0.00116222}
    Conversion_Factors_from_kWh = {"kWh": 1, "kJ": 3600, "BTU": 3412.14, "kCal": 860.421}
    #ToDo: Umwandlungskoeffizienten aus externem file lesen
    #ToDo: function könnte in kleinere brocken zerteilt werden (unit test, berechnung)

    if not ((BaseUnit in ValidUnits) & (TargetUnit in ValidUnits)):
        error = print("error: Einheiten nicht erkannt")
        return error
    #print("no error")


    #Umrechnung in Zwischeneinheit kWh
    zwischen_zahl = BaseNumber * Conversion_Factors_2_kWh[BaseUnit]
    #print("Zwischenzahl: " + str(zwischen_zahl))

    #Umrechung in Zieleinheit
    result_number = zwischen_zahl *Conversion_Factors_from_kWh [TargetUnit]



    #print( f"Base unit: {BaseUnit}, BaseNumber: {BaseNumber}, TargetUnit: {TargetUnit},  Result: {result_number}")
    return result_number

def main():
    #test
    print (UnitConverter("kCal", "kWh", 100))


if __name__ == "__main__":
    main()