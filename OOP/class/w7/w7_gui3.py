from tkinter import *

class ComputerStore:
    def __init__(self):
        self.window = self.create_window()
        self.create_widgets()

    def create_window(self):
        self.window = Tk()
        self.window.title("computer store")
        self.window.geometry('300x300')
        return self.window
    
    def create_widgets(self):
        self.lbl_store = Label(self.window, text="computer store")
        self.lbl_store.grid(column=0, row=0)
        self.lbl_select = Label(self.window, text="Select a product: ")
        self.lbl_select.grid(column=0, row=1, sticky=W)

        self.computer_price = IntVar()
        self.pro_13 = Radiobutton(self.window, text= "MacBook Pro 13 ($2000)", value = 2000, variable= self.computer_price, command=self.calculate_price)
        self.pro_13.grid(column=0, row=2, sticky=W)
        self.air_13 = Radiobutton(self.window, text= "MacBook Air 13 ($1500)", value = 1500, variable= self.computer_price, command=self.calculate_price)
        self.air_13.grid(column=0, row=3, sticky=W)
        self.pro_15 = Radiobutton(self.window, text= "MacBook Pro 15 ($2500)", value = 2500, variable= self.computer_price, command=self.calculate_price)
        self.pro_15.grid(column=0, row=4, sticky=W)

        self.lbl_select = Label(self.window, text="Select an option: ")
        self.lbl_select.grid(column=0, row=5, sticky=W)

        self.cover_var = BooleanVar()
        self.chk_cover = Checkbutton(self.window, text= "Cover ($10)", variable= self.cover_var, command=self.calculate_price)
        self.chk_cover.grid(column=0, row=6, sticky=W)

        self.case_var = BooleanVar()
        self.chk_case = Checkbutton(self.window, text= "Case ($15)", variable= self.case_var, command=self.calculate_price)
        self.chk_case.grid(column=0, row=7, sticky=W)

        self.lbl_price = Label(self.window, text="total price")
        self.lbl_price.grid(column=0, row=8)

        self.total_price = IntVar()
        self.txt_price = Entry(self.window, width=20, state="readonly", textvariable=self.total_price)
        self.txt_price.grid(column=0, row=9, sticky=W)
        
    def calculate_price(self):
        price = self.computer_price.get()
        if self.cover_var.get():
            price += 10
        if self.case_var.get():
            price += 20
        self.total_price.set(price)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    win = ComputerStore()
    win.run()