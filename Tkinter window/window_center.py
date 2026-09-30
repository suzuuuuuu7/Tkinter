from tkinter import *
window = Tk()
width = 400
height = 300
s_width = window.winfo_screenwidth()
s_height = window.winfo_screenheight()
c_x = int(s_width/2-width/2)
c_y = int(s_height/2-height/2)
window.geometry(f"{width}x{height}+{c_x}+{c_y}")
window.resizable(False,False)
window.mainloop()