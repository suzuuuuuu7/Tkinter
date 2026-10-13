from tkinter import *
from tkinter import ttk
win=Tk()
win.title("Size Grip")
win.columnconfigure(0,weight=1)
win.rowconfigure(0,weight=1)
size_grip=ttk.Sizegrip(win)
size_grip.grid(row=1,sticky=SE)
win.mainloop()