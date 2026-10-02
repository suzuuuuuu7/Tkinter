from tkinter import *
win=Tk()
win.title("Option Button")
win.geometry("400x300")
win.resizable(False,False)
def show(var):
    var = value.get()
    l.config(text=var)
opn_list =["Data Science","Cyber Security","Ai/Ml","web development","Graphic Designer"]
value = StringVar()
value.set("SEO")
op_menu = OptionMenu(win,value,*opn_list,command=show)
op_menu.place(x=100,y=100)
l=Label(win,text="",)
l.place(x=100,y=170)
win.mainloop()