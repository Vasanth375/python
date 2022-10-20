'''
Taking input from textfield from window
'''
from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("Window")
l1 = Label(window, text="Physics")
l1.place(x=10, y=10)
e1 = Entry(window, bd=5)
e1.place(x=60, y=10)

l2 = Label(window, text="Maths")
l2.place(x=10, y=10)
e2 = Entry(window, bd=5)
e2.place(x=60, y=50)

l3 = Label(window, text="Total")
l3.place(x=10, y=150)
e3 = Entry(window, bd=5)
e3.place(x=60, y=150)

b = Button(window, text="ADD")
b.place(x=100, y=100)
window.geometry("250x250+10+10")
window.mainloop()