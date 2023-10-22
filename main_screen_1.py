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


current_date = datetime.datetime.now()
date_string = current_date.strftime("%d/%m/%Y")
result_tasks = []
tasks_done = []
chosen_date = None
chosen_deadline = None


def insert_data_to_today_tasks():
    global result_tasks
    today_tasks_list.delete(0, 'end')
    if len(result_tasks) == 0:
        number_of_tasks_label = tk.Label(
            middle_frame_left,
            text=f"{str(len(result_tasks))}     ",
            font=("Arial", "12", "bold"),
            background="#2F3030",
            foreground="#78CE04"
        )
        number_of_tasks_label.place(x=140, y=6)
    try:
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()

        query="SELECT task_or_action FROM tasks WHERE date = ?"
        cursor.execute(query, (date_string,))
        data = cursor.fetchall()
        result_tasks = [(str(row[0]).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "")
                        .replace(",", "").replace("'", "")) for row in data]
        if len(result_tasks) != 0:
            number_of_tasks_label = tk.Label(
                middle_frame_left,
                text=f"{str(len(result_tasks))}     ",
                font=("Arial", "12", "bold"),
                background="#2F3030",
                foreground="#000000"
            )
            number_of_tasks_label.place(x=140, y=6)
            for task in result_tasks:
                corrected_result = f"  {task}"
                today_tasks_list.insert("end", corrected_result)
        else:
            number_of_tasks_label = tk.Label(
                middle_frame_left,
                text=f"{str(len(result_tasks))}     ",
                font=("Arial", "12", "bold"),
                background="#2F3030",
                foreground="#78CE04"
            )
            number_of_tasks_label.place(x=140, y=6)
            corrected_result = "  No new tasks. Enjoy your day!"
            today_tasks_list.insert("end", corrected_result)

        cursor.close()
        conn.close()
    except Exception as e:
        number_of_tasks_label = tk.Label(
            middle_frame_left,
            text="0     ",
            font=("Arial", "12", "bold"),
            background="#2F3030",
            foreground="#78CE04"
        )
        number_of_tasks_label.place(x=140, y=6)
        corrected_result = "  No tasks for today"
        today_tasks_list.insert("end", corrected_result)
    progress_bar_of_day()


def task_done():
    task_to_be_done = today_tasks_list.get((today_tasks_list.curselection()))
    corrected_done = task_to_be_done[2:]

    done_db = sqlite3.connect('tasks_done.db')
    done_cursor = done_db.cursor()
    done_cursor.execute('CREATE TABLE IF NOT EXISTS tasks_done (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT, keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT, delegate_to TEXT, cooperate_with TEXT)')

    tasks_db = sqlite3.connect('tasks.db')
    tasks_cursor = tasks_db.cursor()
    tasks_cursor.execute("SELECT id FROM tasks WHERE REPLACE(REPLACE(REPLACE(task_or_action, '{', ''), '}', ''), '[', '') = ?", (corrected_done,))
    row = tasks_cursor.fetchone()
    try:
        if row is None:
            messagebox.showerror(
                "ERROR", "OOPS! No matching task found in database."
            )
            return
        else:
            row_id = row[0]
            tasks_cursor.execute("SELECT * FROM tasks WHERE id=?", (row_id,))
            row_to_copy=tasks_cursor.fetchone()
            done_cursor.execute(
                "INSERT INTO tasks_done VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                row_to_copy[1:]
            )
            done_db.commit()
            tasks_cursor.execute("DELETE FROM tasks WHERE id = ?", (row_id,))
            tasks_db.commit()
            today_tasks_list.delete(0, 'end')
            insert_data_to_today_tasks()
            progress_bar_of_day()
            messagebox.showinfo(
                "Congratulations", f"Task {corrected_done} has been DONE!"
            )
    except Exception as e:
        messagebox.showerror("Error", "OOPS! " + str(e))

    done_cursor.close()
    done_db.close()
    tasks_cursor.close()
    tasks_db.close()


