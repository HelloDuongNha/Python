from tkinter import *
from tkinter import messagebox as msb

window = Tk()
window.title('Payment')
window.geometry("1080x720")

#handlers
def btn_ok_clicked():
    try:
        price = int(txt_price.get())
        quantity = int(txt_quantity.get())
        paymnent = f'{price * quantity}$'
        lbl_total.config(text = paymnent)
    except ValueError:
        msb.showerror("error, please enter numbers for price & quantity")

#main
lbl_product = Label(window, text= "product:")
lbl_product.grid(row=0, column=0)

txt_product = Entry(window)
txt_product.grid(row=0, column=1)


lbl_price = Label(window, text= "price:")
lbl_price.grid(row=1, column=0)

txt_price = Entry(window)
txt_price.grid(row=1, column=1)


lbl_quantity = Label(window, text= "quantity:")
lbl_quantity.grid(row=2, column=0)

txt_quantity = Entry(window)
txt_quantity.grid(row=2, column=1)

btn_ok = Button(window, text="ok", command=btn_ok_clicked)
btn_ok.grid(row=3, column=1, sticky=W)

lbl_payment = Label(window, text= "payment:")
lbl_payment.grid(row=4, column=0)

lbl_total = Label(window,text= "0$")
lbl_total.grid(row=4, column=1, sticky=W)



window.mainloop()

