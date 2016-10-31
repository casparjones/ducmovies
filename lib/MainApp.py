from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font

from lib.DataHolder import DataHolder
from lib.FilmGui import FilmGui
from lib.MitarbeiterGui import MitarbeiterGui
from lib.KundenGui import KundenGui

import tkinter.messagebox
import tkinter
import datetime


class MainApp(object):
    def __init__(self, root):
        self.filiale = NONE
        self.film = NONE
        self.root = root
        self.form = {}
        self.dh = DataHolder()
        self.root.title("Duc Filmverleih")
        self.mainframe = Frame(self.root, padding="6 6 12 12")
        self.headerFont = Font(family="Helvetica", size=12)
        self.filmGui = FilmGui(self.dh, self.mainframe, self.headerFont, self)
        self.mitarbeiterGui = MitarbeiterGui(self.dh, self.mainframe, self.headerFont, self)
        self.kundenGui = KundenGui(self.dh, self.mainframe, self.headerFont, self)

        self.createmenu()

    def open_filiale(self, filiale):
        self.filiale = filiale
        self.show_movies()

    def close_app(self):
        self.dh.close_connection()
        self.root.destroy()

    @staticmethod
    def about():
        tkinter.messagebox.showinfo("About", "Filmverleih von Duc")

    def frame_clean_up(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()

        self.mainframe.grid_remove()
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack()

        self.mainframe.pack(side="bottom", fill=BOTH, expand=True)
        self.mainframe.grid()

    def add_form_textfield(self, label, data, row, form):
        Label(self.mainframe, text=label).grid(column=1, row=row, sticky=W)
        if data is not None and type(form[label]) is Text:
            form[label].insert(INSERT, self.get_content(data, label))
        form[label].grid(column=2, row=row)

    def create_table_header(self, headers):
        column = 0
        for header in headers:
            column += 1
            Label(self.mainframe, text=header, font=self.headerFont).grid(column=column, row=1, sticky=W)

    def create_table_content(self, content, columns):
        row = 1
        for rowValue in content:
            row += 1
            col = 0
            for colKey in columns:
                col += 1
                Label(self.mainframe, text=rowValue[colKey]).grid(column=col, row=row, sticky=W)

    def show_movies(self):
        if self.filiale is NONE:
            return

        filme = self.dh.get_filme(self.filiale)
        self.frame_clean_up()

        c = ["Titel", "Genre", "Erscheinungsjahr", "Verliehen"]
        self.create_table_header(c)
        c = ["Titel", "Genre", "Erscheinungsjahr"]
        self.create_table_content(filme, c)

        row = 1
        for film in filme:
            row += 1
            verliehen = self.dh.get_film_verliehen_in_filiale(film, self.filiale)
            if verliehen is None:
                Label(self.mainframe, text=" ./. ").grid(column=4, row=row, sticky=W)
                Button(self.mainframe, text="verleihen", command=lambda inner_film=film: self.add_ausleih(inner_film)) \
                    .grid(column=5, row=row)
            else:
                verliehen_an = verliehen["Datum"] + " an " + verliehen["k.Vorname"] + " " + verliehen["k.Name"]
                Label(self.mainframe, text=verliehen_an).grid(column=4, row=row, sticky=W)
                Button(self.mainframe, text="Zurück", command=lambda ausleih=verliehen: self.delete_ausleih(ausleih)) \
                    .grid(column=5, row=row)

    def add_ausleih(self, film):
        self.frame_clean_up()

        kunden = self.dh.get_kunden()
        kunden_options = {}
        for kunde in kunden:
            kunden_options[kunde["Vorname"] + " " + kunde["Name"]] = kunde["Kundennummer"]

        mitarbeiter = self.dh.get_mitarbeiter(self.filiale)
        mitarbeiter_options = {}
        for each_mitarbeiter in mitarbeiter:
            mitarbeiter_options[each_mitarbeiter["Vorname"] + " " + each_mitarbeiter["Name"]] = \
                each_mitarbeiter["Mitarbeiternummer"]

        kunden_id = StringVar()
        mitarbeiter_id = StringVar()
        form = {
            "Kunde": OptionMenu(self.mainframe, kunden_id, *kunden_options),
            "Mitarbeiter": OptionMenu(self.mainframe, mitarbeiter_id, *mitarbeiter_options),
        }

        self.add_form_textfield("Kunde", None, 2, form)
        self.add_form_textfield("Mitarbeiter", None, 3, form)

        Button(self.mainframe, text="save",
               command=lambda inner_form=form: self.save_ausleih(
                   kunden_id, mitarbeiter_id, film, kunden_options, mitarbeiter_options))\
            .grid(column=1, row=6, columnspan=2, sticky=E)
        return

    def save_ausleih(self, kunden_id, mitarbeiter_id, film, kunden_options, mitarbeiter_options):
        now = datetime.datetime.now()

        self.dh.save_ausleih(
            kunden_options[kunden_id.get()],
            mitarbeiter_options[mitarbeiter_id.get()],
            film, now.strftime("%d.%m.%Y"))
        self.show_movies()

    def delete_ausleih(self, ausleih):
        self.dh.delete_ausleih(ausleih)
        self.show_movies()
        return

    @staticmethod
    def filiale_name(filiale):
        return "Nummer " + str(filiale['Filialennummer']) + " " + filiale['Strasse']

    @staticmethod
    def get_content(data, key, default=""):
        if data is None:
            return default
        if data[key] is None:
            return default
        return data[key]

    def createmenu(self):
        filialen_data = self.dh.get_filialen()
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filialen = Menu(menu)
        menu.add_cascade(label="Filalen", menu=filialen)
        for filiale in filialen_data:
            filialen.add_command(label=self.filiale_name(filiale),
                                 command=lambda inner_filiale=filiale: self.open_filiale(inner_filiale))

        self.open_filiale(filialen_data.pop(0))

        help_menu = Menu(menu)
        menu.add_cascade(label="Grunddaten", menu=help_menu)
        help_menu.add_command(label="Kunden", command=self.kundenGui.show_kunden)
        help_menu.add_command(label="Mitarbeiter", command=self.mitarbeiterGui.show_mitarbeiter)
        help_menu.add_command(label="Filme", command=self.filmGui.show_filme)
        help_menu.add_command(label="About...", command=self.about)
