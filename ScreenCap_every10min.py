from datetime import datetime
import time
import tkinter as tk
from tkinter import filedialog
import pyautogui
import os

def Screen_CAP(FilePath):

    # Create target Directory if don't exist
    if not os.path.exists(FilePath):
        os.makedirs(FilePath)

    DateTime = datetime.now().strftime("%Y%m%d_%H%M")

    print(DateTime)
    screen = pyautogui.screenshot()
    screen.save(os.path.join(FilePath,DateTime+".jpg"))

def run(condition, FilePath):
    while datetime.now().minute not in {0,10,20,30,40,50}:  # Wait 1 second until we are synced up with the 'every 10 minutes' clock
        time.sleep(1)

    while condition == True:
        Screen_CAP(FilePath)
        time.sleep(10*60)  # Wait for 10 minutes


if __name__ == "__main__":
    YearMonth= datetime.now().strftime("%Y%m")
    MonthDay= datetime.now().strftime("%m%d")
    Weeekday= datetime.now().strftime("%a")

    # Define file path for screen shot storage
    root = tk.Tk()
    FilePath=filedialog.askdirectory(title= "Choose file path for Screen Shot Storage ")
    root.destroy()

    FilePath=FilePath+"/"+YearMonth+"/"+MonthDay+"("+Weeekday+")"


    run(True,FilePath)

