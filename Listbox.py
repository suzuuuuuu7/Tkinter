from tkinter import *
win=Tk()
win.title("List box")
win.geometry("500x500")
win.resizable(False,False)
def get_data(event):
    event =p.get()
    print(event)
list_1=["Python","Java","C","html/css"] # list of variable to put inside the list box
p=StringVar(value=list_1) # data type
list_box=Listbox(win,listvariable=p,font=("times roman",15,"bold"),selectmode="extended")# create list box
list_box.place(x=20,y=20,height=150,width=150)
list_box.bind("<<ListboxSelect>>",get_data)
win.mainloop()
