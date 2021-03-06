from connection_helper import connection
import pymysql
import time
from tabulate import tabulate

class Journals():
        '''journal Class'''

        def create_journal(self, description):
                '''Function that creates a new journal from user input and persists it to the database'''
                try:
                        with connection.cursor() as cursor:
                                sql = 'INSERT INTO Journals ( Description, created) VALUES (%s,%s)'
                                cursor.execute(sql, (description, time.strftime('%Y-%m-%d %H:%M:%S'))
                                )
                                connection.commit()
                                print(f"journal:>> {description[:25]} created")

                except pymysql.Error  as e:
                        print(f"There was an error creating user: {e}")


        def update_journal(self):
                '''Function that updates a journal from user input and persists it to the database'''
                try:
                        with connection.cursor() as cursor:
                                self.get_journals_all()
                                journal_id = input("Enter the journal ID you want to update: >> ")
                                description = input("Enter the new description: >> ")
                                sql = 'UPDATE Journals SET DESCRIPTION = %s WHERE JOURNALID = %s'
                                cursor.execute(sql, (description, journal_id))
                                connection.commit()
                                print(f"journal {journal_id} has been updated.")

                except pymysql.Error as e:
                        print(f"There was an error updating the Journal {e}")

        def get_journals_all(self):
                '''Function that returns all journals in the database'''
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Journals'
                                cursor.execute(sql)
                                print("Your List of journals: ")
                                data = [[x['JournalID'], x['Description'][:50]] for x in cursor.fetchall()]
                                print(tabulate(data))
                except pymysql.Error as e:
                        print(f'There was an error retrieving your request. {e}')
                

        def export_all_journals(self, name_file):
                '''Function that exports all journals to a csv file'''
                try:
                        with connection.cursor() as cursor:
                                sql = 'SELECT * FROM Journals'
                                cursor.execute(sql)
                                f = open(f"{name_file}.txt","w")
                                [f.writelines(f"Journal {i+1}:\n\n{x['Description']}\n\n") for i,x in enumerate(cursor.fetchall())]
                                print(f"journals written to file {name_file}")
                except pymysql.Error as e:
                        print(f'There was an error retrieving your request. {e}')


        def delete_journal(self, journal_id):
                '''Function that deletes a journal from the database based on the journal ID input by the user'''
                try:
                        with connection.cursor() as cursor:
                                sql = 'DELETE FROM Journals WHERE JournalID = %s'
                                cursor.execute(sql, (journal_id))
                                connection.commit()
                                print(f"journal {journal_id} has been deleted.")
                except pymysql.Error as e:
                        print(f"There was an error deleting the journal {e}")
