import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
import sqlite3

chosen_date = None
chosen_deadline = None

def new_task():
    new_task_win = tk.Tk()
    new_task_win.geometry ("600x400")
    new_task_win.title("New Task")
    new_task_win.resizable(0,0)
    new_task_win.configure(bg = "#212121")
    
    cal = Calendar (new_task_win, selectmode = 'day', date_pattern = ('dd/mm/yyyy'), background = "black")
    cal.place(x= 330, y= 160)

    def choose_date():
        global chosen_date
        chosen_date = cal.get_date()

        chosen_date_label = tk.Label(
            middle_frame,
            text = chosen_date,
            font = ('Montserrat', '12'),
            background = "#2F3030",
            foreground = "#FFFFFF"
        )
        chosen_date_label.place(x = 180, y = 5)
    
    def choose_deadline():
        global chosen_deadline
        chosen_deadline = cal.get_date()

        chosen_deadline_label = tk.Label(
            middle_frame,
            text = chosen_deadline,
            font = ('Montserrat', '12', 'bold'),
            background = "#970000",
            foreground = "#FFFFFF"
        )
        chosen_deadline_label.place(x = 180, y = 45)
    
    def exit_new_task():
        if len(task_description_row.get()) != 0:
            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
            if answer:
                new_task_win.destroy()
            else:
                pass
        elif len(keywords_row.get()) != 0:
            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
            if answer:
                new_task_win.destroy()
            else:
                pass
        elif len(expected_result_row.get()) != 0:
            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
            if answer:
                new_task_win.destroy()
            else:
                pass
        else:
            new_task_win.destroy()

    def save_into_database():   
        global chosen_date
        global chosen_deadline

        tasks_conn = sqlite3.connect('tasks.db')
        tasks_cursor = tasks_conn.cursor()
        delegated_conn = sqlite3.connect('delegated_tasks.db')
        delegated_cursor = delegated_conn.cursor()

        if chosen_date or chosen_deadline != None:
            if chosen_date == None and chosen_deadline != None:
                chosen_date = chosen_deadline
            else:
                pass

            try:
                if len(delegate_to_row.get()) == 0:
                    tasks_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT, keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT, delegate_to TEXT, cooperate_with TEXT)')

                    task_ID = None
                    task_or_action = task_description_row.get()
                    keywords = keywords_row.get()
                    expected_result = expected_result_row.get()
                    date = chosen_date
                    deadline = chosen_deadline
                    delegate_to = delegate_to_row.get()
                    cooperate_with = cooperate_with_row.get()

                    query = "INSERT INTO tasks (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                    values = (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with)
                    tasks_cursor.execute(query, values)

                    tasks_conn.commit()
                    tasks_cursor.close()
                    tasks_conn.close()
                    messagebox.showinfo("Success", "Task successfully saved!")
                else:
                    delegated_cursor.execute('CREATE TABLE IF NOT EXISTS delegated_tasks (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT, keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT, delegate_to TEXT, cooperate_with TEXT)')

                    task_ID = None
                    task_or_action = task_description_row.get()
                    keywords = keywords_row.get()
                    expected_result = expected_result_row.get()
                    date = chosen_date
                    deadline = chosen_deadline
                    delegate_to = delegate_to_row.get()
                    cooperate_with = cooperate_with_row.get()

                    query = "INSERT INTO delegated_tasks (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                    values = (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with)
                    delegated_cursor.execute(query, values)                    

                    delegated_conn.commit()
                    delegated_cursor.close()
                    delegated_conn.close()
                    messagebox.showinfo("Success", "Task successfully saved into DELEGATED TASKS!")
                new_task_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", "OOPS! " + str(e))
        else:
            messagebox.showerror("ERROR", "Date is not selected. Select date for the task.")

    header_label = tk.Label(
        new_task_win,
        text = "NEW TASK",
        font = ('Montserrat', '15'),
        background = "#212121",
        foreground = "#FFFFFF"
    )
    header_label.place(x = 250, y = 5)

    top_frame = tk.Frame(
        new_task_win,
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
        new_task_win,
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


    save_button = tk.Button(
        new_task_win,
        text = "SAVE",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = save_into_database,
        background = '#004C01',
        foreground = '#FFFFFF'
    )
    save_button.place(x = 480, y = 360)

    exit_button = tk.Button(
        new_task_win,
        text = "EXIT",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = exit_new_task,
        background = '#970000',
        foreground = '#FFFFFF'
    )
    exit_button.place(x = 370, y = 360)

    bottom_frame = tk.Frame(
        new_task_win,
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

    new_task_win.protocol("WM_DELETE_WINDOW", exit_new_task)




