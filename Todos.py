from connection_helper import connection
import pymysql
from pymysql import Error


class Todos():
        '''Todo Class'''

        def __init__(self):
                self.TodoID = None
 



        # create a todo
        def create_todo(self, description):

                try:
                        with connection.cursor() as cursor:
                                sql = 'INSERT INTO Todos ( description) VALUES (%s)'
                                cursor.execute(sql, (description)
                                )
                                connection.commit()
                                print(f"Todo {description}[:12] created")

                except pymysql.Error  as e:
                        print(f"There was an error creating user: {e}")

        #  Get all todos, completed, in progress and todos
        def get_todos_all(self,):
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Todos'
                                cursor.execute(sql)
                                print("Your List of Todos: ")
                                [print(x['description']) for x in cursor.fetchall()]
                except pymysql.ERROR as e:
                        print(f'There was an error retrieving your request. {e}')
                

        # Export todos to 
        def export_todos(self, name_file):
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Todos'
                                cursor.execute(sql)
                                f = open(f"{name_file}.txt","w")
                                [f.writelines(f"{x['description']}\n") for x in cursor.fetchall()]
                                print(f"Todos written to file {name_file}")
                except pymysql.ERROR as e:
                        print(f'There was an error retrieving your request. {e}')


todo_1 = Todos()
todo_1.create_todo("This is the first todo in the database")