def see_task():
    global chosen_date
    global chosen_deadline

    selection = today_tasks_list.curselection()
    if selection:
        pass
    else:
        messagebox.showerror(
            "Error", "No task selected. Please select a task to edit."
        )
        return

    see_task_win = tk.Tk()
    see_task_win.geometry("600x400")
    see_task_win.title("New Task")
    see_task_win.resizable(0, 0)
    see_task_win.configure(bg="#212121")

    cal = Calendar(
        see_task_win,
        selectmode='day',
        date_pattern=('dd/mm/yyyy'),
        background="black"
    )
    cal.place(x=330, y=160)

    def choose_date():
        global chosen_date

        chosen_date = cal.get_date()
        chosen_date_label = tk.Label(
            middle_frame,
            text=chosen_date,
            font=('Montserrat', '12'),
            background="#2F3030",
            foreground="#FFFFFF"
        )
        chosen_date_label.place(x=180, y=5)

    def choose_deadline():
        global chosen_deadline

        chosen_deadline = cal.get_date()
        chosen_deadline_label = tk.Label(
            middle_frame,
            text=chosen_deadline,
            font=('Montserrat', '12', 'bold'),
            background="#970000",
            foreground="#FFFFFF"
        )
        chosen_deadline_label.place(x=180, y=45)

    def exit_see_task():
        if len(task_description_row.get()) != 0:
            answer = messagebox.askyesno(
                "Close", "All changes will be lost. Continue?"
            )
            if answer:
                see_task_win.destroy()
            else:
                pass
        elif len(keywords_row.get()) != 0:
            answer = messagebox.askyesno(
                "Close", "All changes will be lost. Continue?"
            )
            if answer:
                see_task_win.destroy()
            else:
                pass
        elif len(expected_result_row.get()) != 0:
            answer = messagebox.askyesno(
                "Close", "All changes will be lost. Continue?"
            )
            if answer:
                see_task_win.destroy()
            else:
                pass
        else:
            see_task_win.destroy()

    def edit_task():
        global chosen_date
        global chosen_deadline

        selection = today_tasks_list.curselection()
        if selection:
            task_to_be_edited = today_tasks_list.get(selection)
            corrected_edited = task_to_be_edited[2:]
        else:
            messagebox.showerror("Error", "No task selected. Please select a task to edit.\nBe sure that task you want to edit is properly selected on Main screen.")

        if chosen_date is None and chosen_deadline is not None:
            chosen_date = chosen_deadline
        elif chosen_date is not None and chosen_deadline is not None:
            chosen_date = min(chosen_date, chosen_deadline)
        elif chosen_date is not None and chosen_deadline is None:
            chosen_deadline = chosen_date

        answer = messagebox.askyesno("Edit Task", "Do you wish to edit task?")
        if answer:
            try:
                if len(delegate_to_row.get()) == 0:
                    conn = sqlite3.connect('tasks.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT id FROM tasks WHERE REPLACE(REPLACE(REPLACE(task_or_action, '{', ''), '}', ''), '[', '') = ?", (corrected_edited,))
                    row = cursor.fetchone()
                    row_id = row[0]
                    cursor.execute("DELETE FROM tasks WHERE id = ?", (row_id,))
                    conn.commit()
                    today_tasks_list.delete(0, 'end')

                    task_ID = None
                    task_or_action = task_description_row.get()
                    keywords = keywords_row.get()
                    expected_result = expected_result_row.get()
                    date = chosen_date
                    deadline = chosen_deadline
                    delegate_to = delegate_to_row.get()
                    cooperate_with = cooperate_with_row.get()

                    query="INSERT INTO tasks (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                    values = (
                        task_ID, task_or_action, keywords,
                        expected_result, date, deadline,
                        delegate_to, cooperate_with
                    )
                    cursor.execute(query, values)

                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Success", "Task successfully edited!")
                else:
                    tasks_conn = sqlite3.connect('tasks.db')
                    tasks_cursor = tasks_conn.cursor()
                    delegated_conn = sqlite3.connect('delegated_tasks.db')
                    delegated_cursor = delegated_conn.cursor()

                    tasks_cursor.execute("SELECT id FROM tasks WHERE REPLACE(REPLACE(REPLACE(task_or_action, '{', ''), '}', ''), '[', '') = ?", (corrected_edited,))
                    row = tasks_cursor.fetchone()
                    row_id = row[0]
                    tasks_cursor.execute(
                        "DELETE FROM tasks WHERE id = ?", (row_id,)
                    )
                    tasks_conn.commit()
                    today_tasks_list.delete(0, 'end')
                    tasks_conn.commit()
                    tasks_cursor.close()
                    tasks_conn.close()

                    delegated_cursor.execute('CREATE TABLE IF NOT EXISTS delegated_tasks (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT, keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT, delegate_to TEXT, cooperate_with TEXT)')
                    task_ID = None
                    task_or_action = task_description_row.get()
                    keywords = keywords_row.get()
                    expected_result = expected_result_row.get()
                    date = chosen_date
                    deadline = chosen_deadline
                    delegate_to = delegate_to_row.get()
                    cooperate_with = cooperate_with_row.get()
                    query="INSERT INTO delegated_tasks (task_ID, task_or_action, keywords, expected_result, date, deadline, delegate_to, cooperate_with) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                    values = (
                        task_ID, task_or_action,
                        keywords, expected_result, date,
                        deadline, delegate_to, cooperate_with
                    )
                    delegated_cursor.execute(query, values)
                    delegated_conn.commit()
                    delegated_cursor.close()
                    delegated_conn.close()
                    messagebox.showinfo(
                        "Success",
                        "Task successfully saved into DELEGATED TASKS!"
                    )
                insert_data_to_today_tasks()
                progress_bar_of_day()
                see_task_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", "OOPS! " + str(e))
                see_task_win.destroy()
        else:
            pass

    def insert_values():
        global chosen_date
        global chosen_deadline

        task_to_be_viewed = today_tasks_list.get(
            (today_tasks_list.curselection())
        )
        corrected_viewed = task_to_be_viewed[2:]

        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM tasks WHERE REPLACE(REPLACE(REPLACE(task_or_action,'{', ''), '}', ''), '[', '') = ?", (corrected_viewed,))
        row = cursor.fetchone()
        row_id = row[0]

        cursor.execute(
            "SELECT task_or_action FROM tasks WHERE id=?",
            (row_id,)
        )
        result_task_or_action = cursor.fetchone()[0]
        task_description_row.insert(0, result_task_or_action)

        cursor.execute("SELECT keywords FROM tasks WHERE id=?", (row_id,))
        result_keywords = cursor.fetchone()[0]
        keywords_row.insert(0, result_keywords)

        cursor.execute(
            "SELECT expected_result FROM tasks WHERE id=?",
            (row_id,)
        )
        result_expected_result = cursor.fetchone()[0]
        expected_result_row.insert(0, result_expected_result)

        cursor.execute("SELECT date FROM tasks WHERE id=?", (row_id,))
        chosen_date = cursor.fetchone()[0]
        result_date_label = tk.Label(
            middle_frame,
            text=chosen_date,
            font=('Montserrat', '12'),
            background="#2F3030",
            foreground="#FFFFFF"
        )
        result_date_label.place(x=180, y=5)

        cursor.execute("SELECT deadline FROM tasks WHERE id=?", (row_id,))
        chosen_deadline = cursor.fetchone()[0]
        result_deadline_label = tk.Label(
            middle_frame,
            text=chosen_deadline,
            font=('Montserrat', '12', 'bold'),
            background="#970000",
            foreground="#FFFFFF"
        )
        result_deadline_label.place(x=180, y=45)

        cursor.execute("SELECT delegate_to FROM tasks WHERE id=?", (row_id,))
        result_delegate_to = cursor.fetchone()[0]
        delegate_to_row.insert(0, result_delegate_to)

        cursor.execute(
            "SELECT cooperate_with FROM tasks WHERE id=?", (row_id,)
        )
        result_cooperate_with = cursor.fetchone()[0]
        cooperate_with_row.insert(0, result_cooperate_with)

        cursor.close()
        conn.close()

    header_label = tk.Label(
        see_task_win,
        text="TASK VIEW",
        font=('Montserrat', '15'),
        background="#212121",
        foreground="#FFFFFF"
    )
    header_label.place(x=250, y=5)

    top_frame = tk.Frame(
        see_task_win,
        width=570,
        height=100,
        background="#2F3030"
    )
    top_frame.place(x=15, y=40)

    task_description_label = tk.Label(
        top_frame,
        text="TASK OR ACTION",
        font=("Open Sans", "10", "bold"),
        background="#2F3030",
        foreground="#000000"
    )
    task_description_label.place(x=10, y=5)

    task_description_row = tk.Entry(
        top_frame,
        font=("Open Sans", "10", "bold"),
        width=56,
        insertbackground="#FFFFFF",
        background="#000000",
        foreground="#FFFFFF"
    )
    task_description_row.place(x=150, y=5)

    keywords_label = tk.Label(
        top_frame,
        text="Keywords",
        font=("Open Sans", "10", "bold"),
        background="#2F3030",
        foreground="#000000"
    )
    keywords_label.place(x=10, y=35)

    keywords_row = tk.Entry(
        top_frame,
        font=("Open Sans", "10"),
        width=56,
        insertbackground="#FFFFFF",
        background="#000000",
        foreground="#FFFFFF"
    )
    keywords_row.place(x=150, y=35)

    expected_result_label = tk.Label(
        top_frame,
        text="Expected Result",
        font=("Open Sans", "10", "bold"),
        background="#2F3030",
        foreground="#000000"
    )
    expected_result_label.place(x=10, y=65)

    expected_result_row = tk.Entry(
        top_frame,
        font=("Open Sans", "10"),
        width=56,
        insertbackground="#FFFFFF",
        background="#000000",
        foreground="#FFFFFF"
    )
    expected_result_row.place(x=150, y=65)

    middle_frame = tk.Frame(
        see_task_win,
        width=305,
        height=80,
        background="#2F3030"
    )
    middle_frame.place(x=15, y=160)

    date_button = tk.Button(
        middle_frame,
        text="Choose Date",
        font=('Arial', '10', 'bold'),
        width=16,
        command=choose_date,
        background='#464646',
        foreground='#FFFFFF'
    )
    date_button.place(x=10, y=5)

    deadline_button = tk.Button(
        middle_frame,
        text="Choose Deadline",
        font=('Arial', '10', 'bold'),
        width=16,
        command=choose_deadline,
        background='#464646',
        foreground='#FFFFFF'
    )
    deadline_button.place(x=10, y=45)

    edit_button = tk.Button(
        see_task_win,
        text="EDIT",
        font=('Arial', '10', 'bold'),
        width=11,
        command=edit_task,
        background='#004C01',
        foreground='#FFFFFF'
    )
    edit_button.place(x=480, y=360)

    exit_button = tk.Button(
        see_task_win,
        text="EXIT",
        font=('Arial', '10', 'bold'),
        width=11,
        command=exit_see_task,
        background='#970000',
        foreground='#FFFFFF'
    )
    exit_button.place(x=370, y=360)

    bottom_frame = tk.Frame(
        see_task_win,
        width=305,
        height=80,
        background="#2F3030"
    )
    bottom_frame.place(x=15, y=265)

    delegate_to_label = tk.Label(
        bottom_frame,
        text="Delegate to",
        font=("Open Sans", "10", "bold"),
        background="#2F3030",
        foreground="#000000"
    )
    delegate_to_label.place(x=10, y=5)

    delegate_to_row = tk.Entry(
        bottom_frame,
        font=("Open Sans", "10"),
        width=20,
        insertbackground="#FFFFFF",
        background="#000000",
        foreground="#FFFFFF"
    )
    delegate_to_row.place(x=150, y=5)

    cooperate_with_label = tk.Label(
        bottom_frame,
        text="Cooperate with",
        font=("Open Sans", "10", "bold"),
        background="#2F3030",
        foreground="#000000"
    )
    cooperate_with_label.place(x=10, y=35)

    cooperate_with_row = tk.Entry(
        bottom_frame,
        font=("Open Sans", "10"),
        width=20,
        insertbackground="#FFFFFF",
        background="#000000",
        foreground="#FFFFFF"
    )
    cooperate_with_row.place(x=150, y=35)

    see_task_win.protocol("WM_DELETE_WINDOW", exit_see_task)
    insert_values()


