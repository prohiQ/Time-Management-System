import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox

# Created on : 14. 10. 2023, 14:20:23
# Author     : prohi


class TaskWindow(tk.Toplevel):

    def __init__(self, dbManager=None):
        super().__init__()

        self.geometry("600x400")
        self.title("New Task")
        self.resizable(0, 0)
        self.configure(bg="#212121")
        self.dbManager = dbManager
    
    def chooseDate(self):
        self.currentDateLabel.config(background = "#A8A803")
        self.currentDateLabel.config(foreground = "#FFFFFF")
        self.currentDateLabel.config(text=self.cal.get_date())
        
    def chooseDeadline(self):
        self.deadlineDateLabel.config(background = "#970000")
        self.deadlineDateLabel.config(foreground = "#FFFFFF")
        self.deadlineDateLabel.config(text=self.cal.get_date())  

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

    def exitWindow(self):
#        if len(self.taskDescriptionTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
#            if answer:
#                self.destroy()
#            else:
#                pass
#        elif len(self.keywordsTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
#            if answer:
#                self.destroy()
#            else:
#                pass
#        elif len(self.expectedResultTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close New Task", "If you close the window, the changes will be lost.\nClose the New Task?")
#            if answer:
#                self.destroy()
#            else:
#                pass
#        else:
#            self.destroy()
        self.destroy()

    def show(self):
        self.createWindow()

    def createWindow(self):
        self.headerLabel = tk.Label(
            self,
            text="NEW TASK",
            font=("Montserrat", "15"),
            background="#212121",
            foreground="#FFFFFF",
        )
        self.headerLabel.place(x=230, y=5)

        self.cal = Calendar(
            self,
            selectmode='day',
            date_pattern=('dd/mm/yyyy'),
            background="black"
        )
        self.cal.place(x=330, y=160)

        self.topFrame = tk.Frame(
            self, 
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
            self, 
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

        self.currentDateLabel = tk.Label(
            self.middleFrame,
            text = "",
            font = ('Montserrat', '12'),
            background = "#2F3030",
            foreground = "#FFFFFF"
        )
        self.currentDateLabel.place(x = 180, y = 5)

        self.deadlineDateButton = tk.Button(
            self.middleFrame,
            text = "Choose Deadline",
            font = ('Arial', '10', 'bold'),
            width = 16,
            command = self.chooseDeadline,
            background = self.middleFrame["background"],
            foreground = '#FFFFFF'
        )
        self.deadlineDateButton.place(x=10, y=45)

        self.deadlineDateLabel = tk.Label(
            self.middleFrame,
            text = "",
            font = ('Montserrat', '12', 'bold'),
            background = self.middleFrame["background"],
            foreground = "#FFFFFF"
        )
        self.deadlineDateLabel.place(x = 180, y = 45)

        self.bottomFrame = tk.Frame(
            self, 
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
            self,
            text="SAVE",
            font=("Arial", "10", "bold"),
            width=11,
            command=self.saveTask,
            background="#A94102",
            foreground="#FFFFFF",
        )
        self.saveButton.place(x=480, y=360)

        self.exitButton = tk.Button(
            self,
            text="EXIT",
            font=("Arial", "10", "bold"),
            width=11,
            command=self.exitWindow,
            background="#970000",
            foreground="#FFFFFF",
        )
        self.exitButton.place(x=370, y=360)


#    self.protocol("WM_DELETE_WINDOW", exit_adhoc_task)
