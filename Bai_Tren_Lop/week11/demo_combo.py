from tkinter import *
from tkinter.ttk import *

#### 1. CREATE THE WINDOW ####
window = Tk()
window.title("Combo Box Demo")
window.geometry('300x200')

#### 2. EVENT HANDLERS ####
def cbb_bg_color_selected(event):
    bg_color = cbb_bg_color.get()   # get the selected item
    window.configure(bg=bg_color)   # set the background color

#### 3. WIDGETS ####
lbl_choose_bg = Label(window, text="Choose a background color:")
lbl_choose_bg.grid(row=0, column=0)

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
cbb_bg_color = Combobox(window, width=10, state='readonly')
cbb_bg_color.bind('<<ComboboxSelected>>', cbb_bg_color_selected)

cbb_bg_color['values'] = colors     #set the values of the combo box
cbb_bg_color.current(0)             #set the selected item is the 1st item
cbb_bg_color.grid(row=0, column=1)

#### 4. RUN THE MAIN LOOP ####
window.mainloop()