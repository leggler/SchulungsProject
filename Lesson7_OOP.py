class Player():
    def __init__(self, first_name, last_name, height_cm, weight):
        self.first_name = first_name
        #.first_name ist eine variable, die sinnvollerweise gleich heißt wie oben in der eingabe - könnte auch anders heißen
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight = weight

# selbst geschriebene methode:  wenn auf dieser ebene eine funtkion erstellt wird, kiommt diese zu allen objekten automatisch hinzu gleicher init wie oben
    def weight_to_lbs(self):
        pounds = self.weight * 2.234
        return pounds



# in klammer steht player --> golfplayer ist child von player
class GolfPlayer(Player):
#initialisierungsmethode
    def __init__(self, first_name, last_name, height_cm, weight, points, handicap, tournaments): #self ist das neue objekt, dass auf basis dieses models/diser sturktur erstellt wird (zb lukas_golfobj)
        # Vererbung: super() greift auf die elternklasse zurück (-->"Player")
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight=weight)
        self.points = points
        self.handicap = handicap
        self.tournaments = tournaments
        #methoden können sogar schon im init angewendet werden (wenn weight schon darüber definiert wurde)
        self.weight_in_pounds = self.weight_to_lbs()



class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight, goals, red_cards, yellow_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight=weight)
        self.goals = goals
        self.red_cards = red_cards
        self.yellow_cards = yellow_cards





############ Was kann ich jetzt mit diesen Objekten machen??
#objekte definieren
lukas_golfobj = GolfPlayer(first_name="lukas", last_name="eggler", height_cm=190, weight=90, points=123, handicap=5, tournaments=20)
petra_golfobj = GolfPlayer("petra", "maier", 170, 65, 133, 2, 33)

#eigenschaften von objekten ausprinten
print(lukas_golfobj.handicap)

#LISTE VON OBJEKTEN ERSTELLEN (=90% der use cases)
golf_players = [lukas_golfobj, petra_golfobj]

#... und die elemente in der liste durchgegen.
for player in golf_players:
    print (f"Name: {player.first_name}, Handicap: {str(player.handicap)}")

#methode aus der klasse anwenden
print(petra_golfobj.weight_to_lbs())
print (petra_golfobj.weight_in_pounds)

ronaldo = FootballPlayer("christiano", "ronaldo", 190, 80, 44, 2, 3)
print(ronaldo.red_cards)

#.sort kann man auf arrays anwenden

golf_players.sort(key=lambda x: x.height_cm, reverse=False)
#bei array aus objekten kann die sort-funktion nicht direkt auf eigenschaften zugreifen (das kann sie nur bei arrays)
# x repräsenteirt den kompletten datensatz
#gilt auch für ein Array in dem Dictionarys drin sind

for player in golf_players:
    print ("sortiert: "+ player.first_name + player.last_name)
