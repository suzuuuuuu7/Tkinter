from tkinter import *
win = Tk()
def run():
    status_bar.config(text="run")
win.geometry("500x500")
win.title("Status bar")
win.resizable(False,False)
status_bar=Label(win,text="status bar",bd=3,relief=SUNKEN,anchor=W)
status_bar.pack(side=BOTTOM,fill=X)
button= Button(win,text="run",command=run)
button.pack(padx=20,pady=20)
win.mainloop()