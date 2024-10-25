from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

class BookStore:
    def __init__(self):
        self.window = self.create_window()
        self.create_widgets()

    def create_window(self):
        self.window = Tk()
        self.window.geometry("350x250")
        self.window.title("Book Store")
        return self.window

    def create_widgets(self):
        # book
        self.book_input = StringVar(self.window)
        Label(self.window, text='Book', ).grid(row=0, column=0)
        Entry(self.window, textvariable=self.book_input ,width=30).grid(row=0, column=1, columnspan=2, sticky=W, padx=5)

        # price
        self.price_input = StringVar(self.window)
        Label(self.window, text='Price').grid(row=1, column=0)
        Entry(self.window, textvariable=self.price_input, width=30).grid(row=1, column=1, columnspan=2, sticky=W, padx=5)

        # quantity
        self.quantity_input = StringVar(self.window)
        Label(self.window, text='Quantity').grid(row=2, column=0)
        Entry(self.window, width=30, textvariable= self.quantity_input).grid(row=2, column=1, columnspan=2, sticky=W, padx=5)

        # extra choices
        Label(self.window, text='Extra').grid(row=3, column=0)
        # extra cover
        self.cover_var =  BooleanVar(self.window)
        Checkbutton(self.window, text= "Cover ($1)", variable= self.cover_var).grid(row=3, column=1, sticky=W)
        # extra card
        self.card_var =  BooleanVar(self.window)
        Checkbutton(self.window, text= "Card ($1.5)", variable= self.card_var).grid(row=3, column=2)

        # delivery
        Label(self.window, text='Delivery').grid(row=4, column=0)
        self.delivery_price = IntVar(value=1    )
        Radiobutton(self.window, text="Normal (Free)", variable=self.delivery_price, value=1).grid(row=4, column=1, sticky=W)
        Radiobutton(self.window, text="Express ($2)", variable=self.delivery_price, value=2).grid(row=5, column=1, sticky=W)
        Radiobutton(self.window, text="Immediate ($5)", variable=self.delivery_price, value=3).grid(row=6, column=1, sticky=W)

        # Payment button
        Button(self.window, text="Payment", command=self.process_payment).grid(row=7, column=1, pady=10)

    def process_payment(self):
        try:
            name = self.book_input.get()
            price_str = self.price_input.get()
            quantity_str = self.quantity_input.get()
            # check bug

            if not name:
                raise ValueError("Book name cannot be empty.")
            if not price_str:
                raise ValueError("Book's price cannot be empty.")
            if not quantity_str:
                raise ValueError("Book's quantity cannot be empty.")

            if not isinstance(name, str):
                raise ValueError("Name must be a string.")

            try:
                price = float(price_str)
            except ValueError:
                raise ValueError("Price must be a number.")

            try:
                quantity = int(quantity_str)
            except ValueError:
                raise ValueError("Quantity must be an integer.")

            if price <= 0:
                raise ValueError("Price must be non-negative.")
            if quantity <= 0:
                raise ValueError("Quantity must be non-negative.")
            
            # Calculate total price
            total_price = price * quantity
            if self.cover_var.get():
                total_price += 1
            if self.card_var.get():
                total_price += 1.5
            if self.delivery_price.get() == 2:
                total_price += 2
            elif self.delivery_price.get() == 3:
                total_price += 5

            messagebox.showinfo("Payment", f"Total price: ${total_price:.2f}")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    win = BookStore()
    win.run()