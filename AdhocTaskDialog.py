import tkinter as tk
import datetime
# Created on : 14. 10. 2023, 14:20:23
# Author     : prohi


class AdhocTaskDialog():

    dlg = None
    dbManager = None
    currentDate = None
    
    topFrame = None
    taskDescriptionLabel = None
    taskDescriptionTextfield = None
    keywordsTextLabel = None
    keywordsTextfield = None
    expectedResultLabel = None
    expectedResultTextfield = None
    currentDateLabel = None
    
    saveButton = None
    exitButton = None
    
    def __init__(self, master=None, dbManager=None):
        self.dlg = tk.Toplevel(master)
        self.dbManager = dbManager
        self.currentDate = datetime.datetime.now().strftime("%d/%m/%Y")
        
        self.dlg.geometry("600x200")
        self.dlg.title("Adhoc Task")
        self.dlg.resizable(0, 0)
        self.dlg.configure(bg="#212121")
        
        self.createDialog()
        
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
        
    def exitDialog(self):
#        if len(self.taskDescriptionTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close Adhoc Task", "If you close the window, the changes will be lost.\nClose Adhoc Task?")
#            if answer:
#                self.dlg.destroy()
#            else:
#                pass
#        elif len(self.keywordsTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close Adhoc Task", "If you close the window, the changes will be lost.\nClose Adhoc Task?")
#            if answer:
#                self.dlg.destroy()
#            else:
#                pass
#        elif len(self.expectedResultTextfield.get()) != 0:
#            answer = messagebox.askyesno("Close Adhoc Task", "If you close the window, the changes will be lost.\nClose Adhoc Task?")
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
            text = "ADHOC TASK",
            font = ('Montserrat', '15'),
            background = "#212121",
            foreground = "#FFFFFF"
        )
        self.headerLabel.place(x = 230, y = 5)

        self.topFrame = tk.Frame(
            self.dlg,
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
            self.dlg,
            text = self.currentDate,
            font = ('Montserrat', '15'),
            background = "#212121",
            foreground = "#FFFFFF"
        )
        self.currentDateLabel.place(x = 15, y = 160)

        self.saveButton = tk.Button(
            self.dlg,
            text = "SAVE",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = self.saveAdhocTask,
            background = '#A94102',
            foreground = '#FFFFFF'
        )
        self.saveButton.place(x = 480, y = 160)

        self.exitButton = tk.Button(
            self.dlg,
            text = "EXIT",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = self.exitDialog,
            background = '#970000',
            foreground = '#FFFFFF'
        )
        self.exitButton.place(x = 370, y = 160)
        return self


#    self.dlg.protocol("WM_DELETE_WINDOW", exit_adhoc_task)
