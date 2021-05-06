a = 33
b = "hello"
c = [1, 2, 3]

print("einfache datentypen (int, float, bool, string, NAN) --> wird per VALUE übergeben")
#--> a ändert sich nicht, wenn ich b veränder


a = 0
b = a
b += 20
print(a)
#id() printed speicherplatz einervariable
print(id(a))
print(id(b))


print("komplexe datentypen (array, dict, objekt) werden per REFERENZ zum SPEICHERPLATZ übergeben (in C++: Pointer)")
print("--> a verändert sich, obowhl ich nur b verändert habe")
a = [1, 2, 3] #beim erstellen wird natürlich neuer speicherplatz gebraucht
b = a
b += [44]
print (a)

print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))

print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
print(id(b[3]))



a = [1, 2, 3]
b = a  #hier wird nur eine referenz übergeben
b = [1, 2, 3] #hier wird alles überschrieben, neuer speicherplatz vergeben
b[0]=42 #daher kann ich b jetzt auch unabhänigg von a verändern
print(a)
print(b)

#kopieren: das 0te element der übergebenen liste wird auf 42 gesetzt
def make_value_42(b):
    b[0] = 42

a = [1, 2, 3]
print(a)
make_value_42(a)
print(a)


print("ECHTES kopieren von listen mit list()")
a = [1, 2, 3]
b = list(a) #b = a würde nur referenz übergeben
b[0] = 42
print(a)
print(b)

print("ACHTUNG! beim echten kopieren von verschachtelten listen")
a = [1, 2, [3]]
print (a)
b = list(a)
b[2] += [42]
print(a) # die zuweisung von b hat auch a verändert!
print(b)

print("lösung: deepcopy")
from copy import deepcopy
a = [1, 2, [3]]
b = deepcopy(a)
b[2] += [42]
print (a) #a bleibt wie es war
print (b)

print("deepcopy kann auch leere listen kopieren")
a = []
print(a)
a.append(a)
print(a)
b = deepcopy(a)
a+=[2]
print(a)


print("problem existiert auch bei objekten")
class Thing(object):
    testproperty = [] #hier teilen sich alle objekte den selben speicherplatz

#ich hab zwei objekte erstellt
a = Thing()
b = Thing()

b.testproperty.append(42)

print(b.testproperty)
print(a.testproperty) #a hat auch 42, obwohl ich nur b verändern wollte!



print("richtige lösung für objekte:")
class Thing(object):
    def __init__(self): #durch diese zeile wird jedem neu erstellten objekt eigener speicherplatz zugeordnet
        self.testproperty = []

#ich hab zwei objekte erstellt
a = Thing()
b = Thing()

b.testproperty.append(42)

print(b.testproperty)
print(a.testproperty) #jetzt hab ich tatsächlich nur b verändert

print("deepcopy() funktioniert auch für objekte")
c = deepcopy(b)
print (c.testproperty)

