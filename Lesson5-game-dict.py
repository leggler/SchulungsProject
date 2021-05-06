
#[09:39] Elisabeth Böck working, full code
import random # importiert fertige funktionen/bibliotheken
import json #lesen, schreiben, bearbeiten von key-value pairs
import datetime

current_time = datetime.datetime.now()
print (current_time)


secret = random.randint(1, 30)
# bool_a = True # als Steuervariable, dann while bool_a und bool_a = False als Ausstieg
attempts = 0


with open("lesson5-game-score.txt","r") as score_file:
    score_list = json.loads(score_file.read()) #bei einem leeren file muss [] sein damit json lesen kann
#    score_list.sort()
#    print("Top scores:" + str(score_list[:2]))  # [:3] --> erste drei elemente der lsite; [3:] --> alle ab dem dritten element;

print("Top Scores:")
for score_element in score_list: #score_list ist jetzt ein dictionary, und kann nicht mehr
    print("  versuche:" + str(score_element["attempts"]) + ", Timestamp:" + score_element.get("date")) #.get() ist gleich zum direkten zugriff über score_element[]



while True:
    guess = int(input("Bitte Zahl (zwischen 1 und 30) raten: "))
    attempts += 1 # ident mit attempts = attempts + 1
    if guess == secret:
        #score_list.append(attempts) # append hängt das neue Element an die bestehende Liste dazu, sonst würde ich sie überschreiben
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
        with open("lesson5-game-score.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Gewonnen! Die Zahl ist " + str(secret))
        print("Versuche: " + str(attempts))
        break
    elif guess > secret:
        print("Falsch, die gesuchte Zahl ist kleiner.")
    elif guess < secret:
        print("Falsch, die gesuchte Zahl ist größer.")







