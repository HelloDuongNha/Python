from tkinter import *
from tkinter import messagebox as msb

######1. create window ######
window = Tk() #create a window
window.title('first GUI application') #set a title
window.geometry('1080x720') #set a size

######2. event handlers #####
def btn_hello_clicked():
    #get the first name from the text box
    first_name = txt_firstname.get()
    #get the last namee from the text box
    last_name = txt_lastname.get()
    #show a message box with the full name
    full_name = first_name + " " + last_name
    msb.showinfo("full name", full_name)
######3. create widget ######
#create a label on the window with text "first name: "
lbl_firstname = Label(window, text="first name:")
#place the lable on the window at (0, 0) position
lbl_firstname.grid(row=0, column=0)

#create a text box on the window
txt_firstname = Entry(window)
#place the text box on the window at (0, 1) position
txt_firstname.grid(row=0, column=1)

lbl_lastname = Label(window, text="last name:")
lbl_lastname.grid(row=1, column=0)

txt_lastname = Entry(window)
txt_lastname.grid(row=1, column=1)

btn_hello = Button(window, text="hello", command=btn_hello_clicked)
btn_hello.grid(row=2, column=1, sticky=W)
#####4. run the window ######
window.mainloop() #run the window in a main loop, waiting for events