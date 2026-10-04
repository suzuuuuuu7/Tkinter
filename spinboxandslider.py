from tkinter import *
from tkinter import ttk
win=Tk()
win.title("Spin box")
win.geometry("500x500")
win.resizable(width=False,height=False)
var = IntVar()
def display():
    data=var.get()
    label.config(text=data)
spain = ttk.Spinbox(win,from_=0,to=100,increment=1,width=25,font=("roboto",20,"italic"),textvariable=var,command=display)
spain.place(x=50,y=100,height=30)
label =Label(win,text="",font=("Times Roman",30,"bold"),fg="red")
label.place(x=150,y=150)
value = DoubleVar()
def show(name):
   name= str(value.get())
   label1.config(text=name)
slider = Scale(win, from_=0, to=100, orient=HORIZONTAL,font=("Times Roman",20,"bold"),variable=value,command = show)
slider.place(x=100,y=250,height=400,width=300)
label1=Label(win,text="",font=("Times Roman",20,"bold"),fg="blue")
label1.place(x=200,y=350)
win.mainloop()