# PanedWindow()
from tkinter import *
from tkinter import ttk
win=Tk()
win.title("Paned Window")
win.geometry("400x400")
panned_window=PanedWindow(win,orient=HORIZONTAL,sashwidth=4,showhandle=True,sashpad=10) # horizontal sliding
panned_window.pack(fill="both",expand=True)
left_side=Listbox(win)

left_side.pack(side="left")
panned_window.add(left_side)
right_side=Listbox(win)
right_side.pack(side="right")
panned_window.add(right_side)
win.mainloop()
