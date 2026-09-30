import tkinter as tk
window = tk.Tk()
window.title("Password Entry")
window.geometry("400x300")
label = tk.Label(window,text ="Enter Password")
label.place(x=100,y=100)
password = tk.Entry(window,show="*")
password.place(x=100,y=130)
def show():
    p = password.get()
    print(p)
tk.Button(window,text="Submit",command = show).place(x=130,y=160)
window.mainloop()
