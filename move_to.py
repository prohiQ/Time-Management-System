import tkinter as tk



def move_task_to():
    move_to_win = tk.Tk()
    move_to_win.geometry ("300x270")
    move_to_win.title("Move Task to ...")
    move_to_win.resizable(0,0)
    move_to_win.configure(bg = "#212121")

    main_frame = tk.Frame(
        move_to_win,
        width = 270,
        height = 250,
        background = "#2F3030"
    )
    main_frame.place(x = 15, y = 10)

    delegation_button = tk.Button(
        main_frame,
        text = "DELEGATION",
        font = ('Arial', '11'),
        width = 24,
        command = None,
        background = '#0003C8',
        foreground = '#FFFFFF'
    )
    delegation_button.place(x = 25, y = 10)

    projects_button = tk.Button(
        main_frame,
        text = "PROJECTS",
        font = ('Arial', '11'),
        width = 24,
        command = None,
        background = '#0003C8',
        foreground = '#FFFFFF'
    )
    projects_button.place(x = 25, y = 50)

    catchbox_button = tk.Button(
        main_frame,
        text = "CATCH-BOX",
        font = ('Arial', '11'),
        width = 24,
        command = None,
        background = '#0003C8',
        foreground = '#FFFFFF'
    )
    catchbox_button.place(x = 25, y = 90)

    maybe_sometimes_button = tk.Button(
        main_frame,
        text = "MAYBE/SOMETIMES",
        font = ('Arial', '11'),
        width = 24,
        command = None,
        background = '#0003C8',
        foreground = '#FFFFFF'
    )
    maybe_sometimes_button.place(x = 25, y = 130)

    remarks_button = tk.Button(
        main_frame,
        text = "REMARKS",
        font = ('Arial', '11'),
        width = 24,
        command = None,
        background = '#0003C8',
        foreground = '#FFFFFF'
    )
    remarks_button.place(x = 25, y = 170)

    exit_move_to_button = tk.Button(
        main_frame,
        text = "EXIT",
        font = ('Arial', '11'),
        width = 24,
        command = move_to_win.destroy,
        background = '#970000',
        foreground = '#FFFFFF'
    )
    exit_move_to_button.place(x = 25, y = 210)

