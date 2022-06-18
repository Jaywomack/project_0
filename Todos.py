from connection_helper import connection
import pymysql
import time
from tabulate import tabulate

class Todos():
        '''Todo Class'''

        # create a todo
        def create_todo(self, description):

                try:
                        with connection.cursor() as cursor:
                                sql = 'INSERT INTO Todos ( Description, created) VALUES (%s,%s)'
                                cursor.execute(sql, (description, time.strftime('%Y-%m-%d %H:%M:%S'))
                                )
                                connection.commit()
                                print(f"Todo:>> {description[:25]} created")

                except pymysql.Error  as e:
                        print(f"There was an error creating user: {e}")

        #  Get all todos, completed, in progress and todos
        def get_todos_all(self):
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Todos'
                                cursor.execute(sql)
                                print("Your List of Todos: ")
                                data = [[x['TodoID'], x['Description']] for x in cursor.fetchall()]
                                print(tabulate(data))
                except pymysql.Error as e:
                        print(f'There was an error retrieving your request. {e}')
                

        # Export todos to 
        def export_todos(self, name_file):
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Todos'
                                cursor.execute(sql)
                                f = open(f"{name_file}.txt","w")
                                [f.writelines(f"{x['Description']}\n") for x in cursor.fetchall()]
                                print(f"Todos written to file {name_file}")
                except pymysql.Error as e:
                        print(f'There was an error retrieving your request. {e}')


        def delete_todo(self, todo_id):
                try:
                        with connection.cursor() as cursor:
                                sql = 'DELETE FROM Todos WHERE TodoID = %s'
                                cursor.execute(sql, (todo_id))
                                connection.commit()
                                print(f"Todo {todo_id} has been deleted.")
                except pymysql.Error as e:
                        print(f"There was an error deleting the todo {e}")
