
#Minimum Example:
def say_hello(name):
    #print(f"hello {name}")
    return f"hello {name}"


def say_goodby():
    print("Goodby")


#kurzschreibweise um mehrere werte aus funktion zurück zu bekommen
def get_square_cube(number):
    square = number * number
    cube = number ** 3
    return square, cube


#werte als array zurückgeben
def get_square_cube_array(number):
    square = number * number
    cube = number * number * number
    return [square, cube]


#werte als dict zurückgeben
def get_square_cube_dict(number):
    square = number * number
    cube = number * number * number
    return {"square": square, "cube": cube}

def main():
    #test code
    dict = get_square_cube_dict(3)
    print(dict)


    str=say_hello("markus")
    print(str)

    print (say_hello(name="lukas"))


    square, cube = get_square_cube(number=3)

    print(square)
    print(cube)


    Array = get_square_cube_array(3)
    print(Array)


#diese zwei zeilen sind spezieller code, wenn die functions-datei auch selbst startbar sein soll
#der code in der datai selbst muss immer in der function "main()" stehen
#der entsprechende code wird dann NICHT ausgeführt, wenn functionen aus dem file in anderen files importiert werden
if __name__=="__main__":
    main()