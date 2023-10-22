import tkinter as tk
from tkcalendar import Calendar
# Created on : 14. 10. 2023, 9:22:47
# Author     : prohi


# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.
class EventWindow(tk.Toplevel):   
    
    def __init__(self, dbManager=None):
        super().__init__()
        
        self.geometry("600x400")
        self.title("Add Event")
        self.resizable(0, 0)
        self.configure(bg="#212121")
        self.dbManager = dbManager

    def saveEvent(self):
        values = {
#            "taskID":None,
#            "taskOrAction":self.taskDescriptionTextField.get(),
#            "keywords":self.keywordsTextField.get(),
#            "expectedResult":self.expectedResultTextField.get(),
#            "date":self.dateTextField,
#            "deadline":None,
#            "delegateTo":None,
#            "cooperateWith":None
        }
        self.dbManager.saveEvent(values)
        
    def exitDialog(self):
#        if len(self.descriptionTextField.get()) != 0:
#            answer = messagebox.askyesno("Close Add Remark", "All changes will be lost.\nDo you want to continue?")
#            if answer:
#                self.destroy()
#            else:
#                pass
#        elif len(self.field1TextField.get()) != 0:
#            answer = messagebox.askyesno("Close Add Remark", "All changes will be lost.\nDo you want to continue?")
#            if answer:
#                self.destroy()
#            else:
#                pass
#        elif len(self.field2TextField.get()) != 0:
#            answer = messagebox.askyesno("Close Add Remark", "All changes will be lost.\nDo you want to continue?")
#            if answer:
#                self.destroy()
#            else:
#                pass
#        else:
#            self.destroy()
        self.destroy()
    
    def chooseStartDate(self):
        self.startDateLabel.config(background = "#A8A803")
        self.startDateLabel.config(foreground = "#FFFFFF")
        self.startDateLabel.config(text=self.cal.get_date())
        
    def chooseEndDate(self):
        self.endDateLabel.config(background = "#970000")
        self.endDateLabel.config(foreground = "#FFFFFF")
        self.endDateLabel.config(text=self.cal.get_date())        
    
    def show(self):
        self.createWindow()
    
    def createWindow(self):
        self.headerLabel = tk.Label(
            self,
            text = "NEW EVENT",
            font = ('Montserrat', '15'),
            background = "#212121",
            foreground = "#FFFFFF"
        )
        self.headerLabel.place(x = 240, y = 5)

        self.cal = Calendar(
            self,
            selectmode='day',
            date_pattern=('dd/mm/yyyy'),
            background="black"
        )
        self.cal.place(x=330, y=160)

        self.topFrame = tk.Frame(
            self,
            width = 570,
            height = 100,
            background = "#2F3030"
        )
        self.topFrame.place(x = 15, y = 40)

        self.descriptionLabel = tk.Label(
            self.topFrame,
            text = "EVENT",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.descriptionLabel.place(x = 10, y = 5)

        self.descriptionTextField = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10", "bold"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.descriptionTextField.place(x = 150, y = 5)

        self.field1Label = tk.Label(
            self.topFrame,
            text = "Field 1",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.field1Label.place(x = 10, y = 35)

        self.field1TextField = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.field1TextField.place(x = 150, y = 35)

        self.field2Label = tk.Label(
            self.topFrame,
            text = "Field 2",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.field2Label.place(x = 10, y = 65)

        self.field2TextField = tk.Entry(
            self.topFrame,
            font = ("Open Sans", "10"),
            width = 56,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.field2TextField.place(x = 150, y = 65)

        self.middleFrame = tk.Frame(
            self,
            width = 305,
            height = 80,
            background = "#2F3030"
        )
        self.middleFrame.place(x = 15, y = 160)

        self.startDateButton = tk.Button(
            self.middleFrame,
            text = "Choose Start Date",
            font = ('Arial', '10', 'bold'),
            width = 16,
            command = self.chooseStartDate,
            background = '#464646',
            foreground = '#FFFFFF'
        )
        self.startDateButton.place(x = 10, y = 5)

        self.startDateLabel = tk.Label(
            self.middleFrame,
            text = None,
            font = ('Montserrat', '12'),
            background = self.middleFrame["background"],
            foreground = "#FFFFFF"
        )
        self.startDateLabel.place(x = 180, y = 5)

        self.endDateButton = tk.Button(
            self.middleFrame,
            text = "Choose End Date",
            font = ('Arial', '10', 'bold'),
            width = 16,
            command = self.chooseEndDate,
            background = '#464646',
            foreground = '#FFFFFF'
        )
        self.endDateButton.place(x = 10, y = 45)

        self.endDateLabel = tk.Label(
            self.middleFrame,
            text = None,
            font = ('Montserrat', '12', 'bold'),
            background = self.middleFrame["background"],
            foreground = "#FFFFFF"
        )
        self.endDateLabel.place(x = 180, y = 45)

        self.saveButton = tk.Button(
            self,
            text = "SAVE",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = self.saveEvent,
            background = '#A8A803',
            foreground = '#FFFFFF'
        )
        self.saveButton.place(x = 480, y = 360)

        self.exitButton = tk.Button(
            self,
            text = "EXIT",
            font = ('Arial', '10', 'bold'),
            width = 11,
            command = self.exitDialog,
            background = '#970000',
            foreground = '#FFFFFF'
        )
        self.exitButton.place(x = 370, y = 360)

        self.bottomFrame = tk.Frame(
            self,
            width = 305,
            height = 80,
            background = "#2F3030"
        )
        self.bottomFrame.place(x = 15, y = 265)

        self.startTimeLabel = tk.Label(
            self.bottomFrame,
            text = "Start Time",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.startTimeLabel.place(x = 10, y = 5)

        self.startTimeTextField = tk.Entry(
            self.bottomFrame,
            font = ("Open Sans", "10"),
            width = 20,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.startTimeTextField.place(x = 150, y = 5)

        self.endTimeLabel = tk.Label(
            self.bottomFrame,
            text = "End Time",
            font = ("Open Sans", "10", "bold"),
            background = "#2F3030",
            foreground = "#000000"
        )
        self.endTimeLabel.place(x = 10, y = 35)

        self.endTimeTextField = tk.Entry(
            self.bottomFrame,
            font = ("Open Sans", "10"),
            width = 20,
            insertbackground = "#FFFFFF",
            background = "#000000",
            foreground = "#FFFFFF"
        )
        self.endTimeTextField.place(x = 150, y = 35)

        return self
