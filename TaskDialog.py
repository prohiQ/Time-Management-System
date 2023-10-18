import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox

# Created on : 14. 10. 2023, 14:20:23
# Author     : prohi


class TaskDialog:
    dlg = None
    dbManager = None
    cal = None
    currentDate = None
    deadlineDate = None

    headerLabel = None
    
    topFrame = None
    taskDescriptionLabel = None
    taskDescriptionTextfield = None
    keywordsTextLabel = None
    keywordsTextfield = None
    expectedResultLabel = None
    expectedResultTextfield = None
    
    middleFrame = None
    currentDateButton = None
    currentDateLabel = None
    deadlineDateButton = None
    deadlineDateLabel = None
    
    bottomFrame = None
    delegatedToLabel = None
    delegatedToTextfield = None
    cooperateWithLabel = None
    cooperateWithTextfield = None

    saveButton = None
    exitButton = None

    def __init__(self, master=None, dbManager=None):
        self.dlg = tk.Toplevel(master)
        self.dlg.geometry("600x400")
        self.dlg.title("New Task")
        self.dlg.resizable(0, 0)
        self.dlg.configure(bg="#212121")
        
        self.createDialog()
        
        self.cal = Calendar(
            self.dlg,
            selectmode='day',
            date_pattern=('dd/mm/yyyy'),
            background="black"
        )
        self.cal.place(x=330, y=160)
        
    def chooseDate(self):
        self.currentDate = self.cal.get_date()
        self.currentDateLabel = tk.Label(
            self.middleFrame,
            text = self.currentDate,
            font = ('Montserrat', '12'),
            background = "#2F3030",
            foreground = "#FFFFFF"
        )
        self.currentDateLabel.place(x = 180, y = 5)

    def chooseDeadline(self):
        self.deadlineDate = self.cal.get_date()
        self.deadlineDateLabel = tk.Label(
            self.middleFrame,
            text = self.deadlineDate,
            font = ('Montserrat', '12', 'bold'),
            background = "#970000",
            foreground = "#FFFFFF"
        )
        self.deadlineDateLabel.place(x = 180, y = 45)
    
    def saveTask(self):
        values = {
            "taskID": None,
            "taskOrAction": self.taskDescriptionTextField.get(),
            "keywords": self.keywordsTextField.get(),
            "expectedResult": self.expectedResultTextField.get(),
            "date": self.currentDateTextField,
            "deadline": self.deadlineDateTextfield,
            "delegateTo": self.delegateToTextfield,
            "cooperateWith": self.cooperateWithTextfield,
        }
        
        if self.currentDate or self.deadlineDate is not None:
            if self.currentDate is None and self.deadlineDate is not None:
                self.currentDate = self.deadlineDate
            else:
                pass
                if len(self.delegateToTextfield.get()) == 0:
                
                    self.saveTask(values)
                    messagebox.showinfo("Success", "Task successfully saved!")
                else:
                    self.saveDelegatedTask(values)
                    messagebox.showinfo("Success", "Task successfully saved into DELEGATED TASKS!")
        else:
            messagebox.showerror("ERROR", "Date is not selected. Select date for the task.")

    def exitDialog(self):
