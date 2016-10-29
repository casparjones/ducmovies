# simple gui
from tkinter import *
from lib.FilmAppMenu import FilmAppMenu

# create the window
root = Tk()

# modify root window
root.title("Simple GUI")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
m = FilmAppMenu(root)

#kick off the event loop
root.mainloop()

