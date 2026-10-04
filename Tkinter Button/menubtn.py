from tkinter import *
win =Tk()
def show():
    label.config(text="file menu")
win.geometry("400x300")
win.title("menu button")
var = StringVar()
menu_btn=Menubutton(win,text="file") # create menu button
menu_btn.menu=Menu(menu_btn,tearoff = 0) # call menu
menu_btn["menu"]=menu_btn.menu # add menu
menu_btn.menu.add_checkbutton(label="New file",variable = var,command =show) # add sub buttons
menu_btn.menu.add_checkbutton(label="Open file")
menu_btn.menu.add_checkbutton(label="delete")
menu_btn.menu.add_checkbutton(label="save as")
menu_btn.pack()
label = Label(win, text="", font=("times new roman",10,"bold"))
label.pack()
label.pack()
win.mainloop()
