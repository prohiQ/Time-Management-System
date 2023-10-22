import tkinter as tk
import time
import requests
#import sys
#import datetime
#from tkinter import messagebox
from AdhocTaskWindow import *
from EventWindow import *
from CatchIdeaWindow import *
from RemarkWindow import *
from TaskOverviewWindow import *
from TaskWindow import *
from DBManager import *

# Created on : 17. 10. 2023, 17:32:05
# Author     : prohi


class MainWindow(tk.Tk):
   
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
        
#        self.cal = Calendar(
#            self.dlg,
#            selectmode='day',
#            date_pattern=('dd/mm/yyyy'),
#            background="black"
#        )
#        self.cal.place(x=330, y=160)

    def insert_data_to_today_tasks(self):
        print("Hi")
     
    def tasks_list(self):
        print("Hi")
        
    def task_done(self):
        print("Hi") 
        
    def see_task(self):
        print("Hi")  
        
    def do_task_tomorrow(self):
        print("Hi")
    
    def move_task_to(self):
        print("Hi")
        
    def delete_task_from_database(self):
        print("Hi")
        
    def delegated_tasks_list(self):
        print("Hi")
        
    def catch_idea(self):
        ci = CatchIdeaWindow(self.dbManager)
        ci.show()
        
    def adhoc_task(self):
        adht = AdhocTaskWindow(self.dbManager)
        adht.show()
        
    def new_task(self):
        tsk = TaskWindow(self.dbManager)
        tsk.show()
        
    def add_remark(self):
        rmk = RemarkWindow(self.dbManager)
        rmk.show()
        
    def add_event(self):
        addevt = EventWindow(self.dbManager)
        addevt.show()

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

    def check_internet(self):
        url = "https://www.google.com"
        timeout = 5
        try:
            _ = requests.get(url, timeout=timeout)
            self.onlineFrame1.configure(background="#007606")
            self.onlineFrame2.configure(background="#007606")
        except requests.ConnectionError:
            self.onlineFrame1.configure(background="#9B0202")
            self.onlineFrame2.configure(background="#9B0202")
        self.after(10000, self.check_internet)

    def show(self):
        self.create_window()
        
        self.mainloop()
        self.after(10000, self.check_internet)

    def create_window(self):
        self.build_right_frame()
        self.build_top_left_frame()
        self.build_top_right_frame()
        self.build_middle_left_frame()
        self.build_middle_right_frame()
        self.build_bottom_left_frame()
        self.build_very_bottom_frame1()
        self.build_very_bottom_frame2()
        self.build_very_bottom_frame3()
        
        self.check_internet()

    def build_right_frame(self):
        self.rightFrame = tk.Frame(
            None,
            width=230,
            height=600,
            background="#2F3030"
        )
        self.rightFrame.place(x=570, y=0)
        
        self.headerLabel = tk.Label(
            self.rightFrame,
            text="TMS 1.1",
            font=('Montserrat', '40'),
            background="#2F3030",
            foreground="#474747"
        )
        self.headerLabel.place(x=15, y=30)

        self.refreshButton = tk.Button(
            self.rightFrame,
            text="REFRESH",
            font=('Arial', '8', 'bold'),
            width=10,
            command=self.insert_data_to_today_tasks,
            background='#00BFC5',
            foreground='#000000'
        )
        self.refreshButton.place(x=140, y=5)

        self.taskListButton = tk.Button(
            self.rightFrame,
            text="MY TASKS",
            font=('Arial', '11'),
            width=21,
            command=self.tasks_list,
            background='#0003C8',
            foreground='#FFFFFF'
        )
        self.taskListButton.place(x=16, y=160)

        self.delegatedTaskListButton = tk.Button(
            self.rightFrame,
            text="DELEGATED TASKS",
            font=('Arial', '11'),
            width=21,
            command=self.delegated_tasks_list,
            background='#0003C8',
            foreground='#FFFFFF'
        )
        self.delegatedTaskListButton.place(x=16, y=200)

        self.projectListButton = tk.Button(
            self.rightFrame,
            text="PROJECTS",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        )
        self.projectListButton.place(x=16, y=240)

        self.catchBoxButton = tk.Button(
            self.rightFrame,
            text="CATCH-BOX",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        )
        self.catchBoxButton.place(x=16, y=280)

        self.calendarButton = tk.Button(
            self.rightFrame,
            text="CALENDAR",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        )
        self.calendarButton.place(x=16, y=320)

        self.revisionButton = tk.Button(
            self.rightFrame,
            text="REVISION",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        )
        self.revisionButton.place(x=16, y=360)

        self.maybeListButton = tk.Button(
            self.rightFrame,
            text="MAYBE/SOMETIMES",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        )
        self.maybeListButton.place(x=16, y=400)

        self.birthdaysListButton = tk.Button(
            self.rightFrame,
            text="BIRTHDAYS",
            font=('Arial', '11'),
            width=21,
            command=None,
            background='#0003C8',
            foreground='#FFFFFF'
        )
        self.birthdaysListButton.place(x=16, y=440)

        self.exitButton = tk.Button(
            self.rightFrame,
            text="EXIT",
            font=('Arial', '11'),
            width=21,
            command=self.exit_window,
            background='#970000',
            foreground='#FFFFFF'
        )
        self.exitButton.place(x=16, y=480)
        
        self.signLabel = tk.Label(
            self.rightFrame,
            text='by VK',
            font=("Edwardian Script ITC", "25"),
            background='#2F3030',
            foreground='#FFFFFF'
        )
        self.signLabel.place(x=125, y=550)
         
    def build_top_left_frame(self):
        self.topLeftFrame = tk.Frame(
            None,
            width=270,
            height=120,
            background="#2F3030"
        )
        self.topLeftFrame.place(x=10, y=10)
        
        self.onlineFrame1 = tk.Frame(
            self.topLeftFrame,
            width=250,
            height=5,
            background="#007606"
        )
        self.onlineFrame1.place(x=8, y=12)

        self.topLeftFrameHeader = tk.Frame(
            self.topLeftFrame,
            width=250,
            height=90,
            background='#6A6A6A'
        )
        self.topLeftFrameHeader.place(x=8, y=18)

        self.myDaySign = tk.Label(
            self.topLeftFrameHeader,
            text="MY DAY",
            font=("Open Sans", "30"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        )
        self.myDaySign.place(x=45, y=20)
    
    def build_top_right_frame(self):
        self.topRightFrame = tk.Frame(
            None,
            width=270,
            height=120,
            background="#2F3030"
        )
        self.topRightFrame.place(x=290, y=10)
        
        self.onlineFrame2 = tk.Frame(
            self.topRightFrame,
            width=250,
            height=5,
            background="#007606"
        )
        self.onlineFrame2.place(x=8, y=12)

        self.topRightFrameHeader = tk.Frame(
            self.topRightFrame,
            width=250,
            height=90,
            background='#6A6A6A'
        )
        self.topRightFrameHeader.place(x=8, y=18)

        self.dateSign = tk.Label(
            self.topRightFrameHeader,
            text="Date",
            font=("Open Sans ", "20"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        )
        self.dateSign.place(x=20, y=8)

        self.dateLabel = tk.Label(
            self.topRightFrameHeader,
            text=time.strftime('%d/%m/%y'),
            font=("Open Sans ", "20"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        )
        self.dateLabel.place(x=95, y=8)

        self.weekdaySign = tk.Label(
            self.topRightFrameHeader,
            text="Day",
            font=("Open Sans ", "20"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        )
        self.weekdaySign.place(x=20, y=45)

        self.weekdayLabel = tk.Label(
            self.topRightFrameHeader,
            text=time.strftime('%A'),
            font=("Open Sans ", "20"),
            background="#6A6A6A",
            foreground="#FFFFFF"
        )
        self.weekdayLabel.place(x=95, y=45)
    
    def build_middle_left_frame(self):
        self.middleLeftFrame = tk.Frame(
            None,
            width=320,
            height=235,
            background="#2F3030"
        )
        self.middleLeftFrame.place(x=10, y=155)
        
        self.remarkFieldLabel = tk.Label(
            self.middleLeftFrame,
            text="Tasks for today:",
            font=("Open Sans", "12", "bold"),
            background="#2F3030",
            foreground="#000000"
        )
        self.remarkFieldLabel.place(x=10, y=6)

        self.todayTasksListbox = tk.Listbox(
            self.middleLeftFrame,
            width=42,
            height=11,
            selectforeground="#FFFFFF",
            selectbackground="#181818",
            font=("Arial", "10", "bold"),
            foreground="#C2C2C2",
            background="#303030"
        )
        self.taskListButton.place(x=11, y=38)
    
    def build_middle_right_frame(self):
        self.middleRightFrame = tk.Frame(
            None,
            width=202,
            height=230,
            background="#2F3030"
        )
        self.middleRightFrame.place(x=350, y=157)
        
        self.doneButton = tk.Button(
            self.middleRightFrame,
            text="DONE",
            font=('Arial', '11'),
            width=18,
            command=self.task_done,
            background='#004C01',
            foreground='#FFFFFF'
        )
        self.doneButton.place(x=20, y=20)

        self.seeTaskButton = tk.Button(
            self.middleRightFrame,
            text="SEE TASK",
            font=('Arial', '11'),
            width=18,
            command=self.see_task,
            background='#027853',
            foreground='#FFFFFF'
        )
        self.seeTaskButton.place(x=20, y=60)

        self.doItTommorowButton = tk.Button(
            self.middleRightFrame,
            text="DO IT TOMORROW",
            font=('Arial', '11'),
            width=18,
            command=self.do_task_tomorrow,
            background='#027853',
            foreground='#FFFFFF'
        )
        self.doItTommorowButton.place(x=20, y=100)

        self.moveToButton = tk.Button(
            self.middleRightFrame,
            text="MOVE TO",
            font=('Arial', '11'),
            width=18,
            command=self.move_task_to,
            background='#027853',
            foreground='#FFFFFF'
        )
        self.moveToButton.place(x=20, y=140)

        self.deleteButton = tk.Button(
            self.middleRightFrame,
            text="DELETE",
            font=('Arial', '11'),
            width=18,
            command=self.delete_task_from_database,
            background='#970000',
            foreground='#FFFFFF'
        )
        self.deleteButton.place(x=20, y=180)
    
    def build_bottom_left_frame(self):
        self.bottomLeftFrame = tk.Frame(
            None,
            width=320,
            height=150,
            background="#2F3030"
        )
        self.bottomLeftFrame.place(x=10, y=400)

        self.remarkListboxLabel = tk.Label(
            self.bottomLeftFrame,
            text="Remarks for today:",
            font=("Open Sans", "12", "bold"),
            background="#2F3030",
            foreground="#000000"
        )
        self.remarkListboxLabel.place(x=10, y=6)

        self.remarkListbox = tk.Listbox(
            self.bottomLeftFrame,
            width=49,
            height=6,
            background="#303030"
        )
        self.remarkListbox.place(x=10, y=35)
    
    def build_very_bottom_frame1(self):
        self.veryBottomFrame1 = tk.Frame(
            None,
            width=230,
            height=35,
            background="#2F3030"
        )
        self.veryBottomFrame1.place(x=10, y=565)

        self.catchItButton = tk.Button(
            self.veryBottomFrame1,
            text="CATCH THE IDEA",
            font=('Arial', '8', 'bold'),
            width=14,
            command=self.catch_idea,
            background='#4F0082',
            foreground='#FFFFFF'
        )
        self.catchItButton.place(x=10, y=5)

        self.adhocTaskButton = tk.Button(
            self.veryBottomFrame1,
            text="ADHOC TASK",
            font=('Arial', '8', 'bold'),
            width=13,
            command=self.adhoc_task,
            background='#A94102',
            foreground='#FFFFFF'
        )
        self.adhocTaskButton.place(x=125, y=5)
    
    def build_very_bottom_frame2(self):
        self.veryBottomFrame2 = tk.Frame(
            None,
            width=110,
            height=50,
            background="#2F3030"
        )
        self.veryBottomFrame2.place(x=240, y=555)

        self.newTaskButton = tk.Button(
            self.veryBottomFrame2,
            text="NEW TASK",
            font=('Arial', '9', 'bold'),
            width=13,
            height=2,
            command=self.new_task,
            background='#004C01',
            foreground='#FFFFFF'
        )
        self.newTaskButton.place(x=5, y=2)
      
    def build_very_bottom_frame3(self):  
        self.veryBottomFrame3 = tk.Frame(
            None,
            width=220,
            height=35,
            background="#2F3030"
        )
        self.veryBottomFrame3.place(x=347, y=565)

        self.addRemarkButton = tk.Button(
            self.veryBottomFrame3,
            text=" ADD REMARK",
            font=('Arial', '8', 'bold'),
            width=13,
            command=self.add_remark,
            background='#9E019A',
            foreground='#FFFFFF'
        )
        self.addRemarkButton.place(x=8, y=5)

        self.addEventButton = tk.Button(
            self.veryBottomFrame3,
            text=" ADD EVENT",
            font=('Arial', '8', 'bold'),
            width=13,
            command=self.add_event,
            background='#A8A803',
            foreground='#FFFFFF'
        )
        self.addEventButton.place(x=116, y=5)
    
        
        