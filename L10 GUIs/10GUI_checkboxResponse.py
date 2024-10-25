from tkinter import *


window = Tk()
window.geometry("350x200")
window.title("COMP1753 GUI")

chk_state = BooleanVar()
chk_state.set(True)

chk = Checkbutton(window, text="Choose", var=chk_state)
chk.grid(column=0, row=0)


def clicked():
    if chk_state.get():
        res = "Checkbox is checked"
    else:
        res = "Checkbox is not checked"
    output.set(res)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

output = StringVar()

txt = Entry(window, width=30, textvariable=output, state="readonly")
txt.grid(column=2, row=0)

window.mainloop()
