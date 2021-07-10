from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

messagebox.showinfo('Task Recorder','Screen Capture/ Request Task Input every 30min')


def define_file():
    file = filedialog.askdirectory()
    lbl.configure(text=file)
    return (file)

window = Tk()

window.title("Task Recorder")

window.geometry('350x200')

Line1=Label(window, text="Storage location for .txt file")
lbl = Label(window, text="Define data storage file")

Line1.grid(column=0, row=0)
lbl.grid(column=0, row=1)

btn = Button(window, text="Define",command=define_file)

btn.grid(column=1, row=1)



# Define File Storage




window.mainloop()