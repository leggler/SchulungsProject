#while-oops
# läuft solange das while-statement true ist
secret = 23
guess = 0


while (secret != guess):
    guess = int(input("zahl raten"))
    if secret != guess:
        print("Falsch geraten - nochmal")
    else:
        print ("Richtig!")



