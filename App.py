import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
from EventWindow import *
from AdhocTaskWindow import *
from CatchIdeaWindow import *
from RemarkWindow import *
from TaskWindow import *
from DBManager import *
from MainWindow import MainWindow as mw
# Created on : 14. 10. 2023, 13:23:56
# Author     : prohi


# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.

if __name__ == "__main__":
#    root = tk.Tk()
#    root.geometry("800x600")
#    root.title("Time Management System 1.1: Main Screen")
#    root.resizable(0, 0)
#    root.configure(bg="#212121")

    dbm = DBManager('tasks.db')
    mwi = mw(dbm=dbm)
#    evdlg = AdhocTaskDialog(root, dbm)
#    evdlg = CatchIdeaDialog(root, dbm)
#    evdlg = EventWindow( dbm)
#    evdlg = RemarkDialog(root, dbm)
#    evdlg = TaskDialog(root, dbm)
#    evdlg.show
    mwi.show()
    mwi.mainloop()
#    evdlg.mainloop()
