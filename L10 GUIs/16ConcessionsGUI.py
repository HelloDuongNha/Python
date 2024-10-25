from tkinter import *
import tkinter.font as tkfont


window = Tk()
window.geometry("600x350")
window.title("Concessions")


default_font = tkfont.nametofont("TkDefaultFont")


default_font.configure(size=12, family="Arial")


lbl0 = Label(window, text="Concessions", font=("Arial Bold", 20))
lbl0.grid(column=0, row=0, sticky="W")

name_lbl = Label(window, text="Name:", font=("Arial Bold", 12))
name_lbl.grid(column=0, row=1, sticky="W")

name_input_txt = Entry(window, width=30, font=("Arial", 12))
name_input_txt.grid(column=0, row=2, sticky="W", padx=5, pady=5)

student_state = BooleanVar()
student_chk = Checkbutton(window, text="student", font=("Arial Bold", 12), var=student_state)
student_chk.grid(column=0, row=3, sticky="W")

age_lbl = Label(window, text="Age range:", font=("Arial Bold", 12))
age_lbl.grid(column=0, row=4, sticky="W")

selected = IntVar()
selected.set(1)

rad0 = Radiobutton(window, text="0-18", value=0, variable=selected)
rad0.grid(column=0, row=5, sticky="W")
rad1 = Radiobutton(window, text="19-34", value=1, variable=selected)
rad1.grid(column=0, row=6, sticky="W")
rad2 = Radiobutton(window, text="35-64", value=2, variable=selected)
rad2.grid(column=0, row=7, sticky="W")
rad2 = Radiobutton(window, text="65+", value=3, variable=selected)
rad2.grid(column=0, row=8, sticky="W")


def clicked():
    message = f"Hello {name_input_txt.get()}"

    student = student_state.get()
    child_or_senior = selected.get() == 0 or selected.get() == 3

    if student and child_or_senior:
        message += " - congratulations, you are entitled to a 20% discount"
    elif student or child_or_senior:
        message += " - congratulations, you are entitled to a 10% discount"
    else:
        message += " - sorry, you must pay the regular price"
    output.set(message)


btn = Button(window, text="Concession?", command=clicked)
btn.grid(column=0, row=9, sticky="W", padx=5, pady=5)

output = StringVar()

txt = Entry(window, width=60, textvariable=output, state="readonly", font=("Arial", 12))
txt.grid(column=0, row=10, sticky="W", padx=5, pady=5)

window.mainloop()
