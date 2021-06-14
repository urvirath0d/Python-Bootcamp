# importing library
from tkinter import *
from tkinter import ttk

window = Tk()
# Declaring Window Title
window.title("Registration Screen")
# Declaring Window Size
window.geometry('500x1000')
# Declaring Window Color
window.configure(background="grey94")
# below four field are declared
L= Label(window, text="Register Your Self For Placement").grid(row=0, column=1)
Firstname = Label(window, text="First Name").grid(row=1, column=0)
LastName = Label(window, text="Last Name").grid(row=2, column=0)
Email = Label(window, text="Email Id").grid(row=3, column=0)
Mobile = Label(window, text="Contact Number").grid(row=4, column=0)
EnrollmentNumber = Label(window, text="Enrollment Number").grid(row=5, column=0)
Division = Label(window, text="Division").grid(row=6, column=0)
CGPA = Label(window, text="CGPA").grid(row=7, column=0)
PassOutYear = Label(window, text="Year Of Passing BE").grid(row=8, column=0)
Backlog = Label(window, text="Backlogs In Any Sem").grid(row=9, column=0)
Experience = Label(window, text="Years OF Experience").grid(row=10, column=0)

#L1 = Entry(window).grid(row=0, column=1)
Firstname1 = Entry(window).grid(row=1, column=1)
Lastname1 = Entry(window).grid(row=2, column=1)
Email1 = Entry(window).grid(row=3, column=1)
Mobile1 = Entry(window).grid(row=4, column=1)
EnrollmentNumber1 = Entry(window).grid(row=5, column=1)
#Division1 = Entry(window).grid(row=5, column=1)
CGPA1 = Entry(window).grid(row=7, column=1)
#PassOutYear1 = Entry(window).grid(row=7, column=1)
# Backlog1 = Entry(window).grid(row=8, column=1)
Experience1 = Entry(window).grid(row=10, column=1)


# function declaration
def clicked():
    res = "Welcome to" + txt.get()
    lbl.configure(text=res)
btn = ttk.Button(window, text="Submit").grid(row=11, column=0)
btn2 = ttk.Radiobutton(window, text='yes', value=1).grid(column=1,row=9)
btn3 = ttk.Radiobutton(window, text="no", value=2).grid(row=9, column=2)
btn4= ttk.Checkbutton(window, text="C").grid(row=6, column=2)
btn5= ttk.Checkbutton(window, text="D").grid(row=6, column=1)
list=['2021','2022','2023','2024']
v=StringVar()
droplist= OptionMenu(window,v,*list)
v.set('Pass Out Year')
droplist.grid(row=8,column=1)

window.mainloop()
