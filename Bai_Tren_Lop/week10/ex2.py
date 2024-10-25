from tkinter import *
from tkinter import messagebox as msb

#create window
window = Tk()
window.title('Payment')
window.geometry("1080x720")

#event handlers
def btn_ok_clicked():
    total = 0
    if cb_1752_checked.get() ==True:
        total += 300
    if cb_1821_checked.get() ==True:
        total += 300
    if cb_1863_checked.get() ==True:
        total += 300
    lbl_total.config(text=f'{total}$')

#create widgets
lbl_select = Label(window, text="select courses:")
lbl_select.grid(row=0, column=0, sticky=W)

cb_1752_checked = BooleanVar() #creat a boolean variable to bind with the check box
cb_1752 = Checkbutton(window, text="1752", variable= cb_1752_checked)
cb_1752.grid(row=0, column=1)

cb_1821_checked = BooleanVar()
cb_1821 = Checkbutton(window, text="1821", variable= cb_1821_checked)
cb_1821.grid(row=1, column=1)

cb_1863_checked = BooleanVar()
cb_1863 = Checkbutton(window, text="1863", variable= cb_1863_checked)
cb_1863.grid(row=2, column=1)

btn_ok = Button(window, text="ok", command=btn_ok_clicked)
btn_ok.grid(row=3, column=1, sticky=W)

lbl_payment = Label(window, text= "payment:")
lbl_payment.grid(row=4, column=0)

lbl_total = Label(window,text= "0$")
lbl_total.grid(row=4, column=1, sticky=W)
lbl_total = Label(window,text= "0$")
lbl_total.grid(row=4, column=1, sticky=W)


#run
window.mainloop()