import tkinter as tk
import time
#import requests
#import sys
#import datetime
#from tkinter import messagebox
from AdhocTaskDialog import *
from DBManager import *

# Created on : 17. 10. 2023, 17:32:05
# Author     : prohi


class MainWindow(tk.Tk):

    dbManager = None
    
    rightFrame = None
    headerLabel = None
    refreshButton = None
    taskListButton = None
    delegatedTaskListButton = None
    projectListButton = None
    catchBoxButton = None
    calendarButton = None
    revisionButton = None
    maybeListButton = None
    birthdaysListButton = None
    exitButton = None
        
    topFrame = None
    topLeftFrame = None
    topLeftFrameHeader = None
    myDaySignLabel = None
    
    topRightFrame = None
    topRightFrameHeader = None
    dateSignLabel = None
    dateLabel = None
    weekdaySignLabel = None
    weekdayLabel = None
    signLabel = None
    
    middleLeftFrame = None
    middleRightFrame = None
    doneButton = None
    seeTaskButton = None
    doItTommorowButton = None
    moveToButton = None
    deleteButton = None
    remarkFieldLabel = None
    todayTasksListbox = None
    
    bottomLeftFrame = None
    remarkListboxLabel = None
    remarkListbox = None
    
    veryBottomFrame1 = None
    catchItButton = None
    adhocTaskButton = None
    
    veryBottomFrame2 = None
    newTaskButton = None
    
    veryBottomFrame3 = None
    addRemarkButton = None
    addEventButton = None
    
    
#    current_date = datetime.datetime.now()
#    date_string = current_date.strftime("%d/%m/%Y")
#    result_tasks = []
#    tasks_done = []
#    chosen_date = None
#    chosen_deadline = None

    def __init__(self, master=None, dbm=None):
        super().__init__()
        self.dbManager = dbm
        
        self.geometry("800x600")
        self.title("Time Management System 1.1: Main Screen")
        self.resizable(0, 0)
        self.configure(bg="#212121")
        
        self.protocol("WM_DELETE_WINDOW", self.exit_window)
        
        self.createWindow()
        
#        self.cal = Calendar(
#            self.dlg,
#            selectmode='day',
#            date_pattern=('dd/mm/yyyy'),
#            background="black"
#        )
#        self.cal.place(x=330, y=160)

    def insert_data_to_today_tasks():
        print("Hi")
     
    def tasks_list():
        print("Hi")
        
    def task_done():
        print("Hi") 
        
    def see_task():
        print("Hi")  
        
    def do_task_tommorow():
        print("Hi")
    
    def move_task_to():
        print("Hi")
        
    def delete_task_from_database():
        print("Hi")
        
    def catch_idea():
        print("Hi")
        
    def adhoc_task():
        adht = AdhocTaskDialog(self,self.dbManager)
        adht.show
        
    def new_task():
        print("Hi")
        
    def add_remark():
        print("Hi")
        
    def add_event():
        print("Hi")

    def exit_window(self):
