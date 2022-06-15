from Connection import Connection

class User(Connection):
        '''User Class - inherits from Connection => User'''        
        def create_user(self):
                with self.connection.cursor() as cursor:
                        cursor.execute('INSERT INTO Users (username, PASSWORD,admin, created_at, update_at, deleted_at)')

        # Update self
        def update_user(self):
                print('update user')
        # Delete self
        def delete_user(self):
                print('delete user')
        # Login
        def login_user(self):
                print('login user')
        # Logout
        def logout_user(self):
                print('logout user')
        # Admin only methods
        # Show all users
        def show_users(self):
                print('show users')
        # delete a user
        def delete_user(self):
                print('delete user')
        # update a user
        def update_user(self):
                print('update user')

John = User()