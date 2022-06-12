# Revature_Project_0 Jay Womack

# Python | MySQL | CLI To-Do App

> ---
>
> ---

## **Description:** A classic To-Do application that allows users to create an account and create todos that are stored, completed and tabulated for viewing later.

---

### 1. Plan

### 2. Design

### 3. Code

### 4. Test

### 5. Deploy

---

# User Stories

## Users can log in on the command line as a user or as an admin.

### For a user the current options are:

> The current todos are displayed

> The user is prompted to open menu or quit

> The user can type menu to see the menu

> The user can type quit to exit the program

> From the menu the user can:

> add a new todo

> view all the todos

> view all the completed todos

> view all the uncompleted todos to a certain date

> view all the uncompleted todos

> mark a todo as complete

> Lookup todo by name and edit a todo

> delete a todo

---

### If the user is an admin the current options are:

> view all the todos by a specific user

> view all the completed todos by a specific user

> view all the uncompleted todos by a specific user

> view all the todos by a specific date

> view all the completed todos by a specific date

> view all the uncompleted todos by a specific date

> create a performance report from a specific user

---

# Tech Stack

> Python 3.9.13

> Vs Code 1.68.0

> MySQL 8.0.29

# Packages:

> Rich for colorful terminals

> sql-connector-python for database connection

> datetime for date and time

> argparse for command line arguments

> sys for system functions

> os for operating system functions

> re for regular expressions

> Dotenv for hiding variables

---

# Tables

        ## Users
                ### Fields:
                        #### Id primary key auto incrementing
                        #### Username varchar255
                        #### Password stored as hash
                        #### Admin boolean
                        #### Created_at datetime
                        #### Updated_at datetime
                        #### Deleted_at datetime



        # Todos
                ### Fields:
                        #### Id
                        #### Category? Todo or In Process or Complete
                        #### Username foreign key to users table
                        #### Description varchar255
                        #### Date varchar255
                        #### Time varchar255
                        #### Complete boolean
                        #### CompleteDate varchar255
                        #### CompleteTime varchar255
