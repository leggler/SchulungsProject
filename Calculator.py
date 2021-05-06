#taschenrechner

int_eins = int(input("erste zahl:"))
int_zwei = int(input("zweite zahl:"))
operation = input("bitte geben sie 'A' für addition und 'S' für Substraktion ein")
if operation == "A":
    result = int_eins + int_zwei
elif operation == "S":
    result = int_eins - int_zwei
else:
    print("Falscher Operant eingegeben")

print(result)
