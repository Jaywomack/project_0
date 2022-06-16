from connection_helper import connection
import pymysql


class Todos():
        '''Todo Class - inherits from Connection => User => Todo'''

        def __init__(self):
                self.TodoID = None

        # create a todo
        def create_todo(self, description):

                try:
                        with connection.cursor() as cursor:
                                sql = 'INSERT INTO Todos (UserId, username, description) VALUES (%s,%s,%s)'
                                cursor.execute(sql,( self.UserId, self.username, description))
                                connection.commit()
                                print(f"{self.username} your todo has been added")

                except pymysql.Error  as e:
                        print(f"There was an error creating user: {e}")

        #  Get all todos, completed, in progress and todos
        def get_todos_all(self):
                print("Get all todos, completed, in progress and todos")
                

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


        # Admin only methods
        # todos completed in a time range
        def get_todo_metrics_completed(self, timerange):
                print(f"You want todos from what {timerange}?")


        # todo average time to completion 
        def get_todo_metrics_time_average(self, timerange):
                print(f"You want todos from what {timerange}?")


        # todo total completed
        def get_todo_metrics_total_completed(self, timerange):
                print(f"You want todos from what {timerange}?")

                
        # todo performance
        def get_todo_metrics_completed(self, timerange):
                print(f"You want todos from what {timerange}?")

 