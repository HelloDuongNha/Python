from tkinter import *
from tkinter.ttk import *


window = Tk()
window.geometry("600x200")
window.title("COMP1753 GUI")

combo = Combobox(window)
combo["values"] = ["zero", "one", "two", "three", "four"]
combo.current(1)
combo.grid(column=0, row=0)


def clicked():
    res = f"You have selected {combo.get()}"
    output.set(res)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

output = StringVar()

txt = Entry(window, width=30, textvariable=output, state="readonly")
txt.grid(column=2, row=0)

window.mainloop()
