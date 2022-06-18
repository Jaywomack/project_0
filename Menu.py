from Todos import Todos 
from Journals import Journals 
from Tasks import Tasks
import os
import signal


class Menu(Todos):
        '''Menu Class'''


        def main_menu(self):
#         ## What would you like to do?
                
                print("Loading Productivity App")

                print('Welcome to Your Productivity App\n')
                print("""
                1.) Todos
                2.) Tasks
                3.) Journal
                4.) Metrics
                5.) Quit
                """)

                main_menu_choice = int(input("What would you like to do today?  >> "))
                if main_menu_choice == 1:
                        print('Retrieving Todos Menu')
                        self.show_todos_menu()
                elif main_menu_choice == 2:
                        self.show_log_tasks_menu()
                elif main_menu_choice == 3:
                        self.show_journals_menu()
                elif main_menu_choice == 4:
                        self.generate_reports_menu()
                elif main_menu_choice == 5:
                        self.quit_menu()
                

        def show_todos_menu(self):      
                todo = Todos()
                usr = int(input('''Hello, what can I help you with?
        1.) See all todos
        2.) Write todos to a text file
        3.) Create todo
        4.) Delete todo
        \t\n >>'''))
                
                if usr == 1:
                        todo.get_todos_all()
                elif usr == 2:
                        file_name = input("Please enter a filename >>")
                        todo.export_todos(file_name)
                elif usr == 3:
                        description  = input("Please enter a description >>")
                        todo.create_todo(description)
                elif usr == 4:
                        todo.get_todos_all()
                        todo_id = input("Please enter the todo id you wish to delete >> ")
                        todo.delete_todo(todo_id)


        def show_log_tasks_menu(self):
                task = Tasks()
                task_dict = {'cardio':0,'weights':False,'journal':0.1,'writing':0.1,'water':1,'whole_foods':False,'sugar':True,'learned':False}

                task_dict['cardio'] = input("How many minutes of cardio did you do today?  >> ")
                weights = input("Did you lift weights today? Y / N  >> ")
                if weights ==  'Y' or 'y':
                        task_dict['weights'] = True
                elif weights ==  'N' or 'n':
                         task_dict['weights'] = False

                task_dict['journal'] = input('How many pages did you write in your journal today? >> ')

                task_dict['writing'] = input('How many pages did you read today?  >> ')

                task_dict['water'] = input('How many ounces of water did you drink today?  >> ')

                whole_foods = input("Did you eat whole foods today?  Y / N  > > ")
                if whole_foods ==  'Y' or 'y':
                        task_dict['whole_foods'] = True
                elif whole_foods ==  'N' or 'n':
                         task_dict['whole_foods'] = False
                
                sugar = input("Did you eat sugar today? Y / N >>  ")
                if sugar ==  'Y' or 'y':
                        task_dict['sugar'] = True
                elif sugar ==  'N' or 'n':
                         task_dict['sugar'] = False

                learned = input("Did you learn something new today?  Y / N  >>  ")
                if learned ==  'Y' or 'y':
                        task_dict['learned'] = True
                elif learned ==  'N' or 'n':
                         task_dict['learned'] = False
                task.create_task(**task_dict)



        def show_journals_menu(self):      
                journal = Journals()
                usr = int(input('''Hello, what can I help you with?
        1.) See all Journals
        2.) Write Journals to a text file
        3.) Create journal
        4.) Delete journal
        \t\n >>'''))
                        
                if usr == 1:
                        journal.get_journals_all()
                elif usr == 2:
                        file_name = input("Please enter a filename >>")
                        journal.export_all_
                        journals(file_name)
                elif usr == 3:
                        description  = input("Please enter a description >>")
                        journal.create_journal(description)
                elif usr == 4:
                        journal.get_journals_all()
                        journal_id = input("Please enter the Journal id you wish to delete >> ")
                        journal.delete_journal(journal_id)


        def generate_reports_menu(self):

                # * streaks
                # * cumulative minutes cardio
                # * cumulative minutes weights
                # *cumulative pages written
                # * write file about what you have learned
                pass
 

        # The user can type quit to exit the program
        def quit_menu(self):
                return os.kill(os.getppid(), signal.SIGHUP)

