import tkinter as tk
window = tk.Tk()
window.title("File integrity checker")
window.geometry("500x500")
Entries =[]
for i in range(4):
  name = input("enter name")
  label = tk.Label(window,text = name)
  label.grid(row=i,column=1)
  entry = tk.Entry(window)
  entry.grid(row=i, column=0,padx=10,pady=10)
  Entries.append(entry)
def show():
  value = []
  for entry in Entries:
    value.append(entry.get())
  print(value)
button =tk.Button(window, text="Show entries", command=show)
button.place(relx=0.3,rely=0.4)
window.mainloop()
