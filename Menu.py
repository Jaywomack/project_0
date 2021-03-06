from connection_helper import connection
from Todos import Todos 
from Journals import Journals 
from Tasks import Tasks
import os
import signal

class Menu(Todos):
        '''Menu Class
        methods:
        main_menu()
        show_todos_menu()
        show_log_tasks_menu()
        show_journals_menu()
        quit_menu()
        '''

        def main_menu(self):
                '''main_menu - receives user input and calls one of these functions depending on user input:
                show_todos_menu,
                show_log_tasks_menu,
                show_journals_menu,
                quit_menu.'''

                print('Welcome to Your Productivity App\n')
                print("""
        1.) Todos
        2.) Tasks
        3.) Journal
        4.) Quit
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
                        self.quit_menu()
                

        def show_todos_menu(self):    
                '''show_todos_menu - recieves user input and calls one of these functions depending on user input:
                create_todo,
                get_all_todos,
                get_todo_by_id,
                update_todo,
                delete_todo,
                quit_menu.'''

                todo = Todos()
                usr = int(input('''Hello, what can I help you with?
        1.) See all todos
        2.) Export todos to a text file
        3.) Create todo
        4.) Delete todo
        \t\n >>'''))
                
                if usr == 1:
                        todo.get_todos_all()
                        input("Hit ENTER")
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
                '''show_log_tasks_menu - recieves user input and calls one of these functions depending on user input:
                create_task,
                get_all_tasks,
                ingest_task_data,
                export_tasks.
                '''

                task = Tasks()
                task_input = int(input('''Hello, what can I help you with?
        1.) Log Daily Tasks
        2.) Get Past Tasks
        3.) Ingest Tasks Data From Excel File
        4.) Export Tasks Data to .csv

        \t\n >> '''))
                if task_input == 1:
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
                elif task_input == 2:
                        task.get_all_tasks()
                        input("Hit ENTER")
                elif task_input == 3:
                        task.ingest_task_data()
                        input("Hit ENTER")
                elif task_input == 4:
                        task.export_tasks()
                        input("Hit ENTER")


        def show_journals_menu(self): 
                '''show_journals_menu - recieves user input and calls one of these functions depending on user input:
                get_journals_all,
                export_all_journals,
                create_journal,
                delete_journal,
                update_journal'''

                journal = Journals()
                usr = int(input('''Hello, what can I help you with?
        1.) See all Journals
        2.) Write Journals to a text file
        3.) Create journal
        4.) Delete journal
        5.) Update journal
        \t\n >>'''))
                        
                if usr == 1:
                        journal.get_journals_all()
                        input("Hit ENTER")
                elif usr == 2:
                        file_name = input("Please enter a filename >>")
                        journal.export_all_journals(file_name)
                elif usr == 3:
                        description  = input("Please enter a description >>")
                        journal.create_journal(description)
                elif usr == 4:
                        journal.get_journals_all()
                        journal_id = input("Please enter the Journal id you wish to delete >> ")
                        journal.delete_journal(journal_id)
                elif usr == 5:
                        journal.update_journal()


        def quit_menu(self):
                '''closes connection and kills terminal'''
                connection.close()
                return os.kill(os.getppid(), signal.SIGHUP)