#        if len(self.taskDescriptionTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
#            if answer:
#                self.dlg.destroy()
#            else:
#                pass
#        elif len(self.keywordsTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
#            if answer:
#                self.dlg.destroy()
#            else:
#                pass
#        elif len(self.expectedResultTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
#            if answer:
#                self.dlg.destroy()
#            else:
#                pass
#        else:
#            self.dlg.destroy()
        self.destroy()

    def show(self):
        self.win.pack()

    def create_window(self):
        
        self.rightFrame = tk.Frame(
            None,
            width=230,
            height=600,
            background="#2F3030"
        ).place(x=570, y=0)
        
        self.headerLabel = tk.Label(
            self.rightFrame,
            text="TMS 1.1",
            font=('Montserrat', '40'),
            background="#2F3030",
            foreground="#474747"
        ).place(x=15, y=30)

        self.refreshButton = tk.Button(
            self.rightFrame,
            text="REFRESH",
            font=('Arial', '8', 'bold'),
            width=10,
            command=self.insert_data_to_today_tasks,
            background='#00BFC5',
            foreground='#000000'
        ).place(x=140, y=5)

        self.taskListButton = tk.Button(
            self.rightFrame,
            text="MY TASKS",
            font=('Arial', '11'),
            width=21,
            command=self.tasks_list,
            background='#0003C8',
            foreground='#FFFFFF'
        ).place(x=16, y=160)

        self.delegatedTaskListButton = tk.Button(
            self.rightFrame,
            text="DELEGATED TASKS",
            font=('Arial', '11'),
            width=21,
            command=self.delegated_tasks_list,
            background='#0003C8',
            foreground='#FFFFFF'
        ).place(x=16, y=200)

        self.projectListButton = tk.Button(
            self.rightFrame,
            text="PROJECTS",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        ).place(x=16, y=240)

        self.catchBoxButton = tk.Button(
            self.rightFrame,
            text="CATCH-BOX",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        ).place(x=16, y=280)

        self.calendarButton = tk.Button(
            self.rightFrame,
            text="CALENDAR",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        ).place(x=16, y=320)

        self.revisionButton = tk.Button(
            self.rightFrame,
            text="REVISION",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        ).place(x=16, y=360)

        self.maybeListButton = tk.Button(
            self.rightFrame,
            text="MAYBE/SOMETIMES",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        ).place(x=16, y=400)

        self.birthdaysListButton = tk.Button(
            self.rightFrame,
            text="BIRTHDAYS",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        ).place(x=16, y=440)

        self.exitButton = tk.Button(
            self.rightFrame,
            text="EXIT",
            font=('Arial', '11'),
            width=21,
            command=self.exit_window,
            background='#970000',
            foreground='#FFFFFF'
        ).place(x=16, y=480)

        self.topLeftFrame = tk.Frame(
            None,
            width=270,
            height=120,
            background="#2F3030"
        ).place(x=10, y=10)

        self.topLeftFrameHeader = tk.Frame(
            self.topLeftFrame,
            width=250,
            height=90,
            background='#6A6A6A'
        ).place(x=8, y=18)

        self.myDaySign = tk.Label(
            self.topLeftFrameHeader,
            text="MY DAY",
            font=("Open Sans", "30"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        ).place(x=45, y=20)

        self.topRightFrame = tk.Frame(
            None,
            width=270,
            height=120,
            background="#2F3030"
        ).place(x=290, y=10)

        self.topRightFrameHeader = tk.Frame(
            self.topRightFrame,
            width=250,
            height=90,
            background='#6A6A6A'
        ).place(x=8, y=18)

        self.dateSign = tk.Label(
            self.topRightFrameHeader,
            text="Date",
            font=("Open Sans ", "20"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        ).place(x=20, y=8)

        self.dateLabel = tk.Label(
            self.topRightFrameHeader,
            text=time.strftime('%d/%m/%y'),
            font=("Open Sans ", "20"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        ).place(x=95, y=8)

        self.weekdaySign = tk.Label(
            self.topRightFrameHeader,
            text="Day",
            font=("Open Sans ", "20"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        ).place(x=20, y=45)

        self.weekdayLabel = tk.Label(
            self.topRightFrameHeader,
            text=time.strftime('%A'),
            font=("Open Sans ", "20"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        ).place(x=95, y=45)

        self.signLabel = tk.Label(
            self.rightFrame,
            text='by VK',
            font=("Edwardian Script ITC", "25"),
            background='#2F3030',
            foreground='#FFFFFF'
        ).place(x=125, y=550)

        self.middleLeftFrame = tk.Frame(
            None,
            width=320,
            height=235,
            background="#2F3030"
        ).place(x=10, y=155)

        self.middleRightFrame = tk.Frame(
            None,
            width=202,
            height=230,
            background="#2F3030"
        ).place(x=350, y=157)

        self.doneButton = tk.Button(
            self.middleRightFrame,
            text="DONE",
            font=('Arial', '11'),
            width=18,
            command=self.task_done,
            background='#004C01',
            foreground='#FFFFFF'
        ).place(x=20, y=20)

        self.seeTaskButton = tk.Button(
            self.middleRightFrame,
            text="SEE TASK",
            font=('Arial', '11'),
            width=18,
            command=self.see_task,
            background='#027853',
            foreground='#FFFFFF'
        ).place(x=20, y=60)

        self.doItTommorowButton = tk.Button(
            self.middleRightFrame,
            text="DO IT TOMORROW",
            font=('Arial', '11'),
            width=18,
            command=self.do_task_tomorrow,
            background='#027853',
            foreground='#FFFFFF'
        ).place(x=20, y=100)

        self.moveToButton = tk.Button(
            self.middleRightFrame,
            text="MOVE TO",
            font=('Arial', '11'),
            width=18,
            command=self.move_task_to,
            background='#027853',
            foreground='#FFFFFF'
        ).place(x=20, y=140)

        self.deleteButton = tk.Button(
            self.middleRightFrame,
            text="DELETE",
            font=('Arial', '11'),
            width=18,
            command=self.delete_task_from_database,
            background='#970000',
            foreground='#FFFFFF'
        ).place(x=20, y=180)

        self.remarkFieldLabel = tk.Label(
            self.middleLeftFrame,
            text="Tasks for today:",
            font=("Open Sans", "12", "bold"),
            background="#2F3030",
            foreground="#000000"
        ).place(x=10, y=6)

        self.todayTasksListbox = tk.Listbox(
            self.middleLeftFrame,
            width=42,
            height=11,
            selectforeground="#FFFFFF",
            selectbackground="#181818",
            font=("Arial", "10", "bold"),
            foreground="#C2C2C2",
            background="#303030"
        ).place(x=11, y=38)

        self.bottomLeftFrame = tk.Frame(
            None,
            width=320,
            height=150,
            background="#2F3030"
        ).place(x=10, y=400)

        self.remarkListboxLabel = tk.Label(
            self.bottomLeftFrame,
            text="Remarks for today:",
            font=("Open Sans", "12", "bold"),
            background="#2F3030",
            foreground="#000000"
        ).place(x=10, y=6)

        self.remarkListbox = tk.Listbox(
            self.bottomLeftFrame,
            width=49,
            height=6,
            background="#303030"
        ).place(x=10, y=35)

        self.veryBottomFrame1 = tk.Frame(
            None,
            width=230,
            height=35,
            background="#2F3030"
        ).place(x=10, y=565)

        self.catchItButton = tk.Button(
            self.veryBottomFrame1,
            text="CATCH THE IDEA",
            font=('Arial', '8', 'bold'),
            width=14,
            command=self.catch_idea,
            background='#4F0082',
            foreground='#FFFFFF'
        ).place(x=10, y=5)

        self.adhocTaskButton = tk.Button(
            self.veryBottomFrame1,
            text="ADHOC TASK",
            font=('Arial', '8', 'bold'),
            width=13,
            command=self.adhoc_task,
            background='#A94102',
            foreground='#FFFFFF'
        ).place(x=125, y=5)

        self.veryBottomFrame2 = tk.Frame(
            None,
            width=110,
            height=50,
            background="#2F3030"
        ).place(x=240, y=555)

        self.newTaskButton = tk.Button(
            self.veryBottomFrame2,
            text="NEW TASK",
            font=('Arial', '9', 'bold'),
            width=13,
            height=2,
            command=self.new_task,
            background='#004C01',
            foreground='#FFFFFF'
        ).place(x=5, y=2)

        self.veryBottomFrame3 = tk.Frame(
            None,
            width=220,
            height=35,
            background="#2F3030"
        ).place(x=347, y=565)

        self.addRemarkButton = tk.Button(
            self.veryBottomFrame3,
            text=" ADD REMARK",
            font=('Arial', '8', 'bold'),
            width=13,
            command=self.add_remark,
            background='#9E019A',
            foreground='#FFFFFF'
        ).place(x=8, y=5)

        self.addEventButton = tk.Button(
            self.veryBottomFrame3,
            text=" ADD EVENT",
            font=('Arial', '8', 'bold'),
            width=13,
            command=self.add_event,
            background='#A8A803',
            foreground='#FFFFFF'
        ).place(x=116, y=5)
        
        self.pack()