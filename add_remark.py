import tkinter as tk
from tkcalendar import Calendar

def add_remark():
    add_remark_win = tk.Tk()
    add_remark_win.geometry ("600x400")
    add_remark_win.title("Add Remark")
    add_remark_win.resizable(0,0)
    add_remark_win.configure(bg = "#212121")

    cal = Calendar (add_remark_win, selectmode = 'day', date_pattern = ('dd/mm/yyyy'), background = "black")
    cal.place(x= 330, y= 160)

    def choose_date():
        chosen_date = cal.get_date()
        chosen_date_label = tk.Label(
            middle_frame,
            text = chosen_date,
            font = ('Montserrat', '12'),
            background = "#9E019A",
            foreground = "#FFFFFF"
        )
        chosen_date_label.place(x = 180, y = 25)
    

    header_label = tk.Label(
        add_remark_win,
        text = "REMARKS FOR SOME DAY",
        font = ('Montserrat', '15'),
        background = "#212121",
        foreground = "#FFFFFF"
    )
    header_label.place(x = 180, y = 5)

    top_frame = tk.Frame(
        add_remark_win,
        width = 570,
        height = 100,
        background = "#2F3030"
    )
    top_frame.place(x = 15, y = 40)

    remark_description_label = tk.Label(
        top_frame,
        text = "REMARK",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    remark_description_label.place(x = 10, y = 5)

    remark_description_row = tk.Entry(
        top_frame,
        font = ("Open Sans", "10", "bold"),
        width = 56,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    remark_description_row.place(x = 150, y = 5)

    remark_field1_label = tk.Label(
        top_frame,
        text = "Field 1",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    remark_field1_label.place(x = 10, y = 35)

    remark_field1_row = tk.Entry(
        top_frame,
        font = ("Open Sans", "10"),
        width = 56,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    remark_field1_row.place(x = 150, y = 35)

    remark_field2_label = tk.Label(
        top_frame,
        text = "Field 2",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    remark_field2_label.place(x = 10, y = 65)

    remark_field2_row = tk.Entry(
        top_frame,
        font = ("Open Sans", "10"),
        width = 56,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    remark_field2_row.place(x = 150, y = 65)

    middle_frame = tk.Frame(
        add_remark_win,
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
    date_button.place(x = 15, y = 25)

    save_button = tk.Button(
        add_remark_win,
        text = "SAVE",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = None,
        background = '#9E019A',
        foreground = '#FFFFFF'
    )
    save_button.place(x = 480, y = 360)

    exit_button = tk.Button(
        add_remark_win,
        text = "EXIT",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = add_remark_win.destroy,
        background = '#970000',
        foreground = '#FFFFFF'
    )
    exit_button.place(x = 370, y = 360)

