#ASKSAVEASFILENAME
#ASKSAVEASFILE
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
win=Tk()
win.geometry("300x300")
win.columnconfigure(0,weight=1)
win.rowconfigure(0,weight=1)
resize=ttk.Sizegrip(win)
resize.grid(row=0,sticky=SE)
def save_file():
    var=filedialog.asksaveasfile(title="Save as",initialdir="/",filetypes=(("Text file","*.txt"),("All files","*.*"),("python","*.py")),defaultextension="*.py",)
    var.write("welcome to wscube")
    var.close()

button=Button(win,text="save",command=save_file)
button.place(x=100,y=100)
win.mainloop()