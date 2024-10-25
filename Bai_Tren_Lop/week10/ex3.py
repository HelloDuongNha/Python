from tkinter import *
from tkinter import messagebox as msb

window = Tk()
window.title('pizza order')
window.geometry("1080x720")

#handlers
def calculated_payment():
    total = 0
    if pizza_var.get() == 1:
        total += 10
    elif pizza_var.get() == 2:
        total += 12
    elif pizza_var.get() == 3:
        total += 15

    if cbseafood_checked.get() ==True:
        total += 3
    if cbjambon_checked.get() ==True:
        total += 2
    if cbcheese_checked.get() ==True:
        total += 1
    lbl_payment.config(text=f'payment: {total}$')

#main
lbl_select = Label(window, text="sellect pizza:")
lbl_select.grid(row=0, column=0, sticky=W)

pizza_var = IntVar()
rb_seoul = Radiobutton(window,  text="seoul ($10)", value=1, variable=pizza_var, command= calculated_payment)
rb_seoul.grid(row=1, column=0, sticky=W)

rb_newyork = Radiobutton(window,  text="new york ($12)", value=2, variable=pizza_var, command= calculated_payment)
rb_newyork.grid(row=2, column=0, sticky=W)

rb_paris = Radiobutton(window,  text="paris ($15)", value=3, variable=pizza_var, command= calculated_payment)
rb_paris.grid(row=3, column=0, sticky=W)

lbl_topping = Label(window, text="sellect topping:")
lbl_topping.grid(row=4, column=0, sticky=W)

cbseafood_checked = BooleanVar()
cbseafood = Checkbutton(window, text='seafood ($3)',variable= cbseafood_checked, command= calculated_payment)
cbseafood.grid(row=5, column= 0, sticky=W)

cbjambon_checked = BooleanVar()
jambon = Checkbutton(window, text='jambon ($2)',variable= cbjambon_checked, command= calculated_payment)
jambon.grid(row=6, column= 0, sticky=W)

cbcheese_checked = BooleanVar()
cbcheese = Checkbutton(window, text='Tomato/Cheese ($1)',variable= cbcheese_checked, command= calculated_payment)
cbcheese.grid(row=7, column= 0, sticky=W)

lbl_payment = Label(window, text="payment: $0")
lbl_payment.grid(row=8, column=0, sticky=W)

window.mainloop()

