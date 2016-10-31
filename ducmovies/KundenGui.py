from tkinter import *
from tkinter.ttk import *


class KundenGui:
    def __init__(self, dh, mainframe, headerfont, mainwindow):
        self.dh = dh
        self.mainframe = mainframe
        self.headerFont = headerfont
        self.mainwindow = mainwindow
        self.kunde = None

    def show_kunden(self):
        kunden = self.dh.get_kunden()
        self.mainwindow.frame_clean_up()

        columns = ["Vorname", "Name", "Telefon", "Löschen", "Editieren"]
        self.mainwindow.create_table_header(columns)
        columns = ["Vorname", "Name", "Telefon"]
        self.mainwindow.create_table_content(kunden, columns)

        row = 1
        for kunde in kunden:
            row += 1
            Button(self.mainframe, text="Löschen",
                   command=lambda inner_kunde=kunde: self.delete_kunde(inner_kunde)) \
                .grid(column=4, row=row, sticky=W)

            Button(self.mainframe, text="Editieren",
                   command=lambda inner_kunde=kunde: self.edit_create_kunde(inner_kunde)) \
                .grid(column=5, row=row, sticky=W)

        row += 2
        Button(self.mainframe, text="Neuer Kunde anlegen", command=self.edit_create_kunde) \
            .grid(column=1, row=row, columnspan=5, sticky=E)

    def delete_kunde(self, kunde):
        self.dh.delete_kunde(kunde)
        self.show_kunden()
        return

    def save_kunde(self, form, kunde):
        if kunde is None:
            new_kunde = True
            kunde = {}
        else:
            new_kunde = False

        kunde["Name"] = form["Name"].get('0.0', END).rstrip()
        kunde["Vorname"] = form["Vorname"].get('0.0', END).rstrip()
        kunde["Telefon"] = form["Telefon"].get('0.0', END).rstrip()

        kunde["Kundennummer"] = self.dh.save_kunde(kunde)

        self.show_kunden()

    def edit_create_kunde(self, kunde=None):
        self.mainwindow.frame_clean_up()

        if kunde is None:
            Label(self.mainframe, text="Kunde anlegen",
                  font=self.headerFont).grid(column=1, row=0, columnspan=2, sticky=W)
        else:
            Label(self.mainframe, text="Kunde editieren",
                  font=self.headerFont).grid(column=1, row=0, columnspan=2, sticky=W)

        form = {
            "Name": Text(self.mainframe, height=1, width=30),
            "Vorname": Text(self.mainframe, height=1, width=30),
            "Telefon": Text(self.mainframe, height=1, width=30),
        }

        self.mainwindow.add_form_textfield("Name", kunde, 2, form)
        self.mainwindow.add_form_textfield("Vorname", kunde, 3, form)
        self.mainwindow.add_form_textfield("Telefon", kunde, 4, form)

        Button(self.mainframe, text="save", command=lambda inner_form=form: self.save_kunde(inner_form, kunde)) \
            .grid(column=1, row=6, columnspan=2, sticky=E)
        return
