from tkinter import *


window = Tk()
window.geometry("350x200")
window.title("COMP1753 GUI")

selected = IntVar()
selected.set(1)

values = ["zero", "one", "two"]
for i in range(len(values)):
    rad = Radiobutton(window, text=values[i], value=i, variable=selected)
    rad.grid(column=i, row=0)


def clicked():
    res = f"You have selected option {selected.get()}"
    output.set(res)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=1)

output = StringVar()

txt = Entry(window, width=30, textvariable=output, state="readonly")
txt.grid(column=1, row=1, columnspan=2)

window.mainloop()
