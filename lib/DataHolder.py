import pymysql.cursors


class DataHolder:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='duc',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    def close_connection(self):
        if self.connection.open:
            self.connection.close()

    def save_film(self, film):
        if "Filmnummer" in film and film["Filmnummer"] > 0:
            insert = False
            sql = "UPDATE `filme` SET " + \
                  "`Titel` = '" + film["Titel"] + "', " + \
                  "`Genre` = '" + film["Genre"] + "', " + \
                  "`Erscheinungsjahr` = '" + film["Erscheinungsjahr"] + "'" + \
                  " WHERE `Filmnummer` = '" + str(film["Filmnummer"]) + "';"
        else:
            insert = True
            sql = "INSERT INTO `filme` (`Titel`, `Genre`, `Erscheinungsjahr`) " + \
                  "VALUES ('" + film["Titel"] + "', '" + film["Genre"] + "', '" + film["Erscheinungsjahr"] + "');"

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            cursor.close()

        self.connection.commit()

        if insert:
            return self.connection.insert_id()
        else:
            return film["Filmnummer"]

    def save_kunde(self, kunde):
        if "Kundennummer" in kunde and kunde["Kundennummer"] > 0:
            insert = False
            sql = "UPDATE `kunden` SET " + \
                "`Name` = '" + kunde["Name"] + "', " \
                "`Vorname` = '" + kunde["Vorname"] + "', " \
                "`Telefon` = '" + kunde["Telefon"] + "' " \
                " WHERE `Kundennummer` = '" + str(kunde["Kundennummer"]) + "';"
        else:
            insert = True
            sql = "INSERT INTO `kunden` (`Name`, `Vorname`, `Telefon`) " + \
                  "VALUES (" \
                  "'" + kunde["Name"] + "', " \
                  "'" + kunde["Vorname"] + "', " \
                  "'" + kunde["Telefon"] + "');"

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            cursor.close()

        self.connection.commit()

        if insert:
            return self.connection.insert_id()
        else:
            return kunde["Kundennummer"]

    def save_ausleih(self, kunde, mitarbeiter, film, date):
        sql = "INSERT INTO `ausleih` (`Kunde`, `Mitarbeiter`, `Datum`, `Film`) " + \
              "VALUES (" \
              "'" + kunde + "', " \
              "'" + mitarbeiter + "', " \
              "'" + date + "', " \
              "'" + str(film["Filmnummer"]) + "');"

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            cursor.close()

        self.connection.commit()

    def save_mitarbeiter(self, mitarbeiter):
        if "Mitarbeiternummer" in mitarbeiter and mitarbeiter["Mitarbeiternummer"] > 0:
            insert = False
            sql = "UPDATE `mitarbeiter` SET " + \
                "`Name` = '" + mitarbeiter["Name"] + "', " \
                "`Vorname` = '" + mitarbeiter["Vorname"] + "', " \
                "`Filiale` = '" + mitarbeiter["Filiale"] + "', " \
                "`Gehalt` = '" + mitarbeiter["Gehalt"] + "'" + \
                " WHERE `Mitarbeiternummer` = '" + str(mitarbeiter["Mitarbeiternummer"]) + "';"
        else:
            insert = True
            sql = "INSERT INTO `mitarbeiter` (`Name`, `Vorname`, `Filiale`, `Gehalt`) " + \
                  "VALUES (" \
                  "'" + mitarbeiter["Name"] + "', " \
                  "'" + mitarbeiter["Vorname"] + "', " \
                  "'" + mitarbeiter["Filiale"] + "', " \
                  "'" + mitarbeiter["Gehalt"] + "');"

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            cursor.close()

        self.connection.commit()

        if insert:
            return self.connection.insert_id()
        else:
            return mitarbeiter["Mitarbeiternummer"]

    def remove_film_in_filiale(self, film, filiale):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `film_in_filiale` WHERE film_id = " + str(film["Filmnummer"]) + \
                  " AND filiale_id = " + str(filiale["Filialennummer"])
            cursor.execute(sql)
        self.connection.commit()

    def add_film_in_filiale(self, film, filiale):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `film_in_filiale` (`film_id`, `filiale_id`) " + \
              "VALUES ('" + str(film["Filmnummer"]) + "', '" + str(filiale["Filialennummer"]) + "');"
            cursor.execute(sql)

        self.connection.commit()

    def get_film_in_filale(self, film, filiale):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `film_in_filiale` as fif join `filme` as f on fif.film_id = f.Filmnummer " + \
                  "WHERE fif.filiale_id = " + str(filiale["Filialennummer"]) + \
                  " AND fif.film_id = " + str(film["Filmnummer"])
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            return result

    def get_filalen(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `filiale`"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result

    def get_film_verliehen_in_filiale(self, film, filiale):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `ausleih` AS a JOIN `mitarbeiter` AS m ON a.Mitarbeiter = m.Mitarbeiternummer " + \
                  " JOIN kunden AS k ON a.Kunde = k.Kundennummer" + \
                  " WHERE m.Filiale = " + str(filiale["Filialennummer"]) + " AND a.Film = " + str(film["Filmnummer"]) +\
                  " ORDER BY Datum DESC"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            return result

    def get_kunden(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `kunden`"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result

    def delete_ausleih(self, ausleih):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `ausleih` WHERE Ausleihnummer = " + str(ausleih["Ausleihnummer"])
            cursor.execute(sql)
        self.connection.commit()

    def delete_kunde(self, kunde):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `kunden` WHERE Kundennummer = " + str(kunde["Kundennummer"])
            cursor.execute(sql)
        self.connection.commit()

    def delete_film(self, film):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `filme` WHERE Filmnummer = " + str(film["Filmnummer"])
            cursor.execute(sql)
        self.connection.commit()

    def delete_mitarbeiter(self, mitarbeiter):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `mitarbeiter` WHERE Mitarbeiternummer = " + str(mitarbeiter["Mitarbeiternummer"])
            cursor.execute(sql)
        self.connection.commit()

    def get_mitarbeiter(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `mitarbeiter`"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result

    def get_filme(self, filiale=None):
        with self.connection.cursor() as cursor:
            # Read a single record
            if filiale is None:
                sql = "SELECT * FROM `filme`"
            else:
                sql = "SELECT * FROM `film_in_filiale` as fif join `filme` as f on fif.film_id = f.Filmnummer " + \
                      "WHERE fif.filiale_id = " + str(filiale["Filialennummer"])
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
