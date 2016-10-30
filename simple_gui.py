# simple gui
from tkinter import *
from lib.MainApp import MainApp

# create the window
root = Tk()

# modify root window
root.title("Simple GUI")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
m = MainApp(root)

root.protocol("WM_DELETE_WINDOW", m.close_app)
#kick off the event loop
root.mainloop()

