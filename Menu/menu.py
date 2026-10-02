from tkinter import *
win = Tk()
win.geometry("500x500")
win.title("Menu")
win.resizable(width=False,height=False)
main_manu = Menu(win)
win.config(menu=main_manu) # add changes to win(object)

#file menu
file_menu =Menu(main_manu,tearoff = 0)

#sub menu
sub_menu=Menu(main_manu,tearoff=0)
sub_menu.add_command(label="Black hat hacker")
sub_menu.add_command(label="White hat hacker")
sub_menu.add_command(label="Gray hat hacker")
file_menu.add_cascade(label="New",menu=sub_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Rename") # add sub menu
file_menu.add_separator()
main_manu.add_cascade(label="File",menu=file_menu)

# Edit menu
file_menu1 =Menu(main_manu,tearoff = 0)
file_menu1.add_command(label="copy")
file_menu1.add_command(label="cut")
file_menu1.add_command(label="paste")
file_menu1.add_command(label="delete") # add sub menu
main_manu.add_cascade(label="Edit",menu=file_menu1)
file_menu1.add_separator()
win.mainloop()
