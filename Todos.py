from User import User

class Todos(User):
        '''Todo Class - inherits from Connection => User => Todo'''
        

        #  Get all todos, completed, in progress and todos
        def get_todos_all(self):
                pass
                
        # view all the uncompleted todos
        def get_todos_uncompleted(self):
                pass

        # view all the completed todos
        def get_todos_completed(self):
                pass
        # view all the uncompleted todos to a certain date
        def get_todos_by_range(self):
                pass        
        # mark a todo as complete
        def mark_todo(self):
                pass
        # Lookup todo by name and edit/delete a todo
        def get_todo(self):
                pass        
        # Export todos to 
        def export_todos(self):
                pass

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

