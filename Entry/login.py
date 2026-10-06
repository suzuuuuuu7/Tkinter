from tkinter import *
win = Tk()
var = StringVar()
msg=Message(win,text="",width=450,font=("times new roman",18,"bold"),fg="green")
def success():
    msg.config(text="successfully run")
msg.place(x=210,y=310)
def fail():
    msg.config(text="fail to login")
def show():
    email=e1.get()
    print(email)
    pa = e2.get()
    print(pa)
    if email=="sujalkc324@gmail.com" and pa=="12345":
        success()
    else:
        fail()


win.title("Login Page")
win.geometry("500x520")
win.resizable(False,False)
win.iconbitmap(r"C:\Users\sujal\Downloads\login.png")
l1=Label(win,text="Email",font=("Times New Roman",20,"bold"))
l1.place(x=80,y=50)
e1=Entry(win,bg="gray",font=14)
e1.place(x=170,y=50,height=40,width=250,)
l2=Label(win,text="Password",font=("Times New Roman",20,"bold"))
l2.place(x=40,y=150)
e2=Entry(win,bg="gray",font=14,show="*")
e2.place(x=170,y=150,height=40,width=250,)
button =Button(win,text="Login ",command=show,font=("Times New Roman",20,"bold"),fg="red")
button.place(x=230,y=250,height=40,width=100)
win.mainloop()