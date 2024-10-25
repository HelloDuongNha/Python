from tkinter import *

window = Tk()
window.title("Ticket Booking App")
window.geometry("300x500")

#handlers
def calculate():
    extra_value = 0
    from_value = from_var.get().upper()
    to_value = to_var.get().upper()
    price_value = int(txt_price.get())
    bassage_value = int(txt_bassage.get())
    seat_value = seat_var.get()
    dinner_value = dinner_var.get()

    total_value = price_value
    if seat_value:
        total_value += 5
        extra_value += 5
    if dinner_value:
        total_value += 10
        extra_value += 10

    if bassage_value > 7:
        total_value += (bassage_value - 7) * 5

    info = f"Ticket information: from {from_value} to {to_value} (${price_value})"
    if bassage_value > 7:
        info += f"\nOverweight: {bassage_value - 7}kg ($5/kg)"
    else:
        info += f"\nOverweight: 0kg ($5/kg)"
    info += f"\nExtra: ${extra_value}"
    info += f"\nTotal: ${total_value}"
    Label(window, text=info).grid(row=7, column=0, columnspan=2, sticky=W)


#main
from_var =StringVar()
Label(window, text="From:").grid(row=0, column=0, sticky=W)
Entry(window, textvariable=from_var).grid(row=0, column=1, sticky=E)

to_var = StringVar()
Label(window, text="To:").grid(row=1, column=0, sticky=W)
Entry(window, textvariable=to_var).grid(row=1, column=1, sticky=E)

Label(window, text="Price:").grid(row=2, column=0, sticky=W)
txt_price = Entry(window)
txt_price.grid(row=2, column=1, sticky=E)
Label(window, text="$").grid(row=2, column=3, sticky=W)

Label(window, text="Bassage (max 7):").grid(row=3, column=0, sticky=W)
txt_bassage = Entry(window)
txt_bassage.grid(row=3, column=1, sticky=E)
Label(window, text="KG").grid(row=3, column=3, sticky=W)

seat_var = BooleanVar()
dinner_var = BooleanVar()
Label(window, text="extra:").grid(row=4, column=0, sticky=W)
Checkbutton(window, text="Select seat ($5)", variable=seat_var).grid(row=4, column=1, sticky=W)
Checkbutton(window, text="Dinner ($10)", variable=dinner_var).grid(row=5, column=1, sticky=W)

Button(window, text="DONE", command=calculate).grid(row=6, column=1, sticky= W)

window.mainloop()
