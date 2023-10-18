import tkinter as tk
from tkcalendar import Calendar
import datetime
# Created on : 14. 10. 2023, 14:20:23
# Author     : prohi


class RemarkDialog():

    dlg = None
    cal = None
    dbManager = None

    headerLabel = None

    topFrame = None
    remarkDescriptionLabel = None
    remarkDescriptionTextfield = None
    remarkField1Label = None
    remarkField1Textfield = None
    remarkField2Label = None
    remarkField2Textfield = None

    middleFrame = None
    dateButton = None
    dateLabel = None

    saveButton = None
    exitButton = None

    def __init__(self, master=None, dbManager=None):
        self.dbManager = dbManager
        self.currentDate = datetime.datetime.now().strftime("%d/%m/%Y")

        self.dlg = tk.Toplevel(master)
        self.dlg.geometry("600x400")
        self.dlg.title("Add new remark")
        self.dlg.resizable(0, 0)
        self.dlg.configure(bg="#212121")
        
        self.cal = Calendar (self.dlg, selectmode = 'day', date_pattern = ('dd/mm/yyyy'), background = "black")
        self.cal.place(x= 330, y= 160)
        
        self.createDialog()
        
    def chooseDate(self):
        self.dateLabel.config(text = self.cal.get_date())
        
    def saveRemark(self):
        values = {
#            "taskID":None,
#            "taskOrAction":self.taskDescriptionTextField.get(),
#            "keywords":self.keywordsTextField.get(),
#            "expectedResult":self.expectedResultTextField.get(),
#            "date":self.dateTextField,
#            "deadline":None,
#            "delegateTo":None,
            "cooperateWith":None
        }
        self.dbManager.saveRemark(values)
        
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
            text = "REMARKS FOR SOME DAY",
            font = ('Montserrat', '15'),
            background = "#212121",
            foreground = "#FFFFFF"
        )
        self.headerLabel.place(x = 180, y = 5)

        self.topFrame = tk.Frame(
            self.dlg,
            width = 570,
            height = 100,
            background = "#2F3030"
        )
        self.topFrame.place(x = 15, y = 40)

        self.remarkDescriptionLabel= tk.Label(
            self.topFrame,
            text = "REMARK",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.remarkDescriptionLabel.place(x = 10, y = 5)

        self.remarkDescriptionTextfield = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10", "bold"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.remarkDescriptionTextfield.place(x = 150, y = 5)

        self.remarkField1Label = tk.Label(
            self.topFrame,
            text = "Field 1",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.remarkField1Label.place(x = 10, y = 35)

        self.remarkField1Textfield = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.remarkField1Textfield.place(x = 150, y = 35)

        self.remarkField2Label = tk.Label(
            self.topFrame,
            text = "Field 2",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.remarkField2Label.place(x = 10, y = 65)

        self.remarkField2Textfield = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.remarkField2Textfield.place(x = 150, y = 65)

        self.middleFrame = tk.Frame(
            self.dlg,
            width = 305,
            height = 80,
            background = "#2F3030"
        )
        self.middleFrame.place(x = 15, y = 160)

        self.dateButton = tk.Button(
            self.middleFrame,
            text = "Choose Date",
            font = ('Arial', '10', 'bold'),
            width = 16,
            command = self.chooseDate,
            background = '#464646',
            foreground = '#FFFFFF'
        )
        self.dateButton.place(x = 15, y = 25)

        self.dateLabel = tk.Label(
            self.middleFrame,
            text = None,
            font = ('Montserrat', '12'),
            background = "#9E019A",
            foreground = "#FFFFFF"
        )
        self.dateLabel.place(x = 180, y = 25)

        self.saveButton = tk.Button(
            self.dlg,
            text = "SAVE",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = self.saveRemark,
            background = '#A94102',
            foreground = '#FFFFFF'
        )
        self.saveButton.place(x = 480, y = 360)

        self.exitButton = tk.Button(
            self.dlg,
            text = "EXIT",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = self.exitDialog,
            background = '#970000',
            foreground = '#FFFFFF'
        )
        self.exitButton.place(x = 370, y = 360)

#    self.dlg.protocol("WM_DELETE_WINDOW", exit_adhoc_task)