import tkinter
import random
from tkinter import messagebox

secret = random.randint(1,30)


#alles erstes das fesnter erstellen
window = tkinter.Tk()

#ein festner kann meherere elemente haben
hello_label = tkinter.Label(window, text="Hallo Welt!")
#vor es dargestellt wird, muss man es noch ins fenster "packen"
hello_label.pack()

guess = tkinter.Entry(window)
guess.pack()



def ButtonClick():
    if int(guess.get()) == secret:
        result_text = "You WIN"
    elif int(guess.get()) > secret:
        result_text = "WRONG: number is too high"
    else:
        result_text = "WRONG: number is too low"
    messagebox.showinfo(title="result", message = result_text)

submit_button = tkinter.Button(window, text = "Submit", command = ButtonClick) #command: funktion OHNE ()
submit_button.pack()


#damit das fesnter sich nicht gleich selbst beendet, muss es in der mainloop laufen
window.mainloop()



