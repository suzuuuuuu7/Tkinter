import tkinter as tk
window = tk.Tk()
window.title("Entry")
window.geometry("400x300")
tk.Label(window,text="Entry").grid(row = 0,column=1)
entry = tk.Entry(window)
entry.grid(row=0,column =0,padx=10,pady =10)

def show():
    entry.insert(0, "intelipaat.com")
    name = entry.get()
    print(name)
def remove():
    entry.delete(0,tk.END)
tk.Button(window,text="Insert  entry",command=show).grid(row = 1,column=1)
tk.Button(window,text=" delete entry",command=remove).grid(row = 2,column=1)
window.mainloop()
