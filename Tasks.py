from connection_helper import connection
import pymysql
import time    
from tabulate import tabulate



class Tasks:
        
        
        def ingest_task_data(self):
                pass

        def create_task(self,cardio,weights,journal,writing,water,whole_foods,sugar,learned):
                try:
                        with connection.cursor() as cursor:
                                sql = 'INSERT INTO Tasks(created,cardio,weights,journal,writing,water,whole_foods,sugar,learned) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                cursor.execute(sql, (time.strftime('%Y-%m-%d %H:%M:%S'),cardio,weights,journal,writing,water,whole_foods,sugar,learned))
                                connection.commit()
                                print("Added daily tasks")

                except pymysql.Error as e:
                        print(f"Error creating task {e}")

        def get_all_tasks(self):
                try:
                        with connection.cursor() as cursor:
                                lookback = int(input("How many days would you like to lookback?"))
                                sql = 'SELECT * FROM Tasks LIMIT %s'
                                cursor.execute(sql,(lookback))
                                print(tabulate(cursor.fetchall(), headers='keys'))

                except pymysql.Error as e:
                        print(f"There was an error getting your tasks {e}")

        def delete_task(self):
                task_to_delete = input("Please enter a task number for which task you would like to delete > ")
                try:
                        with connection.cursor() as cursor:
                                sql='DELETE FROM Tasks WHERE TaskID = %s'
                                cursor.execute(sql, (task_to_delete))
                                connection.commit()
                                print(f"Todo {task_to_delete} has been deleted.")

                except pymysql.Error as e:
                        print(f"There was am error deleting the task {e}")

task = Tasks()
# task.create_task(60,True,6.5,6.5,128,True,True,True)
# task.delete_task()