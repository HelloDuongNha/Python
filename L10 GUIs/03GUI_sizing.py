from tkinter import *


window = Tk()
window.geometry("350x200")
window.title("COMP1753 GUI")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

window.mainloop()
