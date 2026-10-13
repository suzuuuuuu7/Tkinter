#askopenfilename()
#askopenfile()
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
win =Tk()
win.geometry("500x500")
win.title("File dialog")
win.columnconfigure(0,weight=1)
win.rowconfigure(0,weight=1)
size_grip=ttk.Sizegrip(win)
size_grip.grid(row=1,sticky=SE)
#....askopenfilename()
# def open_file():
#     var=filedialog.askopenfilename(initialdir="/",title="open",filetypes=(("txtfile","*.txt"),("allfile","*.*"))) # give address
#     print(var)
# btn=Button(win,text="open",command=open_file)
# btn.place(x=100,y=20)

#.............askopenfile()

def open_fie():
    var=filedialog.askopenfile(initialdir="/",title="open",filetypes=(("txtfile","*.txt"),("allfile","*.*")))# give address
    if var:
        with var:
            read_file=var.read()
            print(read_file)

btn=Button(win,text="Opn",command=open_fie)
btn.place(x=100,y=50)


win.mainloop()