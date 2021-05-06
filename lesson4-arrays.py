#einfache datentypen int, string, float
example_int = 4

#arrays / Listen: erweiterte datentypen
example_list = [3, 44, 554, 2, 1]
#print(example_list) #ausgabe ganze liste
#print(example_list[3]) #ausgabe ein element aus der liste


string_list = ["golf", "tennis", "ski"]

mixed_list = [44, "lukas", False, 3.43]


example_list.sort() #--> mixed_list.sort() würde fehler bringen!
print(example_list) #ausgabe ganze liste

for item in mixed_list:
    print(item)

