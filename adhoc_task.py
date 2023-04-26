import tkinter as tk
from tkinter import messagebox
import datetime
import sqlite3

current_date = datetime.datetime.now()
date_string = current_date.strftime("%d/%m/%Y")

def adhoc_task():
    adhoc_task_win = tk.Tk()
    adhoc_task_win.geometry ("600x200")
    adhoc_task_win.title("Adhoc Task")
    adhoc_task_win.resizable(0,0)
    adhoc_task_win.configure(bg = "#212121")

    def save_into_database():   
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        try:
            cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT, keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT, delegate_to TEXT, cooperate_with TEXT)')

            task_ID = None
            task_or_action = task_description_row.get()
            keywords = keywords_row.get()
            expected_result = expected_result_row.get()
            date = date_string
            deadline = None
            delegate_to = None
            cooperate_with = None

            query = "INSERT INTO tasks (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            values = (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with)
            cursor.execute(query, values)

            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Success", "Task successfully saved!")
            adhoc_task_win.destroy()

        except Exception as e:
            messagebox.showerror("Error", "OOPS! " + str(e))

    def exit_adhoc_task():
        if len(task_description_row.get()) != 0:
            answer = messagebox.askyesno("Close Adhoc Task", "If you close the window, the changes will be lost.\nClose Adhoc Task?")
            if answer:
                adhoc_task_win.destroy()
            else:
                pass
        elif len(keywords_row.get()) != 0:
            answer = messagebox.askyesno("Close Adhoc Task", "If you close the window, the changes will be lost.\nClose Adhoc Task?")
            if answer:
                adhoc_task_win.destroy()
            else:
                pass
        elif len(expected_result_row.get()) != 0:
            answer = messagebox.askyesno("Close Adhoc Task", "If you close the window, the changes will be lost.\nClose Adhoc Task?")
            if answer:
                adhoc_task_win.destroy()
            else:
                pass
        else:
            adhoc_task_win.destroy()

    header_label = tk.Label(
        adhoc_task_win,
        text = "ADHOC TASK",
        font = ('Montserrat', '15'),
        background = "#212121",
        foreground = "#FFFFFF"
    )
    header_label.place(x = 230, y = 5)

    top_frame = tk.Frame(
        adhoc_task_win,
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

    date_label = tk.Label(
        adhoc_task_win,
        text = date_string,
        font = ('Montserrat', '15'),
        background = "#212121",
        foreground = "#FFFFFF"
    )
    date_label.place(x = 15, y = 160)

    save_button = tk.Button(
        adhoc_task_win,
        text = "SAVE",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = save_into_database,
        background = '#A94102',
        foreground = '#FFFFFF'
    )
    save_button.place(x = 480, y = 160)

    exit_button = tk.Button(
        adhoc_task_win,
        text = "EXIT",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = exit_adhoc_task,
        background = '#970000',
        foreground = '#FFFFFF'
    )
    exit_button.place(x = 370, y = 160)

    adhoc_task_win.protocol("WM_DELETE_WINDOW", exit_adhoc_task)

