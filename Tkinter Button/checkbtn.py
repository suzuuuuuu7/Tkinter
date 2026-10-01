from tkinter import *
win = Tk()
win.geometry("300x300")
def show():
    label.config(text=var.get())
var = StringVar()
ck = Checkbutton(win,text="check",fg="green",font=("Times Roman",10,"bold"),onvalue="python"
,offvalue="java",variable=var,command=show,disabledforeground="yellow")
ck.deselect()
ck.pack()
ck.pack()
label = Label(win,text="",font=("Times Roman",20,"bold"))
label.pack()
b = Button(win,text="show",command=show,)
b.pack()
win.mainloop()