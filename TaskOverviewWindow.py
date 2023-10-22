import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar


class TaskOverviewWindow(tk.Toplevel):
    chosen_date = None
    chosen_deadline = None
    sorted_dates = []
    
    def __init__(self, master=None, dbManager=None):
        super().__init__()
        
        self.geometry("600x400")
        self.title("New Task")
        self.resizable(0, 0)
        self.configure(bg="#212121")
        self.dbManager = dbManager

    def show(self):
        self.createWindow()
        
    def tasks_list():
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()

        tasks_list_win = tk.Tk()
        tasks_list_win.geometry('1080x360')
        tasks_list_win.title('Time Management System 1.1.: TASKS DATABASE')
        tasks_list_win.option_add('*Dialog.msg.title.bg', '#000000')
        tasks_list_win.configure(bg = "#9C9C9C")
        tasks_list_win.resizable(0,0)

        style = ttk.Style(tasks_list_win)
        style.theme_use("clam")
        style.configure("Treeview", background = "#D3D3D3", fieldbackground = "#D3D3D3", foreground = "#000000")

        treeview = ttk.Treeview(
            tasks_list_win, columns=('Task ID', 'Task', 'Keywords', 'Expected Result', 'Date', 'Deadline', 'Delegated to', 'Cooperating with'))

        treeview.heading('#0', text='ID')
        treeview.column('#0', width=0, stretch = False)
        treeview.heading('Task ID', text='Task ID')
        treeview.column('Task ID', width=100)
        treeview.heading('Task', text='Task')
        treeview.column('Task', width=200)
        treeview.heading('Keywords', text='Keywords')
        treeview.column('Keywords', width=100)
        treeview.heading('Expected Result', text='Expected Result')
        treeview.column('Expected Result', width=200)
        treeview.heading('Date', text='Date')
        treeview.column('Date', width=100)
        treeview.heading('Deadline', text='Deadline')
        treeview.column('Deadline', width=100)
        treeview.heading('Delegated to', text='Delegated to')
        treeview.column('Delegated to', width=120)
        treeview.heading('Cooperating with', text='Cooperating with')
        treeview.column('Cooperating with', width=120)

        cursor.execute('SELECT * FROM tasks')
        for row in cursor.fetchall():
            treeview.insert('', 'end', text=row[0], values=row[1:])

        treeview.place (x = 15, y = 55)
    
    def createWindow(self):
        header_label = tk.Label(
                see_task_win,
                text = "TASK VIEW",
                font = ('Montserrat', '15'),
                background = "#212121",
                foreground = "#FFFFFF"
            )
        header_label.place(x = 250, y = 5)
        
        self.cal = Calendar(
            self,
            selectmode='day',
            date_pattern=('dd/mm/yyyy'),
            background="black"
        )
        self.cal.place(x=330, y=160)
        
        top_frame = tk.Frame(
            see_task_win,
            width = 570,
            height = 100,
            background = "#2F3030"
        )
        top_frame.place(x = 15, y = 40)

        task_description_label = tk.Label(
            top_frame,
            text = "TASK OR ACTION",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        task_description_label.place(x = 10, y = 5)

        task_description_row = tk.Entry(
            top_frame,
            font = ("Open Sans", "10", "bold"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        task_description_row.place(x = 150, y = 5)

        keywords_label = tk.Label(
            top_frame,
            text = "Keywords",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        keywords_label.place(x = 10, y = 35)

        keywords_row = tk.Entry(
            top_frame,
            font = ("Open Sans", "10"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        keywords_row.place(x = 150, y = 35)

        expected_result_label = tk.Label(
            top_frame,
            text = "Expected Result",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        expected_result_label.place(x = 10, y = 65)

        expected_result_row = tk.Entry(
            top_frame,
            font = ("Open Sans", "10"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        expected_result_row.place(x = 150, y = 65)

        middle_frame = tk.Frame(
            see_task_win,
            width = 305,
            height = 80,
            background = "#2F3030"
        )
        middle_frame.place(x = 15, y = 160)

        date_button = tk.Button(
            middle_frame,
            text = "Choose Date",
            font = ('Arial', '10', 'bold'),
            width = 16,
            command = choose_date,
            background = '#464646',
            foreground = '#FFFFFF'
        )
        date_button.place(x = 10, y = 5)

        deadline_button = tk.Button(
            middle_frame,
            text = "Choose Deadline",
            font = ('Arial', '10', 'bold'),
            width = 16,
            command = choose_deadline,
            background = '#464646',
            foreground = '#FFFFFF'
        )
        deadline_button.place(x = 10, y = 45)


        edit_button = tk.Button(
            see_task_win,
            text = "EDIT",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = edit_task,
            background = '#004C01',
            foreground = '#FFFFFF'
        )
        edit_button.place(x = 480, y = 360)

        exit_button = tk.Button(
            see_task_win,
            text = "EXIT",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = exit_see_task,
            background = '#970000',
            foreground = '#FFFFFF'
        )
        exit_button.place(x = 370, y = 360)

        bottom_frame = tk.Frame(
            see_task_win,
            width = 305,
            height = 80,
            background = "#2F3030"
        )
        bottom_frame.place(x = 15, y = 265)

        delegate_to_label = tk.Label(
            bottom_frame,
            text = "Delegate to",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        delegate_to_label.place(x = 10, y = 5)

        delegate_to_row = tk.Entry(
            bottom_frame,
            font = ("Open Sans", "10"),
            width = 20,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        delegate_to_row.place(x = 150, y = 5)

        cooperate_with_label = tk.Label(
            bottom_frame,
            text = "Cooperate with",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        cooperate_with_label.place(x = 10, y = 35)

        cooperate_with_row = tk.Entry(
            bottom_frame,
            font = ("Open Sans", "10"),
            width = 20,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        cooperate_with_row.place(x = 150, y = 35)

#        see_task_win.protocol("WM_DELETE_WINDOW", exit_see_task)
#        insert_values()

        header_label = tk.Label(
            tasks_list_win,
            text = "MY TASKS",
            font = ('Montserrat', '15', "bold"),
            background = "#9C9C9C",
            foreground = "#000000"
        )
        header_label.place(x = 450, y = 15)

        top_frame = tk.Frame(
            tasks_list_win,
            width = 1045,
            height = 55,
            background = "#737374"
        )
        top_frame.place(x = 15, y = 290)

        find_task_label = tk.Label(
            top_frame,
            text = "Find Task:",
            font = ("Open Sans", "12", "bold"),
            background = "#737374",
            foreground = "#000000"       
        )
        find_task_label.place(x = 5, y = 12)

        find_task_row = tk.Entry(
            top_frame,
            font = ("Open Sans", "10", "bold"),
            width = 30,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        find_task_row.place(x = 100, y = 14)

        find_task_button = tk.Button(
            top_frame,
            text = "FIND TASK",
            font = ('Arial', '9', 'bold'),
            width = 13,
            command = find_task,
            background = '#4F0082',
            foreground = '#FFFFFF'
        )
        find_task_button.place(x = 320, y = 12)

        select_task_button = tk.Button(
            top_frame,
            text = "SELECT TASK",
            font = ('Arial', '9', 'bold'),
            width = 13,
            command = see_task_in_tasks_list,
            background = '#00248B',
            foreground = '#FFFFFF'
        )
        select_task_button.place(x = 700, y = 12)

        delete_task_button = tk.Button(
            top_frame,
            text = "DELETE TASK",
            font = ('Arial', '9', 'bold'),
            width = 13,
            command = None,
            background = '#970000',
            foreground = '#FFFFFF'
        )
        delete_task_button.place(x = 810, y = 12)

        done_button = tk.Button(
            top_frame,
            text = "DONE",
            font = ('Arial', '9', 'bold'),
            width = 13,
            command = tasks_list_win.destroy,
            background = '#004C01',
            foreground = '#FFFFFF'
        )
        done_button.place(x = 920, y = 12)