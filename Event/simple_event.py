import webbrowser
from tkinter import *
win = Tk()
win.geometry("500x500")
win.resizable(False,False)
win.title("Event")
def web(event):
    webbrowser.open_new_tab("https://www.youtube.com")

label=Label(win,text="click here",font=("times new roman",20,"bold","underline"))
label.place(x=10,y=20)
label.bind("<Button-1>",web)

def show(event):
    print("ok")
button = Button(win,text="open")
button.place(x=10,y=100,height=100,width=100)
button.bind("<Double Button-1>",show)
win.mainloop()