import mysql.connector
from dotenv import load_dotenv
from mysql.connector import errorcode
import os
load_dotenv()

class Database:
        # Initialize the database
        def __init__(self):
                self.cnx = mysql.connector.connect(user=os.getenv("USER"), password=os.getenv("PASSWORD"), host=os.getenv("HOST"), database=os.getenv("DATABASE"), port=os.getenv("PORT"))
                self.cursor = self.cnx.cursor()

        # show tables 
        def show_tables(self):
                self.cursor.execute("SHOW TABLES")
                for (tables) in self.cursor:
                        print(tables)

project_db = Database()
project_db.show_tables()
