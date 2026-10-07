from tkinter import *
from tkinter.messagebox import askokcancel,askretrycancel
win = Tk()
win.geometry("500x500")
win.resizable(width=False,height=False)
#askokcancel
def download():
    info = askokcancel(title="Download",message="This may be harmfully")
    print(info)
button = Button(win,text="download",command = download)
button.place(x=20,y=20)

#askretrycancel
def click():
    ans = askretrycancel(title="Click",message="may be malicious")
    print(ans)
    if ans:
        click()
    else:
        label.config(text="thankyou")
label=Label(win,text="")
label.place(x=20,y=150)
button1 = Button(win,text="click here",command = click)
button1.place(x=20,y=80)
win.mainloop()
