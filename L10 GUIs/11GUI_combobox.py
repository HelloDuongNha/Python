from tkinter import *
from tkinter.ttk import *


window = Tk()
window.geometry("350x200")
window.title("COMP1753 GUI")

combo = Combobox(window)
combo["values"] = ["zero", "one", "two", "three", "four"]
combo.current(1)
combo.grid(column=0, row=0)

window.mainloop()
