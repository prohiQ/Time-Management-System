import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
from EventDialog import *
from AdhocTaskDialog import *
from CatchIdeaDialog import *
from RemarkDialog import *
from TaskDialog import *
from DBManager import *
# Created on : 14. 10. 2023, 13:23:56
# Author     : prohi


# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Time Management System 1.1: Main Screen")
    root.resizable(0, 0)
    root.configure(bg="#212121")

    dbm = DBManager('tasks.db')
#    evdlg = AdhocTaskDialog(root, dbm)
#    evdlg = CatchIdeaDialog(root, dbm)
#    evdlg = EventDialog(root, dbm)
#    evdlg = RemarkDialog(root, dbm)
    evdlg = TaskDialog(root, dbm)
    evdlg.show
    root.mainloop()
