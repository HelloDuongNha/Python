from tkinter import *


def clicked():
    description = "..."
    pizza_price = 0
    print(f"Pizza chosen is {description}")
    txt_output.set(f"Pizza price is £{pizza_price:.2f}")


window = Tk()
window.geometry("250x400")
window.title("Python pizzas")

lbl0 = Label(window, text="Pizzas", font=("Arial Bold", 20))
lbl0.grid(column=0, row=0, sticky="W")

selected = IntVar()
selected.set(0)

rad0 = Radiobutton(window, text="margherita - £6.00", value=0, variable=selected)
rad0.grid(column=0, row=1, sticky="W")
rad1 = Radiobutton(window, text="napoletana - £7.00", value=1, variable=selected)
rad1.grid(column=0, row=2, sticky="W")
rad2 = Radiobutton(window, text="marinara - £7.50", value=2, variable=selected)
rad2.grid(column=0, row=3, sticky="W")

lbl1 = Label(window, text="Extras", font=("Arial Bold", 20))
lbl1.grid(column=0, row=4, sticky="W")

chk_state0 = BooleanVar()
chk0 = Checkbutton(window, text="mushrooms - £0.50", var=chk_state0)
chk0.grid(column=0, row=5, sticky="W")
chk_state1 = BooleanVar()
chk1 = Checkbutton(window, text="cheese - £1.00", var=chk_state1)
chk1.grid(column=0, row=6, sticky="W")
chk_state2 = BooleanVar()
chk2 = Checkbutton(window, text="anchovies - £1.50", var=chk_state2)
chk2.grid(column=0, row=7, sticky="W")
chk_state3 = BooleanVar()
chk3 = Checkbutton(window, text="sausage - £1.80", var=chk_state3)
chk3.grid(column=0, row=8, sticky="W")

btn = Button(window, text="Price", command=clicked)
btn.grid(column=0, row=9, sticky="W", padx=5, pady=5)

txt_output = StringVar()

txt = Entry(window, width=30, textvariable=txt_output, state="readonly")
txt.grid(column=0, row=10, sticky="W", padx=5, pady=5)

window.mainloop()
