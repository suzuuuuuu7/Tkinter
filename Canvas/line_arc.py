from tkinter import *
win=Tk()
win.geometry("800x1000")
win.title("Canvas")
canvas=Canvas(win,bg="gray")
canvas.place(x=0,y=0,height=800,width=500)
coordinates=50,10,200,200 # x0 y0 x1 y1
#create_line
line1=canvas.create_line(coordinates,fill ="red")
line2=canvas.create_line(200,100,300,100,fill="green")
line3=canvas.create_line(100,300,300,300,fill="blue")
arc=canvas.create_arc(200,200,400,300,start=0,extent=360,fill="orange")
win.mainloop()