from tkinter import *
from tkinter.ttk import *
from lib.DataHolder import DataHolder

import tkinter.messagebox
import tkinter


class FilmAppMenu(object):
    def __init__(self, root):
        self.filale = 0
        self.dh = DataHolder()
        self.root = root

        self.root.title("Text Comparitor")
        self.createmenu()

        self.mainframe = Frame(self.root, padding="6 6 12 12")

        ## buttons
        ## self.close = Button(self.mainframe, text="Close",command=self.closeFrame).grid(column=1, row=9, sticky=SE)
        ## self.next = Button(self.mainframe, text="Next",command=self.nextPara).grid(column=1, row=9, sticky=S)
        ## self.next = Button(self.mainframe, text="Prev",command=self.prevPara).grid(column=1, row=9, sticky=SW)

    def closeFrame(self):
        return

    def nextPara(self):
        return

    def prevPara(self):
        return

    def open_filiale(self, filiale):
        self.filale = filiale
        self.show_movies()

    @staticmethod
    def about():
        tkinter.messagebox.showinfo("About", "Filmverleih von Duc")

    def show_kunden(self):
        kunden = self.dh.getKunden()

        ## build frame
        for widget in self.mainframe.winfo_children():
            widget.destroy()

        self.mainframe.grid_remove()
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack()
        ## text labels
        # Label(self.mainframe, text=self.filiale_name(self.filiale), font=("Helvetica", 32)).grid(column=1, row=1, sticky=E)
        self.mainframe.pack(side="bottom", fill=BOTH, expand=True)
        self.mainframe.grid()

        row = 0
        for kunde in kunden:
            row += 1
            Label(self.mainframe, text=kunde["Vorname"]).grid(column=1, row=row, sticky=W)
            Label(self.mainframe, text=kunde["Name"]).grid(column=2, row=row, sticky=W)
            Label(self.mainframe, text=kunde["Telefon"]).grid(column=3, row=row, sticky=W)

    def show_mitarbeiter(self):
        mitarbeiter = self.dh.getMitarbeiter()

        ## build frame
        for widget in self.mainframe.winfo_children():
            widget.destroy()

        self.mainframe.grid_remove()
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack()
        ## text labels
        # Label(self.mainframe, text=self.filiale_name(self.filiale), font=("Helvetica", 32)).grid(column=1, row=1, sticky=E)
        self.mainframe.pack(side="bottom", fill=BOTH, expand=True)
        self.mainframe.grid()

        row = 0
        for eachMitarbeiter in mitarbeiter:
            row += 1
            Label(self.mainframe, text=eachMitarbeiter["Vorname"]).grid(column=1, row=row, sticky=W)
            Label(self.mainframe, text=eachMitarbeiter["Name"]).grid(column=2, row=row, sticky=W)
            Label(self.mainframe, text=eachMitarbeiter["Gehalt"]).grid(column=3, row=row, sticky=W)
            Label(self.mainframe, text=eachMitarbeiter["Filiale"]).grid(column=4, row=row, sticky=W)

    def show_movies(self):
        print(self.filale)
        if self.filale == 0:
            return

        filme = self.dh.getFilme(self.filale)

        ## build frame
        for widget in self.mainframe.winfo_children():
            widget.destroy()

        self.mainframe.grid_remove()
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack()
        ## text labels
        # Label(self.mainframe, text=self.filiale_name(self.filiale), font=("Helvetica", 32)).grid(column=1, row=1, sticky=E)
        self.mainframe.pack(side="bottom", fill=BOTH, expand=True)
        self.mainframe.grid()

        row = 0

        for film in filme:
            row += 1
            Label(self.mainframe, text=film["Titel"]).grid(column=1, row=row, sticky=W)
            Label(self.mainframe, text=film["Genre"]).grid(column=2, row=row, sticky=W)
            Label(self.mainframe, text=film["Erscheinungsjahr"]).grid(column=3, row=row, sticky=W)

    def filiale_name(self, filiale):
        return "Nummer " + str(filiale['Filialennummer']) + " " + filiale['Strasse']

    def createmenu(self):
        filialenData = self.dh.getFilalen()
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filialen = Menu(menu)
        menu.add_cascade(label="Filalen", menu=filialen)
        for filiale in filialenData:
            filialen.add_command(label=self.filiale_name(filiale),
                                 command=lambda filiale=filiale: self.open_filiale(filiale))

        helpmenu = Menu(menu)
        menu.add_cascade(label="Weiter", menu=helpmenu)
        helpmenu.add_command(label="Kunden", command=self.show_kunden)
        helpmenu.add_command(label="Mitarbeiter", command=self.show_mitarbeiter)
        helpmenu.add_command(label="About...", command=self.about)
