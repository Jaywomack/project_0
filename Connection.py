from ssl import CertificateError
import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv()

# connecto to the database
class Connection:
        '''Creates database connection. Use self.connection or self.connection.cursor'''

        # initialize the database
        def __init__(self):

                self.connection = pymysql.connect(
                        host = os.getenv("HOST"),
                        user = os.getenv("USER"),
                        password = os.getenv("PASSWORD"),
                        database = os.getenv("DATABASE"),
                        port = int(os.getenv("PORT")),
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

        def show_db(self):
                with self.connection.cursor() as cursor:
                        cursor.execute("SHOW DATABASES")
                        print(cursor.fetchall())
                        return cursor.fetchall()

        def show_tables(self):
                with self.connection.cursor() as cursor:
                        cursor.execute("SHOW TABLES")
                        print(cursor.fetchall())
                        return cursor.fetchall()

        def show_db_users(self):
                with self.connection.cursor() as cursor:
                        cursor.execute("SELECT user()")
                        print(cursor.fetchall())
                        return cursor.fetchall()
                

        def show_table_fields(self, table):
                '''Pass a table to the function to query its fields'''
                with self.connection.cursor() as cursor:
                        cursor.execute(f"SHOW COLUMNS from {table}")
                        print(cursor.fetchall())
                       
cnx = Connection()

cnx.show_table_fields("Users")

