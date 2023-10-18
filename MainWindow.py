import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import time
import requests
import sys
import sqlite3
import datetime
from tkinter import messagebox


from add_event import add_event
from add_remark import add_remark
from adhoc_task import adhoc_task
from catch_idea import catch_idea
from delegated_tasks_list_database import delegated_tasks_list
from move_to import move_task_to
from new_task import new_task
from tasks_list_database import tasks_list
# Created on : 17. 10. 2023, 17:32:05
# Author     : prohi


class MainWindow(tk.TK):

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
    
    
    current_date = datetime.datetime.now()
    date_string = current_date.strftime("%d/%m/%Y")
    result_tasks = []
    tasks_done = []
    chosen_date = None
    chosen_deadline = None

    def __init__(self, master=None, dbManager=None):
        self.dlg = tk.Tk()
        self.geometry("800x600")
        self.title("Time Management System 1.1: Main Screen")
        self.resizable(0, 0)
        self.configure(bg="#212121")
        
        self.protocol("WM_DELETE_WINDOW", self.exit_window)
        
        self.createWindow()
        
        self.cal = Calendar(
            self.dlg,
            selectmode='day',
            date_pattern=('dd/mm/yyyy'),
            background="black"
        )
        self.cal.place(x=330, y=160)

    def insert_data_to_today_tasks():
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
            command=insert_data_to_today_tasks,
            background='#00BFC5',
            foreground='#000000'
        )
        self.refreshButton.place(x=140, y=5)

        self.taskListButton = tk.Button(
            self.rightFrame,
            text="MY TASKS",
            font=('Arial', '11'),
            width=21,
            command=tasks_list,
            background='#0003C8',
            foreground='#FFFFFF'
        )
        self.taskListButton.place(x=16, y=160)

        self.delegatedTaskListButton = tk.Button(
            self.rightFrame,
            text="DELEGATED TASKS",
            font=('Arial', '11'),
            width=21,
            command=delegated_tasks_list,
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

        self.topLeftFrame = tk.Frame(
            None,
            width=270,
            height=120,
            background="#2F3030"
        )
        self.topLeftFrame.place(x=10, y=10)

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

        self.topRightFrame = tk.Frame(
            None,
            width=270,
            height=120,
            background="#2F3030"
        )
        self.topRightFrame.place(x=290, y=10)

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

        self.signLabel = tk.Label(
            self.rightFrame,
            text='by VK',
            font=("Edwardian Script ITC", "25"),
            background='#2F3030',
            foreground='#FFFFFF'
        )
        self.signLabel.place(x=125, y=550)

        self.middleLeftFrame = tk.Frame(
            None,
            width=320,
            height=235,
            background="#2F3030"
        )
        self.middleLeftFrame.place(x=10, y=155)

        self.middleRightFrame = tk.Frame(
            None,
            width=202,
            height=230,
            background="#2F3030"
        )
        self.middleRightFrame.place(x=350, y=157)

        done_button = tk.Button(
            self.middleRightFrame,
            text="DONE",
            font=('Arial', '11'),
            width=18,
            command=task_done,
            background='#004C01',
            foreground='#FFFFFF'
        )
        done_button.place(x=20, y=20)

        see_task_button = tk.Button(
            self.middleRightFrame,
            text="SEE TASK",
            font=('Arial', '11'),
            width=18,
            command=see_task,
            background='#027853',
            foreground='#FFFFFF'
        )
        see_task_button.place(x=20, y=60)

        do_it_tomorrow_button = tk.Button(
            self.middleRightFrame,
            text="DO IT TOMORROW",
            font=('Arial', '11'),
            width=18,
            command=do_task_tomorrow,
            background='#027853',
            foreground='#FFFFFF'
        )
        do_it_tomorrow_button.place(x=20, y=100)

        move_to_button = tk.Button(
            self.middleRightFrame,
            text="MOVE TO",
            font=('Arial', '11'),
            width=18,
            command=move_task_to,
            background='#027853',
            foreground='#FFFFFF'
        )
        move_to_button.place(x=20, y=140)

        delete_button = tk.Button(
            self.middleRightFrame,
            text="DELETE",
            font=('Arial', '11'),
            width=18,
            command=delete_task_from_database,
            background='#970000',
            foreground='#FFFFFF'
        )
        delete_button.place(x=20, y=180)

        remark_field_label = tk.Label(
            self.middleLeftFrame,
            text="Tasks for today:",
            font=("Open Sans", "12", "bold"),
            background="#2F3030",
            foreground="#000000"
        )
        remark_field_label.place(x=10, y=6)

        today_tasks_list = tk.Listbox(
            self.middleLeftFrame,
            width=42,
            height=11,
            selectforeground="#FFFFFF",
            selectbackground="#181818",
            font=("Arial", "10", "bold"),
            foreground="#C2C2C2",
            background="#303030"
        )
        today_tasks_list.place(x=11, y=38)

        bottom_frame_left = tk.Frame(
            None,
            width=320,
            height=150,
            background="#2F3030"
        )
        bottom_frame_left.place(x=10, y=400)

        remark_listbox_label = tk.Label(
            bottom_frame_left,
            text="Remarks for today:",
            font=("Open Sans", "12", "bold"),
            background="#2F3030",
            foreground="#000000"
        )
        remark_listbox_label.place(x=10, y=6)

        remark_listbox = tk.Listbox(
            bottom_frame_left,
            width=49,
            height=6,
            background="#303030"
        )
        remark_listbox.place(x=10, y=35)

        very_bottom_frame1 = tk.Frame(
            None,
            width=230,
            height=35,
            background="#2F3030"
        )
        very_bottom_frame1.place(x=10, y=565)

        catch_it_button = tk.Button(
            very_bottom_frame1,
            text="CATCH THE IDEA",
            font=('Arial', '8', 'bold'),
            width=14,
            command=catch_idea,
            background='#4F0082',
            foreground='#FFFFFF'
        )
        catch_it_button.place(x=10, y=5)

        adhoc_task_button = tk.Button(
            very_bottom_frame1,
            text="ADHOC TASK",
            font=('Arial', '8', 'bold'),
            width=13,
            command=adhoc_task,
            background='#A94102',
            foreground='#FFFFFF'
        )
        adhoc_task_button.place(x=125, y=5)

        very_bottom_frame2 = tk.Frame(
            None,
            width=110,
            height=50,
            background="#2F3030"
        )
        very_bottom_frame2.place(x=240, y=555)

        new_task_button = tk.Button(
            very_bottom_frame2,
            text="NEW TASK",
            font=('Arial', '9', 'bold'),
            width=13,
            height=2,
            command=new_task,
            background='#004C01',
            foreground='#FFFFFF'
        )
        new_task_button.place(x=5, y=2)

        very_bottom_frame3 = tk.Frame(
            None,
            width=220,
            height=35,
            background="#2F3030"
        )
        very_bottom_frame3.place(x=347, y=565)

        add_remark_button = tk.Button(
            very_bottom_frame3,
            text=" ADD REMARK",
            font=('Arial', '8', 'bold'),
            width=13,
            command=add_remark,
            background='#9E019A',
            foreground='#FFFFFF'
        )
        add_remark_button.place(x=8, y=5)

        add_event_button = tk.Button(
            very_bottom_frame3,
            text=" ADD EVENT",
            font=('Arial', '8', 'bold'),
            width=13,
            command=add_event,
            background='#A8A803',
            foreground='#FFFFFF'
        )
        add_event_button.place(x=116, y=5)

        