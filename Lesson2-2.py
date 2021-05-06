#for-loop
#läuft eine gewisse anzahl oft durch
secret = 23
x=2

for x in range(4): #x beginnt bei 0 - und zählt bis 9
    guess = int(input("zahl raten"))
    if secret == guess:
        print ("Richtig!")
        break
    else:
        print("Falsch geraten - nochmal")

print(x)
