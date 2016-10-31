from tkinter import *
from tkinter.ttk import *


class MitarbeiterGui(object):
    def __init__(self, dh, mainframe, headerfont, mainwindow):
        self.dh = dh
        self.mainframe = mainframe
        self.headerFont = headerfont
        self.mainwindow = mainwindow
        self.mitarbeiter = None

    def show_mitarbeiter(self):
        mitarbeiter = self.dh.get_mitarbeiter()

        self.mainwindow.frame_clean_up()

        columns = ["Vorname", "Name", "Gehalt", "Filiale", "Löschen", "Editieren"]
        self.mainwindow.create_table_header(columns)
        columns = ["Vorname", "Name", "Gehalt", "Filiale"]
        self.mainwindow.create_table_content(mitarbeiter, columns)

        row = 1
        for mitarbeiter in mitarbeiter:
            row += 1
            Button(self.mainframe, text="Löschen",
                   command=lambda inner_mitarbeiter=mitarbeiter: self.delete_mitarbeiter(inner_mitarbeiter)) \
                .grid(column=5, row=row, sticky=W)

            Button(self.mainframe, text="Editieren",
                   command=lambda inner_mitarbeiter=mitarbeiter: self.edit_create_mitarbeiter(inner_mitarbeiter)) \
                .grid(column=6, row=row, sticky=W)

        row += 2
        Button(self.mainframe, text="Neuer Mitarbeiter anlegen", command=self.edit_create_mitarbeiter) \
            .grid(column=1, row=row, columnspan=6, sticky=E)

    def delete_mitarbeiter(self, mitarbeiter):
        self.dh.delete_mitarbeiter(mitarbeiter)
        self.show_mitarbeiter()
        return

    def save_mitarbeiter(self, form, mitarbeiter, filiale, filialen_options):
        if mitarbeiter is None:
            mitarbeiter = {}

        mitarbeiter["Name"] = form["Name"].get('0.0', END).rstrip()
        mitarbeiter["Vorname"] = form["Vorname"].get('0.0', END).rstrip()
        mitarbeiter["Gehalt"] = form["Gehalt"].get('0.0', END).rstrip()
        mitarbeiter["Filiale"] = filialen_options[filiale.get()]

        mitarbeiter["Mitarbeiternummer"] = self.dh.save_mitarbeiter(mitarbeiter)

        self.show_mitarbeiter()

    def edit_create_mitarbeiter(self, mitarbeiter=None):
        self.mainwindow.frame_clean_up()

        if mitarbeiter is None:
            Label(self.mainframe, text="Mitarbeiter anlegen",
                  font=self.headerFont).grid(column=1, row=0, columnspan=2, sticky=W)
        else:
            Label(self.mainframe, text="Mitarbeiter editieren",
                  font=self.headerFont).grid(column=1, row=0, columnspan=2, sticky=W)

        filialen = self.dh.get_filialen()
        filiale_var = StringVar()
        filialen_options = {}
        first_value = None
        for filiale in filialen:
            if first_value is None:
                first_value = self.mainwindow.filiale_name(filiale)
            filialen_options[self.mainwindow.filiale_name(filiale)] = \
                filiale["Filialennummer"]
            if mitarbeiter is not None and mitarbeiter["Filiale"] == filiale["Filialennummer"]:
                first_value = self.mainwindow.filiale_name(filiale)

        form = {
            "Name": Text(self.mainframe, height=1, width=30),
            "Vorname": Text(self.mainframe, height=1, width=30),
            "Gehalt": Text(self.mainframe, height=1, width=30),
            "Filiale": OptionMenu(self.mainframe, filiale_var, first_value, *filialen_options)
        }

        filiale_var.set(first_value)
        self.mainwindow.add_form_textfield("Name", mitarbeiter, 2, form)
        self.mainwindow.add_form_textfield("Vorname", mitarbeiter, 3, form)
        self.mainwindow.add_form_textfield("Gehalt", mitarbeiter, 4, form)
        self.mainwindow.add_form_textfield("Filiale", mitarbeiter, 5, form)

        Button(self.mainframe, text="save",
               command=lambda inner_form=form: self.save_mitarbeiter(
                   inner_form, mitarbeiter, filiale_var, filialen_options)
               ) \
            .grid(column=1, row=6, columnspan=2, sticky=E)
        return
