#"fizzbuzz" beispiel
#Eingabe zahl zw. 1 und 100, gibt alle zahlen bis zu der eingegebenen zahl aus
# wenn ausgegebene zahl durch 3 dividierbar, dann soll "fizz" ausgegebene werden,
# wenn durch /5 "buzz"
# wenn beides zutrifft "fizzbuzz"


end_zahl = int(input("Zahl zw. 1 und 100 eingeben"))

for y in range(1, end_zahl + 1): # 1 = startwert, falls mit dem schleifen-zähler weiter gerechnet werden soll
    if y % 3 == 0 and y % 5 == 0: #Modulo Operator % --> gibt den restwert einer division zurück
        print("fizzbuzz")
    elif y % 3 == 0:
        print("fizz")
    elif y % 5 == 0:
        print("buzz")
    else:
        print(y)





