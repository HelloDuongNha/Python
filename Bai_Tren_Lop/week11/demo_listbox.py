from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msb

#### 1. CREATE THE WINDOW ####
window = Tk()
window.title("Combo Box Demo")
window.geometry('350x200')

#### 2. EVENT HANDLERS ####
def lst_employees_selected(event):
    # get selected index from the listbox
    selected_index = lst_employees.curselection()[0]
    # get employee name from the list
    employee_name = employees[selected_index]
    set_text(txt_name, employee_name)

def set_text(txt_ui, text):
    txt_ui.delete(0, END)
    txt_ui.insert(0, text)

def btn_add_clicked():
    name = txt_name.get()
    employees.append(name)          # add the name to the list employes
    lst_employees.insert(END, name) # add the name to the listbox lst_employees

def btn_edit_clicked():
    try:
        selected_index = lst_employees.curselection()[0]
        name = txt_name.get()
        # update the list employees
        employees[selected_index] = name        
        # update the listbox lst_employees
        lst_employees.delete(selected_index)    # delete the old name
        lst_employees.insert(selected_index, name)  # insert the new name at the same position
    except IndexError:
        msb.showerror("Error", "Please select an employee to edit")

def btn_delete_clicked():
    try:
        selected_index = lst_employees.curselection()[0]
        employees.pop(selected_index)       # remove the name from the list employees
        lst_employees.delete(selected_index)    # remove the name from the listbox lst_employees
    except IndexError:
        msb.showerror("Error", "Please select an employee to delete")

#### 3. WIDGETS ####
lbl_employee = Label(window, text="Employees:")
lbl_employee.grid(row=0, column=0, sticky=W, padx=5, pady=5)

employees = ['John', 'Mary', 'Peter', 'Jane', 'Tom']
lst_employees = Listbox(window, width=10, height=5)
lst_employees.grid(row=1, column=0, rowspan=5, padx=5, pady=5)
lst_employees.insert(END, *employees)
lst_employees.bind('<<ListboxSelect>>', lst_employees_selected)

txt_name = Entry(window, width=25)
txt_name.grid(row=1, column=1, columnspan=3, sticky=W, padx=5, pady=5)

btn_add = Button(window, text="Add", width=3, command=btn_add_clicked)
btn_add.grid(row=2, column=1, sticky=W, padx=5, pady=5)

btn_edit = Button(window, text="Edit", width=3, command=btn_edit_clicked)
btn_edit.grid(row=2, column=2, sticky=W, padx=5, pady=5)

btn_delete = Button(window, text="Delete", width=3, command=btn_delete_clicked)
btn_delete.grid(row=2, column=3, sticky=W, padx=5, pady=5)

#### 4. RUN THE MAIN LOOP ####
window.mainloop()