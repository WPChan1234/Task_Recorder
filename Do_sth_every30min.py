from datetime import datetime
import time
from Screen_Capture import Screen_CAP
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
FilePath=filedialog.askdirectory()
root.destroy()

print(FilePath)
def run(condition, FilePath):
    while datetime.now().minute not in {0,10,20,30,40,50}:  # Wait 1 second until we are synced up with the 'every 10 minutes' clock
        time.sleep(1)

    while condition == True:
        Screen_CAP(FilePath)
        time.sleep(10*60)  # Wait for 10 minutes

run(True,FilePath)

