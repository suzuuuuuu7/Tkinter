from tkinter import *
from tkcalendar import Calendar # import calendar
from tkinter.messagebox import showinfo
from tkcalendar import DateEntry
win = Tk()
win.title("DatePicker")
win.geometry("500x600")
win.resizable(width=False,height=False)
def get_date():
    var=calendar.get_date()
    showinfo(title="DatePicker",message=var)
    print(var)
#Non linear data picker
calendar=Calendar(win,selectmode="day",year=2005,month=5,day=9) # defualt date
calendar.place(x=50,y=20,height=250,width=400)
button=Button(win,text="confirm",font=("arial",17,"bold"),cursor="hand2",bg="green",command=get_date)
button.place(x=170,y=300)

def date_picker():
    var=calendar.get_date()
    showinfo(title="DatePicker",message=var)
    print(var)
#........liner datepicker
#Non linear data picker
Date_picker=DateEntry(win,selectmode="day",year=2005,month=5,day=9) # defualt date
Date_picker.place(x=50,y=400,height=50,width=400)
button=Button(win,text="Select",font=("arial",17,"bold"),cursor="hand2",bg="green",command=date_picker)
button.place(x=170,y=500)


win.mainloop()