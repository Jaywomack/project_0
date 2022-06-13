# Revature_Project_0 Jay Womack

&nbsp;

# Python | MySQL | CLI To-Do App

## **Description:** A classic To-Do application that allows users to create an account and create todos that are stored, completed and tabulated for viewing later.

&nbsp;

## Development LifeCycle

---

&nbsp;

### 1. Plan

### 2. Design

### 3. Code

### 4. Test

### 5. Deploy

&nbsp;

# User Stories

&nbsp;

## Base Level User

---

&nbsp;

> ## As a user of the CLI App I want to be able to write todos and save them so I can check them off as I complete them.

&nbsp;

> ## As a user of the CLI App it would be useful if my todos were sorted by still needing to be done, in progress, and todos that are complete.

&nbsp;

> ## As a user of the CLI App it would be nice if I could create todos and still be able to update them if I made a mistake.

&nbsp;

> ## As a user of the CLI App it would be nice if I could delete a todo that I decide I no loner want.

&nbsp;

> ## As a admin of the CLI App it would be nice if I could easily look at a user's account and see all of their information printed to the console in a way that is informative and useful to seeing what the user is doing and has been doing recently.

&nbsp;

> ## As an admin it would be useful to have a way to compare productivity between users. It would be nice to have metrics that tell how many tasks the user has made and completed. It would be useful to have multiple

&nbsp;

## Users can log in on the command line as a user or as an admin.

&nbsp;

## For a user the current options are:

&nbsp;

> ## The current todos are displayed

&nbsp;

> ## The user is prompted to open menu or quit

&nbsp;

> ## The user can type menu to see the menu

&nbsp;

> ## The user can type quit to exit the program

&nbsp;

> ## From the menu the user can:

&nbsp;

> ## add a new todo

&nbsp;

> ## view all the todos

&nbsp;

> ## view all the completed todos

&nbsp;

> ## view all the uncompleted todos to a certain date

&nbsp;

> ## view all the uncompleted todos

&nbsp;

> ## mark a todo as complete

&nbsp;

> ## Lookup todo by name and edit a todo

&nbsp;

> ## delete a todo

---

&nbsp;

### If the user is an admin the current options are:

> ## view all the todos by a specific user

&nbsp;

> ## view all the completed todos by a specific user

&nbsp;

> ## view all the uncompleted todos by a specific user

&nbsp;

> ## view all the todos by a specific date

&nbsp;

> ## view all the completed todos by a specific date

&nbsp;

> ## view all the uncompleted todos by a specific date

&nbsp;

> ## create a performance report from a specific user

---

&nbsp;

# Tech Stack

> ## Python 3.9.13

> ## Vs Code 1.68.0

> ## MySQL 8.0.29

---

&nbsp;

# Packages:

&nbsp;

> ## Rich for colorful terminals

> ## sql-connector-python for database connection

> ## datetime for date and time

> ## argparse for command line arguments

> ## sys for system functions

> ## os for operating system functions

> ## re for regular expressions

> ## Dotenv for hiding variables

---

# Tables

&nbsp;

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
