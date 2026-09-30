from tkinter import *
window = Tk()
try:
    window.geometry("500x500")
    var = StringVar(window,value="sujal kc")
    print(var.get())
    var1=IntVar(window)
    var1.set(20)
    print(var1.get())
    var2 = DoubleVar(window,name = "float")
    var2.set(44.44)
    print(var2.get())
    var3= BooleanVar(window)
    var3.set(True)
    print(var3.get())
except:
 print("Error")
window.mainloop()