def do_task_tomorrow():
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    tomorrow_date = tomorrow.strftime('%d/%m/%Y')
    selection = today_tasks_list.curselection()
    if selection:
        task_tomorrow = today_tasks_list.get(selection)
        corrected_tomorrow = task_tomorrow[2:]
    else:
        messagebox.showerror(
            "Error",
            "No task selected. Please select a task to edit."
        )

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tasks WHERE REPLACE(REPLACE(REPLACE(task_or_action, '{', ''), '}', ''), '[', '') = ?", (corrected_tomorrow,))
    row = cursor.fetchone()
    try:
        if row is None:
            messagebox.showerror(
                "ERROR",
                "OOPS! No matching task found in database."
            )
            return
        else:
            row_id = row[0]
            cursor.execute(
                "UPDATE tasks SET date=? WHERE id=?",
                (tomorrow_date, row_id)
            )
            conn.commit()
            messagebox.showinfo("Info", "Task moved to tomorrow.")
    finally:
        cursor.close()
        conn.close()
    progress_bar_of_day()
    insert_data_to_today_tasks()


def delete_task_from_database():
    global result_tasks
    task_to_be_deleted = today_tasks_list.get(
        (today_tasks_list.curselection())
    )
    corrected_delete = task_to_be_deleted[2:]
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tasks WHERE REPLACE(REPLACE(REPLACE(task_or_action, '{', ''), '}', ''), '[', '') = ?", (corrected_delete,))
    row = cursor.fetchone()
    try:
        if row is None:
            messagebox.showerror(
                "ERROR", "OOPS! No matching task found in database."
            )
            return
        else:
            answer = messagebox.askyesno(
                "Delete Task", "Do you want do delete task?"
            )
            if answer:
                row_id = row[0]
                cursor.execute("DELETE FROM tasks WHERE id = ?", (row_id,))
                conn.commit()
                today_tasks_list.delete(0, 'end')
                insert_data_to_today_tasks()
                messagebox.showinfo("Info", "Task successfully deleted.")
            else:
                pass
            cursor.close()
            conn.close()
    except Exception as e:
        messagebox.showerror("Error", "OOPS! " + str(e))


