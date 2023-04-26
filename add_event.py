import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox

def add_event():
    add_event_win = tk.Tk()
    add_event_win.geometry ("600x400")
    add_event_win.title("Add Event")
    add_event_win.resizable(0,0)
    add_event_win.configure(bg = "#212121")
    
    cal = Calendar (add_event_win, selectmode = 'day', date_pattern = ('dd/mm/yyyy'), background = "black")
    cal.place(x= 330, y= 160)

    def choose_start_date():
        chosen_start_date = cal.get_date()
        chosen_start_date_label = tk.Label(
            middle_frame,
            text = chosen_start_date,
            font = ('Montserrat', '12'),
            background = "#A8A803",
            foreground = "#FFFFFF"
        )
        chosen_start_date_label.place(x = 180, y = 5)
    
    def choose_end_date():
        chosen_end_date = cal.get_date()
        chosen_end_date_label = tk.Label(
            middle_frame,
            text = chosen_end_date,
            font = ('Montserrat', '12', 'bold'),
            background = "#970000",
            foreground = "#FFFFFF"
        )
        chosen_end_date_label.place(x = 180, y = 45)
    
    def exit_add_event():
        if len(event_description_row.get()) != 0:
            answer = messagebox.askyesno("Close Add Remark", "All changes will be lost.\nDo you want to continue?")
            if answer:
                add_event_win.destroy()
            else:
                pass
        elif len(field1_row.get()) != 0:
            answer = messagebox.askyesno("Close Add Remark", "All changes will be lost.\nDo you want to continue?")
            if answer:
                add_event_win.destroy()
            else:
                pass
        elif len(field2_row.get()) != 0:
            answer = messagebox.askyesno("Close Add Remark", "All changes will be lost.\nDo you want to continue?")
            if answer:
                add_event_win.destroy()
            else:
                pass
        else:
            add_event_win.destroy()   

    header_label = tk.Label(
        add_event_win,
        text = "NEW EVENT",
        font = ('Montserrat', '15'),
        background = "#212121",
        foreground = "#FFFFFF"
    )
    header_label.place(x = 240, y = 5)

    top_frame = tk.Frame(
        add_event_win,
        width = 570,
        height = 100,
        background = "#2F3030"
    )
    top_frame.place(x = 15, y = 40)

    event_description_label = tk.Label(
        top_frame,
        text = "EVENT",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    event_description_label.place(x = 10, y = 5)

    event_description_row = tk.Entry(
        top_frame,
        font = ("Open Sans", "10", "bold"),
        width = 56,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    event_description_row.place(x = 150, y = 5)

    field1_label = tk.Label(
        top_frame,
        text = "Field 1",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    field1_label.place(x = 10, y = 35)

    field1_row = tk.Entry(
        top_frame,
        font = ("Open Sans", "10"),
        width = 56,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    field1_row.place(x = 150, y = 35)

    field2_label = tk.Label(
        top_frame,
        text = "Field 2",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    field2_label.place(x = 10, y = 65)

    field2_row = tk.Entry(
        top_frame,
        font = ("Open Sans", "10"),
        width = 56,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    field2_row.place(x = 150, y = 65)

    middle_frame = tk.Frame(
        add_event_win,
        width = 305,
        height = 80,
        background = "#2F3030"
    )
    middle_frame.place(x = 15, y = 160)

    start_date_button = tk.Button(
        middle_frame,
        text = "Choose Start Date",
        font = ('Arial', '10', 'bold'),
        width = 16,
        command = choose_start_date,
        background = '#464646',
        foreground = '#FFFFFF'
    )
    start_date_button.place(x = 10, y = 5)

    end_date_button = tk.Button(
        middle_frame,
        text = "Choose End Date",
        font = ('Arial', '10', 'bold'),
        width = 16,
        command = choose_end_date,
        background = '#464646',
        foreground = '#FFFFFF'
    )
    end_date_button.place(x = 10, y = 45)


    save_button = tk.Button(
        add_event_win,
        text = "SAVE",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = None,
        background = '#A8A803',
        foreground = '#FFFFFF'
    )
    save_button.place(x = 480, y = 360)

    exit_button = tk.Button(
        add_event_win,
        text = "EXIT",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = exit_add_event,
        background = '#970000',
        foreground = '#FFFFFF'
    )
    exit_button.place(x = 370, y = 360)

    bottom_frame = tk.Frame(
        add_event_win,
        width = 305,
        height = 80,
        background = "#2F3030"
    )
    bottom_frame.place(x = 15, y = 265)

    start_time_label = tk.Label(
        bottom_frame,
        text = "Start Time",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    start_time_label.place(x = 10, y = 5)

    start_time_row = tk.Entry(
        bottom_frame,
        font = ("Open Sans", "10"),
        width = 20,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    start_time_row.place(x = 150, y = 5)

    end_time_label = tk.Label(
        bottom_frame,
        text = "End Time",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    end_time_label.place(x = 10, y = 35)

    end_time_row = tk.Entry(
        bottom_frame,
        font = ("Open Sans", "10"),
        width = 20,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    end_time_row.place(x = 150, y = 35)

    add_event_win.protocol("WM_DELETE_WINDOW", exit_add_event)




