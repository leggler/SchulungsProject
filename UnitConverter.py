#ewige schleife mit abfrage was umgerechnet werden soll zb kWh in kJ = "a", kJ in kWh "b"
#input(), while: while True: etc schleifen
ZwischenZahl = 0.0 #einheit = kWh
ZielZahl = 0.0

while True:
    Zahl = float(input("zu konvertierende zahl (abbruch mit 0):"))
    if Zahl == 0:
        break
    BasisEinheit = input("Basiseinheit (kWh oder kJ):")
    ZielEinheit = input("Zieleinheit: (kWh oder kJ)")

    #Umrechnung in Zwischeneinheit kWh
    if BasisEinheit == "kWh":
        ZwischenZahl = Zahl
    elif BasisEinheit == "kJ":
        ZwischenZahl = Zahl / 3600
    else:
        print("Unbekannte Basis Einheit - break")
        break

    #Umrechnung Zwischeneinheit in Zieleinheit
    if ZielEinheit == "kWh":
        ZielZahl = ZwischenZahl
    elif ZielEinheit == "kJ":
        ZielZahl = ZwischenZahl * 3600
    else:
        print("Unbekannte Ziel Einheit - break")
        break

    print(f"Eingegebene Zahl: {Zahl} {BasisEinheit}; Ergebnis: {ZielZahl} {ZielEinheit}")

    with open("Calculator_log.txt", "a") as calc_log:
        calc_log.write(f"Eingegebene Zahl: {Zahl} {BasisEinheit}; Ergebnis: {ZielZahl} {ZielEinheit}\n")
