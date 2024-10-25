from tkinter import *


def clicked():
    description = "..."
    pizza_price = 0
    print(f"Pizza chosen is {description}")
    txt_output.set(f"Pizza price is £{pizza_price:.2f}")


window = Tk()
window.geometry("250x400")
window.title("Python pizzas")

row_counter = 0

lbl0 = Label(window, text="Pizzas", font=("Arial Bold", 20))
lbl0.grid(column=0, row=row_counter, sticky="W")
row_counter += 1

selected = IntVar()
selected.set(0)

pizzas = ["margherita", "napoletana", "marinara"]
pizza_prices = [6.0, 7.0, 7.5]
for i in range(len(pizzas)):
    rad = Radiobutton(window, text=f"{pizzas[i]} - £{pizza_prices[i]:.2f}", value=i, variable=selected)
    rad.grid(column=0, row=row_counter, sticky="W")
    row_counter += 1

lbl1 = Label(window, text="Extras", font=("Arial Bold", 20))
lbl1.grid(column=0, row=row_counter, sticky="W")
row_counter += 1

extras = ["mushrooms", "cheese", "anchovies", "sausage"]
extra_prices = [0.5, 1.0, 1.5, 1.8]
extra_chosen = []
for i in range(len(extras)):
    extra_chosen.append(BooleanVar())
    chk = Checkbutton(window, text=f"{extras[i]} - £{extra_prices[i]:.2f}", var=extra_chosen[i])
    chk.grid(column=0, row=row_counter, sticky="W")
    row_counter += 1

btn = Button(window, text="Price", command=clicked)
btn.grid(column=0, row=row_counter, sticky="W", padx=5, pady=5)
row_counter += 1

txt_output = StringVar()

txt = Entry(window, width=30, textvariable=txt_output, state="readonly")
txt.grid(column=0, row=row_counter, sticky="W", padx=5, pady=5)
row_counter += 1

window.mainloop()
