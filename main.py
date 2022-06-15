from User import User
from Todos import Todos
from Menu import Menu

menu = Menu()
print("From menu object")
menu.create_user()

NewTodo = Todos()
print("From Todos object")
NewTodo.create_user()


John = User()  
print('From connection object')
print(John.show_tables())
print(John.show_db_users())
