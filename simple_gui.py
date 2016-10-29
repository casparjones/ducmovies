# simple gui
from tkinter import *
from lib.FilmAppMenu import FilmAppMenu

# create the window
root = Tk()

# modify root window
root.title("Simple GUI")
# root.geometry("800x600")

m = FilmAppMenu()
m.createmenu(root)

result = "Hallo Welt"

logo = PhotoImage(file="./images/opengraph-icon-200x200.png")
# w1 = Label(root, image=logo).pack(side="left")
explanation = result
w2 = Label(root,
           compound = CENTER,
           padx = 5,
           text=explanation).pack(side="left")

#kick off the event loop
root.mainloop()

