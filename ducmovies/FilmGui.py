from tkinter import *
from tkinter.ttk import *


class FilmGui(object):
    def __init__(self, dh, mainframe, headerfont, mainwindow):
        self.dh = dh
        self.mainframe = mainframe
        self.headerFont = headerfont
        self.mainwindow = mainwindow
        self.checkbox_values = {}
        self.film = None

    def show_filme(self):
        filme = self.dh.get_filme()

        self.mainwindow.frame_clean_up()

        c = ["Titel", "Genre", "Erscheinungsjahr", "Löschen", "Editieren"]
        self.mainwindow.create_table_header(c)
        c = ["Titel", "Genre", "Erscheinungsjahr"]
        self.mainwindow.create_table_content(filme, c)

        row = 1
        for film in filme:
            row += 1
            Button(self.mainframe, text="Löschen", command=lambda inner_film=film: self.delete_film(inner_film)) \
                .grid(column=4, row=row, sticky=W)

            Button(self.mainframe, text="Editieren", command=lambda inner_film=film: self.edit_create_film(inner_film)) \
                .grid(column=5, row=row, sticky=W)

        row += 2
        Button(self.mainframe, text="Neuer Film anlegen", command=self.edit_create_film) \
            .grid(column=1, row=row, columnspan=5, sticky=E)

    # FILM METHODS
    def delete_film(self, film):
        self.dh.delete_film(film)
        self.show_filme()

    def edit_create_film(self, film=None):
        self.film = film
        self.mainwindow.frame_clean_up()

        if self.film is NONE:
            Label(self.mainframe, text="Film anlegen", font=self.headerFont).grid(column=1, row=0, columnspan=2,
                                                                                  sticky=W)
        else:
            Label(self.mainframe, text="Film editieren", font=self.headerFont).grid(column=1, row=0, columnspan=2,
                                                                                    sticky=W)

        form = {
            "Titel": Text(self.mainframe, height=1, width=30),
            "Genre": Text(self.mainframe, height=1, width=30),
            "Erscheinungsjahr": Text(self.mainframe, height=1, width=30)
        }

        Label(self.mainframe, text="Titel").grid(column=1, row=1, sticky=W)
        if film is not NONE:
            form["Titel"].insert(INSERT, self.mainwindow.get_content(film, "Titel"))
        form["Titel"].grid(column=2, row=1)

        Label(self.mainframe, text="Genre").grid(column=1, row=2, sticky=W)
        if film is not NONE:
            form["Genre"].insert(INSERT, self.mainwindow.get_content(film, "Genre"))
        form["Genre"].grid(column=2, row=2)

        Label(self.mainframe, text="Erscheinungsjahr").grid(column=1, row=3, sticky=W)
        if film is not NONE:
            form["Erscheinungsjahr"].insert(INSERT, self.mainwindow.get_content(film, "Erscheinungsjahr"))
        form["Erscheinungsjahr"].grid(column=2, row=3)

        row = 4
        if self.film is not NONE:
            Label(self.mainframe, text="Film in Filialen editieren:", font=self.headerFont) \
                .grid(column=1, row=4, columnspan=2, sticky=W)
            filialen = self.dh.get_filialen()
            self.checkbox_values = {}
            for filiale in filialen:
                row += 1
                self.checkbox_values[filiale["Filialennummer"]] = IntVar()
                Checkbutton(self.mainframe, text=self.mainwindow.filiale_name(filiale), variable=self.checkbox_values[filiale["Filialennummer"]],
                            command=lambda each_filiale=filiale: self.save_film_in_filiale(film, each_filiale)) \
                    .grid(column=1, row=row, columnspan=2, sticky=E)

                film_in_filiale = self.dh.get_film_in_filale(film, filiale)
                if film_in_filiale is not None:
                    self.checkbox_values[filiale["Filialennummer"]].set(1)

            row += 1

        Button(self.mainframe, text="save", command=lambda inner_form=form: self.save_film(inner_form, film)) \
            .grid(column=1, row=row, columnspan=2, sticky=E)

    def save_film_in_filiale(self, film, filiale):
        if self.checkbox_values[filiale['Filialennummer']].get() == 0:
            self.dh.remove_film_in_filiale(film, filiale)
        else:
            self.dh.add_film_in_filiale(film, filiale)

    def save_film(self, form, film):
        if film is None:
            new_film = True
            film = {}
        else:
            new_film = False

        film["Titel"] = form["Titel"].get('0.0', END).rstrip()
        film["Genre"] = form["Genre"].get('0.0', END).rstrip()
        film["Erscheinungsjahr"] = form["Erscheinungsjahr"].get('0.0', END).rstrip()
        film["Filmnummer"] = self.dh.save_film(film)

        if not new_film:
            self.show_filme()
        else:
            self.edit_create_film(film)
