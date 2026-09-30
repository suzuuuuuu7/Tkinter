from tkinter import *
window = Tk()
window.title("Pack")
window.geometry("400x300+200+100")
window.resizable(False,False)
window.iconbitmap(r"C:\Users\sujal\Downloads\down.ico")
window.attributes("-alpha",0.9)
window.config(bg="gray")
lab = Label(window,text="Name",font=("times new roman",20,"bold"),fg="black",bg="yellow")
lab.pack(fill="x")
lab1 = Label(window,text="Address",font=("times new roman",20,"bold"),fg="white",bg="orange")
lab1.pack(ipady=10,fill="y",ipadx=10,expand=True)
lab2 = Label(window,text="Age",font=("times new roman",20,"italic"),fg="gray",bg="green")
lab2.pack(fill="x")
window.mainloop()


