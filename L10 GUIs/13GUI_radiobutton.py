from tkinter import *


window = Tk()
window.geometry("350x200")
window.title("COMP1753 GUI")

selected = IntVar()
selected.set(1)

rad0 = Radiobutton(window, text="zero", value=0, variable=selected)
rad0.grid(column=0, row=0)
rad1 = Radiobutton(window, text="one", value=1, variable=selected)
rad1.grid(column=1, row=0)
rad2 = Radiobutton(window, text="two", value=2, variable=selected)
rad2.grid(column=2, row=0)

window.mainloop()
