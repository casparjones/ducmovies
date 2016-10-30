import pymysql.cursors

class DataHolder:

    connection =  pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='duc',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    def getFilalen(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `filiale`"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

    def getFilmVerliehenInFiliale(self, film, filiale):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `ausleih` AS a JOIN `mitarbeiter` AS m ON a.Mitarbeiter = m.Mitarbeiternummer " + \
                " JOIN kunden AS k ON a.Kunde = k.Kundennummer" + \
                " WHERE m.Filiale = " + str(filiale["Filialennummer"]) + " AND a.Film = " + str(film["Filmnummer"]) + \
                " ORDER BY Datum DESC"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchone()

            return result

    def getKunden(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `kunden`"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

    def delete_film(self, film):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `filme` WHERE Filmnummer = " + str(film["Filmnummer"])
            cursor.execute(sql)

    def getMitarbeiter(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `mitarbeiter`"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

    def getFilme(self, filiale=None):
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

            return result