def progress_bar_of_day():
    try:
        done_conn = sqlite3.connect('tasks_done.db')
        done_cursor = done_conn.cursor()
        done_cursor.execute('CREATE TABLE IF NOT EXISTS tasks_done (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT, keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT, delegate_to TEXT, cooperate_with TEXT)')
        done_cursor.execute("SELECT COUNT(*) FROM tasks_done WHERE REPLACE(REPLACE(REPLACE(date, '{', ''), '}', ''), '[', '') = ?", (date_string,))
        number_tasks_done = done_cursor.fetchone()[0]
        done_cursor.close()
        done_conn.close()
        tasks_conn = sqlite3.connect('tasks.db')
        tasks_cursor = tasks_conn.cursor()
        tasks_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task_ID TEXT, task_or_action TEXT, keywords TEXT, expected_result TEXT, date TEXT, deadline TEXT, delegate_to TEXT, cooperate_with TEXT)')
        tasks_cursor.execute("SELECT COUNT(*) FROM tasks WHERE REPLACE(REPLACE(REPLACE(date, '{', ''), '}', ''), '[', '') = ?", (date_string,))
        number_tasks_to_fulfill = tasks_cursor.fetchone()[0]
        tasks_cursor.close()
        tasks_conn.close()

        total_number_tasks = number_tasks_done + number_tasks_to_fulfill
        if total_number_tasks != 0:
            task_value = 100 / total_number_tasks
            task_done_value = number_tasks_done * task_value
            value = 0 + task_done_value
        else:
            value = 0

        style_progressbar = ttk.Style()
        style_progressbar.theme_use("default")
        style_progressbar.configure(
            "green.Horizontal.TProgressbar",
            background='#0003C8'
        )
        today_progress_bar = ttk.Progressbar(
            top_header_frame_left,
            style="green.Horizontal.TProgressbar",
            orient="horizontal",
            length=249, mode="determinate"
        )
        today_progress_bar.place(x=0, y=80)
        today_progress_bar["value"] = value

        if total_number_tasks == 0:
            style_progressbar.configure(
                "green.Horizontal.TProgressbar",
                background='#970000',
                troughcolor='#20EE00'
            )
        elif 1 <= value <= 30:
            style_progressbar.configure(
                "green.Horizontal.TProgressbar",
                background='#970000',
                troughcolor='#666666'
            )
        elif 31 <= value <= 60:
            style_progressbar.configure(
                "green.Horizontal.TProgressbar",
                background='#F08C05',
                troughcolor='#666666'
            )
        elif 61 <= value <= 99:
            style_progressbar.configure(
                "green.Horizontal.TProgressbar",
                background='#BFEE00',
                troughcolor='#666666'
            )
        else:
            style_progressbar.configure(
                "green.Horizontal.TProgressbar",
                background='#20EE00',
                troughcolor='#666666'
            )

    except Exception as e:
        print(f"Progress bar error: {e}")
        value = 0
        style_progressbar = ttk.Style()
        style_progressbar.theme_use("default")
        style_progressbar.configure(
            "green.Horizontal.TProgressbar",
            background='#970000',
            troughcolor='#970000'
        )
        today_progress_bar = ttk.Progressbar(
            top_header_frame_left,
            style="green.Horizontal.TProgressbar",
            orient="horizontal", length=249, mode="determinate"
        )
        today_progress_bar.place(x=0, y=80)
        today_progress_bar["value"] = value


