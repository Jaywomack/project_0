from Connection import Connection
import pymysql

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
                print('login user')


        # Logout
        def logout_user(self):
                print('logout user')


        # Admin only methods

        # Show all users
        def show_users(self):
                print('show users')

        # batch todos to a user
        def batch_to_user(self):
                print("patched to user")





 
user = User(str('Shaq'), 'test1234', True)
user.delete_user()


