import webbrowser
from tkinter import * # Treeview()
from tkinter import ttk
win = Tk()
win.geometry("600x700")
win.resizable(False,False)
win.title("Treeview")
label=Label(win,text="Hacker",font=("Arial",20,"bold"))
label.place(x=10,y=10)
tree = ttk.Treeview(win)
tree.insert("",END,text="Black",iid=0)
tree.insert("",END,text="Gray",iid=1)
tree.insert("",END,text="White",iid=2)
tree.insert("",END,text="Hacktivist",iid=3)
tree.insert("",END,text="Red",iid=4)
tree.insert("",END,text="Green",iid=5)
tree.insert("",END,text="Red team",iid=6)
tree.insert("",END,text="Script kids",iid=7)
a= tree.insert("",END,text="Main villian",iid=8,open = True)
# move data to black
tree.insert("",END,text="Illegal work",iid=9)
tree.move(8,"0",0)
tree.move(9,"0",1)

#operation
def clicked(event):
    item = tree.identify_row(event.y) # event.y tell vertical position of our mouse
    if item == a: # check whether a is detected
        label.config(text="yes, main Villian")
tree.bind("<Button-1>",clicked)
label=Label(win,text="",font=("Times new roman",10,"bold"))
label.place(x=220,y=100)
# move to gray
tree.insert("",END,text="Both of good and bad",iid=10)
tree.insert("",END,text="Hire by organization",iid=11)
tree.move(10,"1",0)
tree.move(11,"1",1)
tree.place(x=10,y=60,height=300,width=200)
def show(event):
    webbrowser.open("https://www.geeksforgeeks.org/what-is-a-hacker/")
label1=Label(win,text="Click here",cursor="hand2",font=("Arial",12,"underline"))
label1.place(x=10,y=390)
label1.bind("<Button-1>",show)
win.mainloop()