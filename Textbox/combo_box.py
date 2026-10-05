from tkinter import *
from tkinter import ttk
win=Tk()
win.geometry("500x600")
list_1=["Python","C*","Java","C","Dart"]
data=StringVar()
def show():
    p = data.get()
    label.config(text=p)
combo = ttk.Combobox(win,values=list_1,state="readonly",width=15,height=100,font=("times new roman",16))
combo.set("Choose language")
combo.place(x=100,y=100)
label = Label(win,text="",font=("times new roman",16,"bold"),textvariable=data)
label.place(x=100,y=250)
btn=Button(win,text="show",command=show)
btn.place(x=170,y=300)
win.mainloop()