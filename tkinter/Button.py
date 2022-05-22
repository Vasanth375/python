# imporing the required packages
from tkinter import *
from tkinter import messagebox

# creating window
win = Tk()

# setting size of window
win.geometry("500x500+10+10")

def function():
    messagebox.showinfo("Button one","You Clicked")
#button used to click and show the content reside in function function
butt = Button(win,text="Button One", command=function)

# place button on window
butt.pack()

# repeat the window
win.mainloop()