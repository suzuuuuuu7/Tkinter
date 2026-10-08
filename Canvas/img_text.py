from tkinter import *
win=Tk()
win.geometry("700x800")
win.resizable(False,False)
canvas=Canvas(win,bg="light blue",height=600,width=500)
canvas.place(x=0,y=0)
canvas.create_text(150,300,text="Hello canvas",fill="red",font=("times new roman",22,"bold"))
img=PhotoImage(file=r"C:\Users\sujal\Pictures\pec.png")
canvas.create_image(150,150,image=img)

win.mainloop()