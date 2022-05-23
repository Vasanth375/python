from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
n=1
def count():
    global n
    messagebox.showinfo("button Counter", "clicks {0}".format(n))
    n+=1

butt = Button(window, text="Click me", command=count)
butt.pack()
window.mainloop()

