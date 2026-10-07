from tkinter import *
# sub window
def open():
    new_window=Toplevel()
    new_window.title("new window")
    new_window.geometry("300x400")
    new_window.configure(bg="green")
    new_window.resizable(width=False,height=False)
    new_window.mainloop()
# main window
win=Tk()
win.geometry("500x500")
win.resizable(width=False,height=False)
win.title("main window")
button=Button(win,text="open",command=open)
button.place(x=100,y=100)
win.mainloop()