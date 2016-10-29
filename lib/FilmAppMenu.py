from tkinter import *
from lib.DataHolder import DataHolder
import tkinter.messagebox


class FilmAppMenu:
    def open_filiale(self, filiale):
        print(filiale)

    @staticmethod
    def about():
        tkinter.messagebox.showinfo("About", "Filmverleih von Duc")

    def createmenu(self, root):
        dh = DataHolder()
        filialenData = dh.getFilalen()
        menu = Menu(root)
        root.config(menu=menu)
        filialen = Menu(menu)
        menu.add_cascade(label="Filalen", menu=filialen)
        for filiale in filialenData:
            filialen.add_command(label="Nummer " + str(filiale['Filialennummer']) + " " + filiale['Strasse'],
                                 command=lambda filiale=filiale: self.open_filiale(filiale))

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.about)
