from Todos import Todos
from connection_helper import connection
import pymysql
import os
import signal

class User(Todos):
        '''User Class - inherits from Connection => User'''        
        def __init__(self, username, password, admin):
                self.logged_in = False
                self.username = username
                self.password = password
                self.admin = admin
                self.UserId = None
                self.set_user_id()
                # self.show()

                
        def show(self):
                print(f"User: {self.username}")
                print(f"UserId: {self.UserId}")
                print(f"Password: *******")
                print(f"Admin: {self.admin}")
                print(f"Logged In: {self.logged_in}")
                print("\n")
                

        def create_user(self):
                try:
                        with connection.cursor() as cursor:
                                sql = 'INSERT INTO Users (username, password, admin) VALUES (%s,%s,%s)'
                                cursor.execute(sql,( self.username, self.password, self.admin))
                                connection.commit()
                                print(f"{self.username} added to Users database")
                except pymysql.Error  as e:
                        print(f"There was an error creating user: {e}")


        def set_user_id(self):
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Users WHERE username = %s'
                                cursor.execute(sql, self.username)
                                result = cursor.fetchone()
                                self.UserId = result['UserId']

                except pymysql.Error  as e:
                        print(f"There was an error when fetching userid {e}")


        # Update self
        def update_user(self,  new_username):
                '''Update the username of the user'''
                try:
                        with connection.cursor() as cursor:
                                sql = 'UPDATE Users SET username = %s WHERE username = %s'
                                cursor.execute(sql, (new_username, self.username))
                                connection.commit()
                                print(f"{self.username} updated to {new_username}")
                except pymysql.Error  as e:
                        print(f"There was an error updating user: {e}")


        # Delete self
        def delete_user(self):
                '''Delete the user'''
                try:
                        with connection.cursor() as cursor:
                                delete_user = input("Are you sure? > Y / N")
                                
                                if delete_user == "Y" or "y":
                                        sql = 'DELETE FROM Users WHERE username = %s'
                                        cursor.execute(sql,str(self.username))
                                        connection.commit()
                                        print(f"{str(self.username)} deleted!")
                                else:
                                        print("User menu")

                except pymysql.Error as e:
                        print(f"There was an error when deleting the user{e}")
        


        # Login
        @staticmethod
        def login_user(self):
                '''Login the user and set logged_in to true. Check admin status'''
                name_input = input("Please enter your username: > ")
                password_input = input("Please enter your password: > ")
                with connection.cursor() as cursor:
                        sql = 'SELECT * FROM Users WHERE username = %s and PASSWORD = %s'
                        cursor.execute(sql, (name_input, password_input))
                        result = cursor.fetchone()
####### add logic for admin flag
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
                '''Logout the user and set logged_in to false'''
                self.logged_in = False
                print("Logged out")
                os.kill(os.getppid(), signal.SIGHUP)




        # Admin only methods

        # Show all users
        def show_users(self):
                '''Show all users if admin'''
                if self.admin:
                        try:
                                with connection.cursor() as cursor:
                                        sql = 'SELECT * FROM Users;'
                                        cursor.execute(sql)
                                        print(cursor.fetchall())
                        except pymysql.Error as e:
                                print(f"There was an error when fetching users table {e}")

#####Finish batching function
        # batch todos to a user
        def batch_to_user(self):
                '''Batch todos to a user if admin'''
                print("inserted batch of todos to user")



Michael = User('Michael Jordan', 'test1234', True)

# Michael.create_todo(Michael.UserId, Michael.username, 'Another one')
# Michael.get_todos_all(Michael.UserId)
Michael.export_todos(Michael.UserId,"todos")