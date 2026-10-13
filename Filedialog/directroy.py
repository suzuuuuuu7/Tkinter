# askdirectory()
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
win =Tk()
win.geometry("500x500")
win.title("File dialog")
win.columnconfigure(0,weight=1)
win.rowconfigure(0,weight=1)
size_grip=ttk.Sizegrip(win)
size_grip.grid(row=1,sticky=SE)

def directory():
    var=filedialog.askdirectory(initialdir="/",title="dialog")# give address
    print(var)

btn=Button(win,text="Opn",command=directory)
btn.place(x=100,y=50)
win.mainloop()