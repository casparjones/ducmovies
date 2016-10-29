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