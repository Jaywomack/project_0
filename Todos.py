from connection_helper import connection
import pymysql
import time
from tabulate import tabulate

class Todos():
        '''Todo Class'''

        # create a todo
        def create_todo(self, description):
                '''Function that creates a new todo from user input and persists it to the database'''
                try:
                        with connection.cursor() as cursor:
                                sql = 'INSERT INTO Todos ( Description, created) VALUES (%s,%s)'
                                cursor.execute(sql, (description, time.strftime('%Y-%m-%d %H:%M:%S'))
                                )
                                connection.commit()
                                print(f"Todo:>> {description[:25]} created")

                except pymysql.Error  as e:
                        print(f"There was an error creating user: {e}")


        def get_todos_all(self):
                '''Function that returns all todos in the database'''
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Todos'
                                cursor.execute(sql)
                                print("Your List of Todos: ")
                                data = [[x['TodoID'], x['Description']] for x in cursor.fetchall()]
                                print(tabulate(data))
                except pymysql.Error as e:
                        print(f'There was an error retrieving your request. {e}')
                


        def export_todos(self, name_file):
                '''Function that exports all todos to a csv file'''
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
                '''Function that deletes a todo from the database based on the todo ID input by the user'''
                try:
                        with connection.cursor() as cursor:
                                sql = 'DELETE FROM Todos WHERE TodoID = %s'
                                cursor.execute(sql, (todo_id))
                                connection.commit()
                                print(f"Todo {todo_id} has been deleted.")
                except pymysql.Error as e:
                        print(f"There was an error deleting the todo {e}")
