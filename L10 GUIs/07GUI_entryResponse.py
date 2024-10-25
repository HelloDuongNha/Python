from tkinter import *


window = Tk()
window.geometry("350x200")
window.title("COMP1753 GUI")

input_txt = Entry(window, width=10)
input_txt.grid(column=0, row=0)


def clicked():
    res = "Hello " + input_txt.get()
    output.set(res)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

output = StringVar()

txt = Entry(window, width=10, textvariable=output)
txt.grid(column=2, row=0)

window.mainloop()
