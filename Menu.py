import User 

class Menu(User):
        # From the menu the user can:
        def __init__(self):
                pass
        
        # Login Menu
        def login_menu(self):
                # Welcome prompt

                # Login prompt

                # If the user is an admin, they can see the admin login menu

                # If the user is not found, the user is prompted to create a new user

                # If the user is found, the user is prompted to login

                pass

        # The user is prompted to open menu or quit
        # The user can type menu to see the menu
        def show_user_menu(self):
                # the menu should have tasks that can completed on a todo:
                # 1. view all todos
                # 2. view all uncompleted todos
                # 3. view all completed todos
                # 4. view all todos to a certain date
                # 5. mark a todo as complete
                # 6. lookup a todo by name and edit/delete a todo
                # 7. export todos to a file
                pass

        # Show admin menu
        def show_admin_menu(self):
                # menuitem - todos completed in a time range
                # menuitem - todo average time to completion 
                # menuitem - todo total completed
                # menuitem - todo performance
                pass

        # The user can type quit to exit the program
        def quit_menu(self):
                pass

