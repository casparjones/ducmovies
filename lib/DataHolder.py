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

    def getKunden(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `kunden`"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

    def getMitarbeiter(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `mitarbeiter`"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

    def getFilme(self, filiale):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `film_in_filiale` as fif join `filme` as f on fif.film_id = f.Filmnummer " + \
                  "WHERE fif.filiale_id = " + str(filiale["Filialennummer"])
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
