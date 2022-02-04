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

#einzelne werte hinzufügen
example_list.append(23)
print(example_list)


#einer liste eine liste hinzufügen
example_list.append(mixed_list)
print(example_list)

#lieber die einzelnen werte

for item in mixed_list:
    example_list.append(item)
print(example_list)