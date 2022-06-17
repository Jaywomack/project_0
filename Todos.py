from connection_helper import connection
import pymysql
from pymysql import Error


class Todos():
        '''Todo Class'''

        def __init__(self):
                self.TodoID = None

        # create a todo
        def create_todo(self, UserId, username, description):

                try:
                        with connection.cursor() as cursor:
                                sql = 'INSERT INTO Todos (UserId, username, description) VALUES (%s,%s,%s)'
                                cursor.execute(sql,( UserId, username, description))
                                connection.commit()
                                print(f"{self.username} your todo has been added")

                except pymysql.Error  as e:
                        print(f"There was an error creating user: {e}")

        #  Get all todos, completed, in progress and todos
        def get_todos_all(self, UserId):
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Todos WHERE UserId = %s'
                                cursor.execute(sql,(UserId))
                                print("Your List of Todos: ")
                                [print(x['description']) for x in cursor.fetchall()]
                except pymysql.ERROR as e:
                        print(f'There was an error retrieving your request. {e}')
                

        # Export todos to 
        def export_todos(self, UserId, name_file):
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Todos WHERE UserId = %s'
                                cursor.execute(sql,(UserId))
                                f = open(f"{name_file}.txt","w")
                                [f.writelines(f"{x['description']}\n") for x in cursor.fetchall()]
                                print(f"Todos written to file {name_file}")
                except pymysql.ERROR as e:
                        print(f'There was an error retrieving your request. {e}')


