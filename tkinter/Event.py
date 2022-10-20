from tkinter import *

window = Tk()
window.geometry("500x500+10+10")
def function(event):
    print("mouse event")

label = Label(window, text="click me")

label.pack()

label.bind("<Double-Enter>", function)
window.mainloop()