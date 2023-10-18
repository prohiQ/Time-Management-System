import tkinter as tk
# Created on : 14. 10. 2023, 14:20:23
# Author     : prohi

class CatchIdeaDialog():

    dlg = None
    dbManager = None
    
    headerLabel = None

    topFrame = None
    ideaDescriptionLabel = None
    ideaDescriptionTextfield = None
    keywordsLabel = None
    keywordsTextfield = None
    remarksLabel = None
    remarksTextfield = None

    saveButton = None
    exitButton = None
    
    def __init__(self, master=None, dbManager=None):
        self.dbManager = dbManager
        
        self.dlg = tk.Toplevel(master)
        self.dlg.geometry("600x200")
        self.dlg.title("Catch the Idea")
        self.dlg.resizable(0, 0)
        self.dlg.configure(bg="#212121")
        
        self.createDialog()
        
    def saveTask(self):
        values = {
#            "taskID":None,
#            "taskOrAction":self.tideaDescriptionTextField.get(),
#            "keywords":self.keywordsTextField.get(),
#            "remarks":self.remarksTextField.get(),
        }
        self.dbManager.saveIdea(values)
        
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
            text = "WHAT DO YOU WANT TO CATCH?",
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
            text = "IDEA OR ACTION",
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

        self.remarksLabel = tk.Label(
            self.topFrame,
            text = "Remarks",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.remarksLabel.place(x = 10, y = 65)

        self.remarksTextfield = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.remarksTextfield.place(x = 150, y = 65)

        self.saveButton = tk.Button(
            self.dlg,
            text = "SAVE",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = self.saveTask,
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

