from tkinter import *
from tkinter.messagebox import showinfo,showerror,showwarning
win=Tk()
win.title("Login Page")
win.geometry("500x500")
def info():
    showinfo(title="success",message="successfully logged in")
def error():
    showerror(title="error",message="unexpected error occured")
def warning():
    showwarning(title="warning",message="This may harmful your system")
button1=Button(win,text="info",command=info)
button1.place(x=10,y=10,width=40,height=40)
button2=Button(win,text="error",command=error)
button2.place(x=10,y=50,width=40,height=40)
button3=Button(win,text="warning",command=warning)
button3.place(x=10,y=90,width=50,height=40)

win.mainloop()