def exit_tms():
    answer = messagebox.askyesno("Close TMS", "Do you want to close TMS?")
    if answer:
        sys.exit()
    else:
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Time Management System 1.1: Main Screen")
    root.resizable(0, 0)
    root.configure(bg="#212121")

    root.protocol("WM_DELETE_WINDOW", exit_tms)

    right_frame = tk.Frame(
        None,
        width=230,
        height=600,
        background="#2F3030"
    )
    right_frame.place(x=570, y=0)

    header_label = tk.Label(
        right_frame,
        text="TMS 1.1",
        font=('Montserrat', '40'),
        background="#2F3030",
        foreground="#474747"
    )
    header_label.place(x=15, y=30)

    refresh_button = tk.Button(
        right_frame,
        text="REFRESH",
        font=('Arial', '8', 'bold'),
        width=10,
        command=insert_data_to_today_tasks,
        background='#00BFC5',
        foreground='#000000'
    )
    refresh_button.place(x=140, y=5)

    task_list_button = tk.Button(
        right_frame,
        text="MY TASKS",
        font=('Arial', '11'),
        width=21,
        command=tasks_list,
        background='#0003C8',
        foreground='#FFFFFF'
    )
    task_list_button.place(x=16, y=160)

    delegated_tasks_list_button = tk.Button(
        right_frame,
        text="DELEGATED TASKS",
        font=('Arial', '11'),
        width=21,
        command=delegated_tasks_list,
        background='#0003C8',
        foreground='#FFFFFF'
    )
    delegated_tasks_list_button.place(x=16, y=200)

    project_list_button = tk.Button(
        right_frame,
        text="PROJECTS",
        font=('Arial', '11'),
        width=21,
        command=None,
        background='#0003C8',
        foreground='#FFFFFF'
    )
    project_list_button.place(x=16, y=240)

    catch_box_button = tk.Button(
        right_frame,
        text="CATCH-BOX",
        font=('Arial', '11'),
        width=21,
        command=None,
        background='#0003C8',
        foreground='#FFFFFF'
    )
    catch_box_button.place(x=16, y=280)

    calendar_button = tk.Button(
        right_frame,
        text="CALENDAR",
        font=('Arial', '11'),
        width=21,
        command=None,
        background='#0003C8',
        foreground='#FFFFFF'
    )
    calendar_button.place(x=16, y=320)

    revision_button = tk.Button(
        right_frame,
        text="REVISION",
        font=('Arial', '11'),
        width=21,
        command=None,
        background='#0003C8',
        foreground='#FFFFFF'
    )
    revision_button.place(x=16, y=360)

    maybe_list_button = tk.Button(
        right_frame,
        text="MAYBE/SOMETIMES",
        font=('Arial', '11'),
        width=21,
        command=None,
        background='#0003C8',
        foreground='#FFFFFF'
    )
    maybe_list_button.place(x=16, y=400)

    birthday_list_button = tk.Button(
        right_frame,
        text="BIRTHDAYS",
        font=('Arial', '11'),
        width=21,
        command=None,
        background='#0003C8',
        foreground='#FFFFFF'
    )
    birthday_list_button.place(x=16, y=440)

    exit_button = tk.Button(
        right_frame,
        text="EXIT",
        font=('Arial', '11'),
        width=21,
        command=exit_tms,
        background='#970000',
        foreground='#FFFFFF'
    )
    exit_button.place(x=16, y=480)

    top_frame_left = tk.Frame(
        None,
        width=270,
        height=120,
        background="#2F3030"
    )
    top_frame_left.place(x=10, y=10)

    top_header_frame_left = tk.Frame(
        top_frame_left,
        width=250,
        height=90,
        background='#6A6A6A'
    )
    top_header_frame_left.place(x=8, y=18)

    my_day_sign = tk.Label(
        top_header_frame_left,
        text="MY DAY",
        font=("Open Sans", "30"),
        background="#6A6A6A",
        foreground="#FFFFFF"
    )
    my_day_sign.place(x=45, y=20)

    top_frame_right = tk.Frame(
        None,
        width=270,
        height=120,
        background="#2F3030"
    )
    top_frame_right.place(x=290, y=10)

    top_header_frame_right = tk.Frame(
        top_frame_right,
        width=250,
        height=90,
        background='#6A6A6A'
    )
    top_header_frame_right.place(x=8, y=18)

    date_sign = tk.Label(
        top_header_frame_right,
        text="Date",
        font=("Open Sans ", "20"),
        background="#6A6A6A",
        foreground="#FFFFFF"
    )
    date_sign.place(x=20, y=8)

    date_label = tk.Label(
        top_header_frame_right,
        text=time.strftime('%d/%m/%y'),
        font=("Open Sans ", "20"),
        background="#6A6A6A",
        foreground="#FFFFFF"
    )
    date_label.place(x=95, y=8)

    weekday_sign = tk.Label(
        top_header_frame_right,
        text="Day",
        font=("Open Sans ", "20"),
        background="#6A6A6A",
        foreground="#FFFFFF"
    )
    weekday_sign.place(x=20, y=45)

    weekday_label = tk.Label(
        top_header_frame_right,
        text=time.strftime('%A'),
        font=("Open Sans ", "20"),
        background="#6A6A6A",
        foreground="#FFFFFF"
    )
    weekday_label.place(x=95, y=45)

    sign_label = tk.Label(
        right_frame,
        text='by VK',
        font=("Edwardian Script ITC", "25"),
        background='#2F3030',
        foreground='#FFFFFF'
    )
    sign_label.place(x=125, y=550)

    middle_frame_left = tk.Frame(
        None,
        width=320,
        height=235,
        background="#2F3030"
    )
    middle_frame_left.place(x=10, y=155)

    middle_frame_right = tk.Frame(
        None,
        width=202,
        height=230,
        background="#2F3030"
    )
    middle_frame_right.place(x=350, y=157)

    done_button = tk.Button(
        middle_frame_right,
        text="DONE",
        font=('Arial', '11'),
        width=18,
        command=task_done,
        background='#004C01',
        foreground='#FFFFFF'
    )
    done_button.place(x=20, y=20)

    see_task_button = tk.Button(
        middle_frame_right,
        text="SEE TASK",
        font=('Arial', '11'),
        width=18,
        command=see_task,
        background='#027853',
        foreground='#FFFFFF'
    )
    see_task_button.place(x=20, y=60)

    do_it_tomorrow_button = tk.Button(
        middle_frame_right,
        text="DO IT TOMORROW",
        font=('Arial', '11'),
        width=18,
        command=do_task_tomorrow,
        background='#027853',
        foreground='#FFFFFF'
    )
    do_it_tomorrow_button.place(x=20, y=100)

    move_to_button = tk.Button(
        middle_frame_right,
        text="MOVE TO",
        font=('Arial', '11'),
        width=18,
        command=move_task_to,
        background='#027853',
        foreground='#FFFFFF'
    )
    move_to_button.place(x=20, y=140)

    delete_button = tk.Button(
        middle_frame_right,
        text="DELETE",
        font=('Arial', '11'),
        width=18,
        command=delete_task_from_database,
        background='#970000',
        foreground='#FFFFFF'
    )
    delete_button.place(x=20, y=180)

    remark_field_label = tk.Label(
        middle_frame_left,
        text="Tasks for today:",
        font=("Open Sans", "12", "bold"),
        background="#2F3030",
        foreground="#000000"
    )
    remark_field_label.place(x=10, y=6)

    today_tasks_list = tk.Listbox(
        middle_frame_left,
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

    check_internet()
    insert_data_to_today_tasks()
    progress_bar_of_day()
    root.after(1000, insert_data_to_today_tasks)
    root.mainloop()
    