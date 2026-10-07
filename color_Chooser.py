from tkinter import *
from tkinter.colorchooser import askcolor
win=Tk()
win.geometry("500x500")
win.title("select color")
win.resizable(False,False)
def show():
    color=askcolor(title="choose color")
    print(color)
    win.config(bg= color[1])
button=Button(win,text="open",command=show)
button.place(x=10,y=10)
win.mainloop()