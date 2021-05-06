#while-oops
# läuft solange bis break
import random

secret = random.randint(1, 20)



while True:
    guess = int(input("zahl raten"))
    if secret != guess:
        print("Falsch geraten - nochmal")
    else:
        print ("Richtig!")
        break