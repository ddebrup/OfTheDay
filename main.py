from pynput import keyboard
import csv
from plyer import notification
import tkinter as tk
from tkinter import simpledialog
import pandas as pd
import schedule
from datetime import datetime
from datetime import date
import time
from pynput.keyboard import HotKey, Key, KeyCode, Listener

#Function for data input
def function_1():
    import tkinter as tk
    from tkinter import simpledialog

    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    Name = simpledialog.askstring(title="NAME",
                                      prompt="ENTER NAME?:")
   
    Date = simpledialog.askstring(title = "DOB", 
                                  prompt = "Entire Start Date in MM/DD/YYYY format:", 
                                  initialvalue="01/01/2010")
    
    
    
    
    try:
        with open('Storage.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")

        

        new=[]
        new.append(Name)
        new.append(Date)
        if new not in data:
            with open(r'Storage.csv', 'a') as g: 

            # using csv.writer method from CSV package 
                write = csv.writer(g) 

                write.writerow(new) 
        
    
    except:
        
        new=[]
        new.append(Name)
        new.append(Date)
        
        with open(r'Storage.csv', 'a') as g: 

            # using csv.writer method from CSV package 
            write = csv.writer(g) 

            write.writerow(new) 

#Function for notification alert
def function_2():
    
    with open('Storage.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            today = date.today()
            d1 = today.strftime("%d/%m")

            for entry in data:
                if entry[1][0:5]==d1:
                    message="Wish " + entry[0]
                    notification.notify(title= "OfTheDay",
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)  

#Hotkey for storage & comparison
hotkey1 = HotKey(
    [Key.alt, KeyCode(char='a')],
    function_1
)

#Hotkey for notification & retrieval
hotkey2 = HotKey(
    [Key.alt, KeyCode(char='r')],
    function_2
)
#Hotkey for upcoming updates
#hotkey3 = HotKey()

hotkeys = [hotkey1, hotkey2]


def signal_press_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.press(l.canonical(key))

def signal_release_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.release(l.canonical(key))

with Listener(on_press=signal_press_to_hotkeys, on_release=signal_release_to_hotkeys) as l:
    l.join()

