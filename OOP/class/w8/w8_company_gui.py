from tkinter import *
from tkinter import messagebox as msb
from tkinter import filedialog
import csv
from w8_employee import Employee

class CompanyGUI:
    def __init__(self):
        self.create_window()
        self.create_widget()
        self.__employees = []

    def create_window(self):
        self.window = Tk()
        self.window.geometry('650x350')
        self.window.title('gui example')
    
    def create_widget(self):
        Label(self.window, text="FPT Company Employees").grid(row=0, column=0, columnspan=6)

        self.create_list_box()
        self.create_info_widget()
        self.create_navigation_button()

    def create_list_box(self):
        Button(self.window, text='load', command=self.load_employees).grid(row=1, column=0, sticky=W, padx=5, pady=5)

        # selectmode: choose 1 item only
        # exportselection: keep item selected even when listbox loses focus

        self.lst_employees = Listbox(self.window, width=50, height=10, selectmode=SINGLE, exportselection=False)
        self.lst_employees.grid(row=2, column=0, rowspan=4, padx=5, pady=5)
        self.lst_employees.bind('<<ListboxSelect>>', self.show_employees_info)

    def show_employees_info(self, event):
        selected_index = self.lst_employees.curselection()[0]
        selected_employee = self.__employees[selected_index]
        self.update_entry(self.txt_id, selected_employee.id)
        self.update_entry(self.txt_name, selected_employee.name)
        self.update_entry(self.txt_rate, selected_employee.rate)

    def update_entry(self, entry, value):
        entry.delete(0, END)
        entry.insert(0, value)

    def load_employees(self):
        file_name = filedialog.askopenfilename(filetypes=[("CSV files", "*.CSV"),
                                                            ("All files", "*.*")])
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader: 
                id = int(row[0])
                name = row[1]
                rate = float(row[2])
                self.__employees.append(Employee(id, name, rate))
                self.lst_employees.insert(END, name)

        # set the first employee as the default selected item
        self.lst_employees.selection_set(0)
        self.show_employees_info(None)


    def create_info_widget(self):
        Label(self.window, text="Search").grid(row=1, column=1, sticky=E+N, padx=5, pady=5)
        self.txt_search = Entry(self.window, width=25)
        self.txt_search.grid(row=1, column=2, padx=5, pady=5, columnspan=4, sticky=W+N)
        self.txt_search.bind("<Return>", self.search_employees)

        Label(self.window, text="ID").grid(row=2, column=1, sticky=E+N, padx=5, pady=5)
        self.txt_id = Entry(self.window, width=25)
        self.txt_id.grid(row=2, column=2, padx=5, pady=5, columnspan=4, sticky=W+N)

        Label(self.window, text="Name").grid(row=3, column=1, sticky=E+N, padx=5, pady=5)
        self.txt_name = Entry(self.window, width=25)
        self.txt_name.grid(row=3, column=2, padx=5, pady=5, columnspan=4, sticky=W+N)

        Label(self.window, text="Rate").grid(row=4, column=1, sticky=E+N, padx=5, pady=5)
        self.txt_rate = Entry(self.window, width=25)
        self.txt_rate.grid(row=4, column=2, padx=5, pady=5, columnspan=4, sticky=W+N)

    def create_navigation_button(self):
        Button(self.window, text="| <", command= self.move_first).grid(row=5, column=2, padx=5, pady=5)
        Button(self.window, text="<<", command= self.move_previous).grid(row=5, column=3, padx=5, pady=5)
        Button(self.window, text=">>", command= self.move_next).grid(row=5, column=4, padx=5, pady=5)
        Button(self.window, text="> |", command= self.move_last).grid(row=5, column=5, padx=5, pady=5)
        Button(self.window, text="Exit", command= self.window.quit).grid(row=6, column=5, padx=5, pady=5)

    def move_first(self):
        self.lst_employees.selection_clear(0, END)
        self.lst_employees.selection_set(0)
        self.lst_employees.event_generate('<<ListboxSelect>>')

    def move_previous(self):
        selected_index = self.lst_employees.curselection()[0]
        if selected_index == 0:
            msb.showinfo("Information", "This is the first employee")
        else:
            self.lst_employees.selection_clear(0, END)
            self.lst_employees.selection_set(selected_index - 1)
            self.lst_employees.event_generate('<<ListboxSelect>>')

    def move_next(self):
        selected_index = self.lst_employees.curselection()[0]
        if selected_index == len(self.__employees) - 1:
            msb.showinfo("Information", "This is the last employee")
        else:
            self.lst_employees.selection_clear(0, END)
            self.lst_employees.selection_set(selected_index + 1)
            self.lst_employees.event_generate('<<ListboxSelect>>')

    def move_last(self):
        self.lst_employees.selection_clear(0, END)
        self.lst_employees.selection_set(len(self.__employees) - 1)
        self.lst_employees.event_generate('<<ListboxSelect>>')

    def search_employees(self, event):
        name = self.txt_search.get()
        found = False
        for i in range(len(self.__employees)):
            if name.lower() in self.__employees[i].name.lower():
                self.lst_employees.selection_clear(0, END)
                self.lst_employees.select_set(i)
                self.show_employees_info(None)
                msb.showinfo("information", "employee found")
                found = True
                break
        if not found:
            msb.showinfo("information", "employee not found")


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    company = CompanyGUI()
    company.run()