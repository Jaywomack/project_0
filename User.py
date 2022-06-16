from Connection import Connection
import pymysql
import os
import signal

class User(Connection):
        '''User Class - inherits from Connection => User'''        
        def __init__(self, username, password, admin):
                super().__init__()
                self.logged_in = False
                self.username = str(username)
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
        def update_user(self,  new_username):
                try:
                        with self.connection.cursor() as cursor:
                                sql = 'UPDATE Users SET username = %s WHERE username = %s'
                                cursor.execute(sql, (new_username, self.username))
                                self.connection.commit()
                                print(f"{self.username} updated to {new_username}")
                except pymysql.Error  as e:
                        print(f"There was an error updating user: {e}")


        # Delete self
        def delete_user(self):
                try:
                        with self.connection.cursor() as cursor:
                                delete_user = input("Are you sure? > Y / N")
                                
                                if delete_user == "Y" or "y":
                                        sql = 'DELETE FROM Users WHERE username = %s'
                                        cursor.execute(sql,str(self.username))
                                        self.connection.commit()
                                        print(f"{str(self.username)} deleted!")
                                else:
                                        print("User menu")

                except pymysql.Error as e:
                        print(f"There was an error when deleting the user{e}")
        


        # Login
        def login_user(self):
                name_input = input("Please enter your username: > ")
                password_input = input("Please enter your password: > ")
                with self.connection.cursor() as cursor:
                        sql = 'SELECT * FROM Users WHERE username = %s and PASSWORD = %s'
                        cursor.execute(sql, (name_input, password_input))
                        result = cursor.fetchone()
                        if result:
                                print(f"Welcome {name_input} to ProjectZero Todo List")
                                self.logged_in = True
                                return self.logged_in
                        else:
                                print("Invalid username or password")
                                self.logged_in = False
                                return self.logged_in



        # Logout and set logged_in to false
        def logout_user(self):
                self.logged_in = False
                print("Logged out")
                os.kill(os.getppid(), signal.SIGHUP)




        # Admin only methods

        # Show all users
        def show_users(self):
                print('show users')
                exit()

        # batch todos to a user
        def batch_to_user(self):
                print("patched to user")





 
user = User('John Stockton', 'test1234', True)
user.login_user()
print(user.logged_in)
user.logout_user()
print(user.logged_in)

print('test')
