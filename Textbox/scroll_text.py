from tkinter import *
from tkinter.scrolledtext import ScrolledText
win=Tk()
win.geometry("500x600")
win.title("Scroll Text")
st=ScrolledText(win,width=30,height=15,borderwidth=3)
st.place(x=10,y=10)
win.mainloop()