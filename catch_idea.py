import tkinter as tk

def catch_idea():
    catch_idea_win = tk.Tk()
    catch_idea_win.geometry ("600x200")
    catch_idea_win.title("Catch the Idea")
    catch_idea_win.resizable(0,0)
    catch_idea_win.configure(bg = "#212121")

    header_label = tk.Label(
        catch_idea_win,
        text = "WHAT DO YOU WANT TO CATCH?",
        font = ('Montserrat', '15'),
        background = "#212121",
        foreground = "#FFFFFF"
    )
    header_label.place(x = 150, y = 5)

    top_frame = tk.Frame(
        catch_idea_win,
        width = 570,
        height = 100,
        background = "#2F3030"
    )
    top_frame.place(x = 15, y = 40)

    idea_description_label = tk.Label(
        top_frame,
        text = "IDEA OR ACTION",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    idea_description_label.place(x = 10, y = 5)

    idea_description_row = tk.Entry(
        top_frame,
        font = ("Open Sans", "10", "bold"),
        width = 56,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    idea_description_row.place(x = 150, y = 5)

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

    remarks_label = tk.Label(
        top_frame,
        text = "Remarks",
        font = ("Open Sans", "10", "bold"),
        background = "#2F3030",
        foreground = "#000000"
    )
    remarks_label.place(x = 10, y = 65)

    remarks_row = tk.Entry(
        top_frame,
        font = ("Open Sans", "10"),
        width = 56,
        insertbackground = "#FFFFFF",
        background = "#000000",
        foreground = "#FFFFFF"
    )
    remarks_row.place(x = 150, y = 65)

    save_button = tk.Button(
        catch_idea_win,
        text = "SAVE",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = None,
        background = '#4F0082',
        foreground = '#FFFFFF'
    )
    save_button.place(x = 480, y = 160)

    exit_button = tk.Button(
        catch_idea_win,
        text = "EXIT",
        font = ('Arial', '10', 'bold'),
        width = 11,
        command = catch_idea_win.destroy,
        background = '#970000',
        foreground = '#FFFFFF'
    )
    exit_button.place(x = 370, y = 160)
