from tkinter import *
from tkinter.messagebox import askyesno,askquestion
win = Tk()
win.title("ask yes no")
win.geometry("500x500")
win.resizable(False,False)
def ask():
    var=askyesno(title="ask",message="are you gay?",)
    if var:
        label.config(text="python")

    else:
        label.config(text="Java")


button=Button(win,text="check",font=("arial",16,"bold"),relief="sunken",cursor="arrow",command=ask)
button.pack(padx=20,pady=20)
label=Label(win,text="",font=("arial",16,"bold"))
label.pack(padx=20,pady=40)

win.mainloop()