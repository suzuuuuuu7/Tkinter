#Scrollbar()
from tkinter import *
import tkinter as ttk
win=Tk()
win.geometry("600x700")
win.resizable(False,False)
win.title("Scrollbar")
textbox=Text(win,font=("Times Roman",14),fg="black",bg="white")
textbox.place(x=10,y=50,height=400,width=489)
scrollbar=ttk.Scrollbar(win,command=textbox.yview,orient="vertical")
scrollbar.place(x=500,y=55,height=400,width=20)
textbox["yscrollcommand"]=scrollbar.set

win.mainloop()