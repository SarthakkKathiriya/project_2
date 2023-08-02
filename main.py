
from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar

def your_date():
    date.config(text="Selected Date: " + my_cal.get_date())
    # question for why bg and fg which are in main documentation not working hear.
root = Tk()
root.title('my calendar')
root.geometry('600x500')

my_cal = Calendar(root, selectmode="day", year=2023, month=8, day=2)
my_cal.pack(pady=10)

date_btn=Button(root,  text='Select the Date',command=your_date)
date_btn.pack(pady=5)

date = Label(root, text = "")
date.pack(pady = 5)

root.mainloop()