#strings zusammen setzten mit .format

string_one = "Hallo"
string_two = "Flockdown"


print("erste variante: " + string_one + " " + string_two)
print("zweite Variante: {0} {1}".format(string_one, string_two)) #"new style" format. {0} = das nullte element in der übergebenen liste, {1} das erste element etc.
print("dritte variante: %s %s" %(string_one, string_two))  #"old style" format. %s repräsentiert einen string (%d würde eine decimalzahl repräsentieren)
print(f"vierte variante: {string_one} {string_two}") #"string interpolation" mit f-strings


