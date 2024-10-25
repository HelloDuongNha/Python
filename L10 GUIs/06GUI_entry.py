from tkinter import *


window = Tk()
window.geometry("350x200")
window.title("COMP1753 GUI")

input_txt = Entry(window, width=10)
input_txt.grid(column=0, row=0)


def clicked():
    res = "Hello " + input_txt.get()
    lbl.configure(text=res)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

lbl = Label(window, text="Hello")
lbl.grid(column=2, row=0)

window.mainloop()
