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
                        print('There was an error retrieving your request. {e}')
                

        # view all the uncompleted todos
        def get_todos_uncompleted(self):
                print("view all the uncompleted todos")


        # view all the completed todos
        def get_todos_completed(self):
                print("view all the completed todos")


        # view all the uncompleted todos to a certain date
        def get_todos_by_range(self):
                print("view all the uncompleted todos to a certain date")        


        # mark a todo as complete
        def set_todo_completed(self):
                print("Mark a todo as complete")


        # Lookup todo by name and edit/delete a todo
        def get_todo(self):
                print("Lookup todo by name and edit/delete a todo")


        # Export todos to 
        def export_todos(self):
                print("Export todos to a file")

