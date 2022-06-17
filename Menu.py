from Todos import Todos 
from Tasks import Tasks


class Menu(Todos):
        '''Menu Class'''


        def main_menu(self):
#         ## What would you like to do?
#         * Todos Menu
#         * Log Daily Tasks
#         * Generate Reports
                pass
                

        def show_todos_menu(self):      
                # # Todos Menu

#         * See todos
#         * Write todos to file
#         * Create todo
#         * Update todo
#         * Delete todo
         
                pass


        def show_log_tasks_menu(self):
                task = Tasks()
                task_dict = {'cardio':0,'weights':False,'journal':0.1,'writing':0.1,'water':1,'whole_foods':False,'sugar':True,'learned':False}

                task_dict['cardio'] = input("How many minutes of cardio did you do today?  >> ")
                weights = input("Did you lift weights today? Y / N  >> ")
                if weights ==  'Y' or 'y':
                        task_dict['weights'] = True
                elif sugar ==  'N' or 'n':
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

                


        def generate_reports_menu(self):

                # * streaks
                # * cumulative minutes cardio
                # * cumulative minutes weights
                # *cumulative pages written
                # * write file about what you have learned
                pass
 

        # The user can type quit to exit the program
        def quit_menu(self):
                pass

