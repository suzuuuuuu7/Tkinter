import tkinter as tk
window = tk.Tk()
window.title("File integrity checker")
window.geometry("600x400")
tk.Label(window,text="Enter iP address "
                     "or"
                     " domain name").grid(row=0,column=0,padx=20,pady=10)
tk.Entry(window).grid(row=1,column =0,padx=10)
tk.Label(window,text="Port no").grid(row=0,column=1,padx=20,pady=10)
tk.Entry(window).grid(row=1,column =1)
tk.Label(window,text="Services").grid(row=0,column=2,padx=20,pady=10)
tk.Entry(window).grid(row=1,column =2,padx=10)

button =tk.Button(window, text="submit here")
button.place(relx=0.2, rely = 0.3)
window.mainloop()