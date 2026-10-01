from tkinter import*
win = Tk()
win.geometry("500x500")
win.title("Image")
photo = PhotoImage(file="img.png")
label = Label(win,image =photo,text="Super Eagle",compound="top",font=("Times Roman",20,"bold"))
label.place(x=100,y=100)
win.mainloop()