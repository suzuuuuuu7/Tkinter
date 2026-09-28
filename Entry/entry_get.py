import tkinter as tk
window = tk.Tk()
window.geometry("300x300")
window.title("Entry get")
entry = tk.Entry(window)
entry.place(relx=0.2,rely=0.2)
def show_name():
    name = entry.get()
    print("Your result",name)
    print("Thank you")

button = tk.Button(window, text="Submit", command=show_name)
button.pack()
window.mainloop()