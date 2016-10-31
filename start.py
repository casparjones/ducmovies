# simple gui
from tkinter import *
from ducmovies.MainApp import MainApp

# create the window
root = Tk()

# modify root window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
m = MainApp(root)

# kick off the event loop
root.mainloop()