#        if len(self.taskDescriptionTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
#            if answer:
#                self.dlg.destroy()
#            else:
#                pass
#        elif len(self.keywordsTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
#            if answer:
#                self.dlg.destroy()
#            else:
#                pass
#        elif len(self.expectedResultTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
#            if answer:
#                self.dlg.destroy()
#            else:
#                pass
#        else:
#            self.dlg.destroy()
        self.dlg.destroy()

    def show(self):
        self.dlg.pack()

    def createDialog(self):
        self.headerLabel = tk.Label(
            self.dlg,
            text="NEW TASK",
            font=("Montserrat", "15"),
            background="#212121",
            foreground="#FFFFFF",
        )
        self.headerLabel.place(x=230, y=5)

        self.topFrame = tk.Frame(
            self.dlg, 
            width=570, 
            height=100, 
            background="#2F3030"
        )
        self.topFrame.place(x=15, y=40)

        self.taskDescriptionLabel = tk.Label(
            self.topFrame,
            text="TASK OR ACTION",
            font=("Open Sans", "10", "bold"),
            background="#2F3030",
            foreground="#000000",
        )
        self.taskDescriptionLabel.place(x=10, y=5)

        self.taskDescriptionTextfield = tk.Entry(
            self.topFrame,
            font=("Open Sans", "10", "bold"),
            width=56,
            insertbackground="#FFFFFF",
            background="#000000",
            foreground="#FFFFFF",
        )
        self.taskDescriptionTextfield.place(x=150, y=5)

        self.keywordsLabel = tk.Label(
            self.topFrame,
            text="Keywords",
            font=("Open Sans", "10", "bold"),
            background="#2F3030",
            foreground="#000000",
        )
        self.keywordsLabel.place(x=10, y=35)

        self.keywordsTextfield = tk.Entry(
            self.topFrame,
            font=("Open Sans", "10"),
            width=56,
            insertbackground="#FFFFFF",
            background="#000000",
            foreground="#FFFFFF",
        )
        self.keywordsTextfield.place(x=150, y=35)

        self.expectedResultLabel = tk.Label(
            self.topFrame,
            text="Expected Result",
            font=("Open Sans", "10", "bold"),
            background="#2F3030",
            foreground="#000000",
        )
        self.expectedResultLabel.place(x=10, y=65)

        self.expectedResultTextfield = tk.Entry(
            self.topFrame,
            font=("Open Sans", "10"),
            width=56,
            insertbackground="#FFFFFF",
            background="#000000",
            foreground="#FFFFFF",
        )
        self.expectedResultTextfield.place(x=150, y=65)

        self.middleFrame = tk.Frame(
            self.dlg, 
            width=305, 
            height=80, 
            background="#2F3030"
        )
        self.middleFrame.place(x=15, y=160)

        self.currentDateButton = tk.Button(
            self.middleFrame,
            text = "Choose Date",
            font = ('Arial', '10', 'bold'),
            width = 16,
            command = self.chooseDate,
            background = '#464646',
            foreground = '#FFFFFF'
        )
        self.currentDateButton.place(x=10, y=5)

        self.deadlineDateButton = tk.Button(
            self.middleFrame,
            text = "Choose Deadline",
            font = ('Arial', '10', 'bold'),
            width = 16,
            command = self.chooseDeadline,
            background = '#464646',
            foreground = '#FFFFFF'
        )
        self.deadlineDateButton.place(x=10, y=45)

        self.bottomFrame = tk.Frame(
            self.dlg, 
            width=305, 
            height=80, 
            background="#2F3030"
        )
        self.bottomFrame.place(x=15, y=265)
        
        self.delegateToLabel = tk.Label(
            self.bottomFrame,
            text="Delegate to",
            font=("Open Sans", "10", "bold"),
            background="#2F3030",
            foreground="#000000",
        )
        self.delegateToLabel.place(x=10, y=5)

        self.delegateToTextfield = tk.Entry(
            self.bottomFrame,
            font=("Open Sans", "10"),
            width=20,
            insertbackground="#FFFFFF",
            background="#000000",
            foreground="#FFFFFF",
        )
        self.delegateToTextfield.place(x=150, y=5)

        self.cooperateWithLabel = tk.Label(
            self.bottomFrame,
            text="Coopereate with",
            font=("Open Sans", "10", "bold"),
            background="#2F3030",
            foreground="#000000",
        )
        self.cooperateWithLabel.place(x=10, y=35)

        self.cooperateWithTextfield = tk.Entry(
            self.bottomFrame,
            font=("Open Sans", "10"),
            width=20,
            insertbackground="#FFFFFF",
            background="#000000",
            foreground="#FFFFFF",
        )
        self.cooperateWithTextfield.place(x=150, y=35)

        self.saveButton = tk.Button(
            self.dlg,
            text="SAVE",
            font=("Arial", "10", "bold"),
            width=11,
            command=self.saveTask,
            background="#A94102",
            foreground="#FFFFFF",
        )
        self.saveButton.place(x=480, y=360)

        self.exitButton = tk.Button(
            self.dlg,
            text="EXIT",
            font=("Arial", "10", "bold"),
            width=11,
            command=self.exitDialog,
            background="#970000",
            foreground="#FFFFFF",
        )
        self.exitButton.place(x=370, y=360)


#    self.dlg.protocol("WM_DELETE_WINDOW", exit_adhoc_task)
