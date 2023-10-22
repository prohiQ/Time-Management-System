import datetime
import sqlite3
from tkinter import messagebox
# Created on : 14. 10. 2023, 14:26:26
# Author     : prohi

class DBManager():
    
    conn = None
    dconn = None
    cursor = None
    dcursor = None
    
    def __init__(self, dbPath):
        self.conn = sqlite3.connect(dbPath)
        self.cursor = self.conn.cursor()
        
        self.dconn = sqlite3.connect('delegated_tasks.db')
        self.dcursor = self.dconn.cursor()
        
    def saveAdhocTask(self, values):
        try:
            query = "INSERT INTO tasks (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, values.values())

            self.conn.commit()
            self.cursor.close()

        except Exception as e:
            messagebox.showerror("Error", "OOPS! " + str(e))
            
    def saveTask(self, values):
        try:
            query = "INSERT INTO tasks (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, values)

            self.conn.commit()
            self.cursor.close()

        except Exception as e:
            messagebox.showerror("Error", "OOPS! " + str(e))
            
    def saveDelegatedTask(self, values):
        try:
            query = "INSERT INTO delegated_tasks (task_ID, task_or_action,"
            " keywords, expected_result, date, deadline, delegate_to,"
            " cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            
            self.cursor.execute(query, values)

            self.conn.commit()
            self.cursor.close()

        except Exception as e:
            messagebox.showerror("Error", "OOPS! " + str(e))
    
    def saveRemark(self, values):
        try:
#            query = "INSERT INTO tasks (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
#            self.cursor.execute(query, values)

            self.conn.commit()
            self.cursor.close()

        except Exception as e:
            messagebox.showerror("Error", "OOPS! " + str(e))
            
    def getTasks(self, values):
        try:
            query = "INSERT INTO tasks (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, values)

            self.conn.commit()
            self.cursor.close()

        except Exception as e:
            messagebox.showerror("Error", "OOPS! " + str(e))
      
    def findOne(self, tableName, id):
        try:
            query = "SELECT * FROM {0} WHERE id={1}", tableName, id
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            
#            self.conn.commit()
#            self.cursor.close()

        except Exception as e:
            messagebox.showerror("Error", "OOPS! " + str(e))
        return res
          
    def findAll(self, tableName):
        try:
            query = "SELECT * FROM {0}", tableName
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            
#            self.conn.commit()
#            self.cursor.close()

        except Exception as e:
            messagebox.showerror("Error", "OOPS! " + str(e))
        return res
        
    def createTMSdatabase(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks'
            ' (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT,'
            ' keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT,'
            ' delegate_to TEXT, cooperate_with TEXT)')
            
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks'
            ' (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT,'
            ' keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT,'
            ' delegate_to TEXT, cooperate_with TEXT)')
            
        self.cursor.execute('CREATE TABLE IF NOT EXISTS delegated_tasks'
            ' (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT,'
            ' keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT,'
            ' delegate_to TEXT, cooperate_with TEXT)')
            
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks'
            ' (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT,'
            ' keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT,'
            ' delegate_to TEXT, cooperate_with TEXT)')
            
        