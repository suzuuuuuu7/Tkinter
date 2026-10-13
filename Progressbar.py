
from tkinter import *
from tkinter import ttk
win =Tk()
win.geometry("500x500")
win.title("File dialog")
win.columnconfigure(0,weight=1)
win.rowconfigure(0,weight=1)
size_grip=ttk.Sizegrip(win)
size_grip.grid(row=1,sticky=SE)
Progress_bar=ttk.Progressbar(win,orient=HORIZONTAL,length=200,mode="determinate",)
Progress_bar.place(x=100,y=100,width=200,height=40)
btn1=Button(win,text="start",command=Progress_bar.start)
btn1.place(x=100,y=50)
btn1=Button(win,text="stop",command=Progress_bar.stop)
btn1.place(x=100,y=20)
win.mainloop()