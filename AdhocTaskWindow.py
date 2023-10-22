import tkinter as tk
import datetime
# Created on : 14. 10. 2023, 14:20:23
# Author     : prohi


class AdhocTaskWindow(tk.Toplevel):

#    dlg = None
#    dbManager = None
#    currentDate = None
#    
#    topFrame = None
#    taskDescriptionLabel = None
#    taskDescriptionTextfield = None
#    keywordsTextLabel = None
#    keywordsTextfield = None
#    expectedResultLabel = None
#    expectedResultTextfield = None
#    currentDateLabel = None
#    
#    saveButton = None
#    exitButton = None
    
    def __init__(self, master=None, dbManager=None):
        super().__init__()
        self.dbManager = dbManager
        self.currentDate = datetime.datetime.now().strftime("%d/%m/%Y")
        
        self.geometry("600x200")
        self.title("Adhoc Task")
        self.resizable(0, 0)
        self.configure(bg="#212121")
        
    def saveAdhocTask(self):
        values = {
            "taskID":None
#            "taskOrAction":self.taskDescriptionTextfield.get(),
#            "keywords":self.keywordsTextfield.get(),
#            "expectedResult":self.expectedResultTextfield.get(),
#            "date":self.dateTextfield,
#            "deadline":None,
#            "delegateTo":None,
#            "cooperateWith":None
        }
        self.dbManager.saveAdhocTask(values)
        
    def exitWindow(self):
#        if len(self.taskDescriptionTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close Adhoc Task", "If you close the window, the changes will be lost.\nClose Adhoc Task?")
#            if answer:
#                self.destroy()
#            else:
#                pass
#        elif len(self.keywordsTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close Adhoc Task", "If you close the window, the changes will be lost.\nClose Adhoc Task?")
#            if answer:
#                self.destroy()
#            else:
#                pass
#        elif len(self.expectedResultTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close Adhoc Task", "If you close the window, the changes will be lost.\nClose Adhoc Task?")
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
            text = "ADHOC TASK",
            font = ('Montserrat', '15'),
            background = "#212121",
            foreground = "#FFFFFF"
        )
        self.headerLabel.place(x = 230, y = 5)

        self.topFrame = tk.Frame(
            self,
            width = 570,
            height = 100,
            background = "#2F3030"
        )
        self.topFrame.place(x = 15, y = 40)

        self.taskDescriptionLabel= tk.Label(
            self.topFrame,
            text = "TASK OR ACTION",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.taskDescriptionLabel.place(x = 10, y = 5)

        self.taskDescriptionTextfield = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10", "bold"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.taskDescriptionTextfield.place(x = 150, y = 5)

        self.keywordsLabel = tk.Label(
            self.topFrame,
            text = "Keywords",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.keywordsLabel.place(x = 10, y = 35)

        self.keywordsTextfield = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.keywordsTextfield.place(x = 150, y = 35)

        self.expectedResultLabel = tk.Label(
            self.topFrame,
            text = "Expected Result",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.expectedResultLabel.place(x = 10, y = 65)

        self.expectedResultTextfield = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.expectedResultTextfield.place(x = 150, y = 65)

        self.currentDateLabel = tk.Label(
            self,
            text = self.currentDate,
            font = ('Montserrat', '15'),
            background = "#212121",
            foreground = "#FFFFFF"
        )
        self.currentDateLabel.place(x = 15, y = 160)

        self.saveButton = tk.Button(
            self,
            text = "SAVE",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = self.saveAdhocTask,
            background = '#A94102',
            foreground = '#FFFFFF'
        )
        self.saveButton.place(x = 480, y = 160)

        self.exitButton = tk.Button(
            self,
            text = "EXIT",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = self.exitWindow,
            background = '#970000',
            foreground = '#FFFFFF'
        )
        self.exitButton.place(x = 370, y = 160)
        return self


#    self.protocol("WM_DELETE_WINDOW", exit_adhoc_task)

