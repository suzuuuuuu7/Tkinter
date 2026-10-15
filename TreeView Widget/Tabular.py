from tkinter import *
from tkinter import ttk
win=Tk()
win.title("Tabular data")
win.geometry("800x500")
win.columnconfigure(0,weight=1)
win.rowconfigure(0,weight=1)
size_grip=ttk.Sizegrip(win)
size_grip.grid(row=1,sticky=SE)
#.................. styling
style=ttk.Style()
style.theme_use("clam")
style.configure("Treeview",relief="solid",borderwidth=1,)

data_list=[("Sujata kc","22","sujalkc324@gmail.com"),("Manoj barstool",22,"m3@gmail.com")]
col=("Name_1","Age_1","EmailAddress_1")
tree=ttk.Treeview(win,columns=col,show="headings")
tree.heading("Name_1",text="Name")
tree.heading("Age_1",text="Age")
tree.heading("EmailAddress_1",text="Address")
for data in data_list:
    tree.insert("",END,values=data)

tree.place(x=20,y=20,height=200,width=600)
win.mainloop()
