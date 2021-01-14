from plyer import notification
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
#Name = simpledialog.askstring(title="NAME",
                                  #prompt="ENTER NAME?:")
#Date = simpledialog.askstring(title="Test",
                                  #prompt="ENTER DOB:")
#Date = simpledialog.askstring(title = "DOB", prompt = "Entire Start Date in MM/DD/YYYY format:", initialvalue="01/01/2010")
Name = "Arun"
Date = "12/12/2020"
# check it out
#print("Hello", USER_INP)
notification.notify(title= Name,message= Date,app_icon = None,timeout= 10,toast=False)
