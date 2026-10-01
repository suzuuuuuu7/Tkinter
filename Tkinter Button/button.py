from tkinter import *
win = Tk()
win.geometry("500x500")
win.title("Button")
def change():
    label.configure(text="world")
button = Button(win,text="ON",font=20,fg="red",bg="gray",relief=SUNKEN,cursor="hand2")
button.place(x=100,y=100)
button1 = Button(win,text="Click",font=20,fg="Green",bg="red",relief=SUNKEN,cursor="hand2",command=change)
button1.place(x=200,y=100)
label = Label(win,text="Hello",font=("Times Roman",20,"bold"))
label.place(x=200,y=150)
win.mainloop()