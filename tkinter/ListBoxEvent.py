from tkinter import *
top = Tk()
top.geometry("500x500")

def method(event):
	char = listbox.get(ANCHOR)
	top.configure(bg=char)



lb = Label(top, text="This is listbox label")
listbox = Listbox(top)
listbox.insert(1, "pink")
listbox.insert(2, "red")
listbox.insert(3, "C")

lb.bind("<Button>", method)

lb.pack()
listbox.pack()

top.mainloop()