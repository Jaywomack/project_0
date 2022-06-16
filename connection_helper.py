import pymysql.cursors
from dotenv import load_dotenv
import os
load_dotenv()

connection =  pymysql.connect(host = os.getenv("HOST"), user = os.getenv("USER"), password = os.getenv("PASSWORD"), database = os.getenv("DATABASE"), port = int(os.getenv("PORT")), charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


 



