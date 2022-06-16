from Connection import Connection
import pymysql

class User(Connection):
        '''User Class - inherits from Connection => User'''        
        def __init__(self, username, password, admin):
                super().__init__()
                self.logged_in = False
                self.username = username
                self.password = password
                self.admin = admin
                
        def create_user(self):
                try:
                        with self.connection.cursor() as cursor:
                                sql = 'INSERT INTO Users (username, password, admin) VALUES (%s,%s,%s)'
                                cursor.execute(sql,( self.username, self.password, self.admin))
                                self.connection.commit()
                                print(f"{self.username} added to Users database")
                except pymysql.Error  as e:
                        print(f"There was an error creating user: {e}")


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


John = User('Michael Jordan', 'test1234', True)
John.create_user()