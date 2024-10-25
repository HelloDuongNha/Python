from tkinter import *


window = Tk()
window.geometry("350x200")
window.title("COMP1753 GUI")

chk_state = BooleanVar()
chk_state.set(True)

chk = Checkbutton(window, text="Choose", var=chk_state)
chk.grid(column=0, row=0)

window.mainloop()
