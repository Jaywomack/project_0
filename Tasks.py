from connection_helper import connection
import pymysql
import pandas as pd
import time    
from tabulate import tabulate
from sqlalchemy import create_engine

class Tasks:
        
        def export_tasks(self):
                '''Function that exports tasks to a csv file'''
                try:
                        with connection:
                                name_file = input('What would you like to name your file?')
                                sql ='SELECT * FROM Tasks;'
                                tasks_df = pd.read_sql(sql,connection)
                                return tasks_df.to_csv(f'{name_file}.csv')

                except pymysql.Error as e:
                        print(e)

        def ingest_task_data(self):
                '''Function that imports tasks from a csv file into the database'''
                try:
                        xl_file = pd.ExcelFile('./task_sheet.xlsx')
                        xl_df = xl_file.parse(sheet_name='task_log')
                        engine = create_engine("mysql+pymysql://{user}:{pw}@revature-project-db-do-user-8494246-0.b.db.ondigitalocean.com:25060/ProjectZero"
                        .format(user="jay",
                                pw="test1234"))
                        xl_df.to_sql('Tasks', con = engine, if_exists = 'append', chunksize = 1000, index = False)
                        print("Tasks added to database")

                except pymysql.Error as e:
                        print(e)

        def create_task(self,cardio,weights,journal,writing,water,whole_foods,sugar,learned):
                '''Function that creates a new task from user input and persists it to the database'''
                try:
                        with connection.cursor() as cursor:
                                sql = 'INSERT INTO Tasks(created,cardio,weights,journal,writing,water,whole_foods,sugar,learned) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                cursor.execute(sql, (time.strftime('%Y-%m-%d %H:%M:%S'),cardio,weights,journal,writing,water,whole_foods,sugar,learned))
                                connection.commit()
                                print("Added daily tasks")

                except pymysql.Error as e:
                        print(f"Error creating task {e}")

        def get_all_tasks(self):
                '''Function that returns all tasks in the database'''
                try:
                        with connection.cursor() as cursor:
                                lookback = int(input("How many days would you like to lookback?"))
                                sql = 'SELECT * FROM Tasks LIMIT %s'
                                cursor.execute(sql,(lookback))
                                print(tabulate(cursor.fetchall(), headers='keys'))

                except pymysql.Error as e:
                        print(f"There was an error getting your tasks {e}")

        def delete_task(self):
                '''Function that deletes a task from the database based on the task id based on input from the user'''
                
                task_to_delete = input("Please enter a task number for which task you would like to delete > ")
                try:
                        with connection.cursor() as cursor:
                                sql='DELETE FROM Tasks WHERE TaskID = %s'
                                cursor.execute(sql, (task_to_delete))
                                connection.commit()
                                print(f"Todo {task_to_delete} has been deleted.")

                except pymysql.Error as e:
                        print(f"There was am error deleting the task {e}")

