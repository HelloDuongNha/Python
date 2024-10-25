class Item:
    def __init__(self, id, name, price, quantity):
        # Initialize attributes to default values
        self.__id = 0
        self.__name = ''
        self.__price = 0
        self.__quantity = 0
        
        # Set attributes using setter methods
        self.set_id(id)
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def show_item(self):
        print(f'\n| ID: {self.__id:3} | NAME: {self.__name:10} | PRICE: {self.__price:10} | QUANTITY: {self.__quantity:10} |\n')

    def set_id(self, id):
        try:
            id = int(id)
            if id <= 0:
                print("Invalid ID. ID must be a positive number.")
                self.__id = 'no id'
                return
            self.__id = id
            print('Set up ID successfully ')
        except ValueError:
            print('ID input error.')
            self.__id = 'no id'

    def set_name(self, name):
        if name == '':
            print('Sorry, NAME cannot be empty.')
            self.__name = 'no name'
            return
        self.__name = name
        print('Set up NAME successfully ')

    def set_price(self, price):
        try:
            price = int(price)
            if price <= 0:
                print("Sorry, Price must be positive.")
                self.__price = 0
                return
            self.__price = price
            print('Set up PRICE successfully ')
        except ValueError:
            print('PRICE input error.')
            self.__price = "no price"

    def set_quantity(self, quantity):
        try:
            quantity = int(quantity)
            if quantity <= 0:
                print("Sorry, Quantity must be a positive number.")
                self.__quantity = 0
                return
            self.__quantity = quantity
            print('Set up QUANTITY successfully ')
        except ValueError:
            print('QUANTITY input error.')
            self.__quantity = 'no quantity'

    def add_quantity(self, amount):
        try:
            amount = int(amount)
            quantity = int(self.__quantity)
            if amount <= 0:
                print('sory, amount must be a positive number.')
                return
            if (quantity + amount) > 1000000:
                print('Too many items, warehouse overflow.\n')
                return
            quantity += amount
            self.__quantity = quantity
            print('Added quantity successfully.')
        except ValueError:
            print('Error in adding amount.')

    def decrease_quantity(self, amount):
        try:
            amount = int(amount)
            quantity = int(self.__quantity)
            if amount <= 0:
                print('sory, amount must be a positive number.')
                return
            if (quantity - amount) < 0:
                print('Cannot decrease quantity below zero.')
                return
            quantity -= amount
            self.__quantity = quantity
            print('Decreased quantity successfully.')
        except ValueError:
            print('Error in decreasing amount.')


# def test_item_class():
#     # Create an item
#     print('\n***** create an Item ***** \n')
#     item = Item(1, 'Widget', 10, 100)
#     item.show_item()

#     # Test getters
#     print('***** Get an Item ***** \n')
#     print('ID:', item.get_id())
#     print('Name:', item.get_name())
#     print('Price:', item.get_price())
#     print('Quantity:', item.get_quantity(),'\n')

#     # Test set_name with valid and invalid inputs
#     print('\n** Test set_name with valid and invalid inputs **\n')
#     item.set_name('')
#     item.show_item()
#     item.set_name('Gadget')
#     item.show_item()

#     # Test set_price with valid and invalid inputs
#     print('\n** Test set_price with valid and invalid inputs **\n')
#     item.set_price(-5)
#     item.show_item()
#     item.set_price(20)
#     item.show_item()

#     # Test set_quantity with valid and invalid inputs
#     print('\n** Test set_quantity with valid and invalid inputs **\n')
#     item.set_quantity(-10)
#     item.show_item()
#     item.set_quantity(50)
#     item.show_item()

#     # Test add_quantity with valid and invalid inputs
#     print('\n** Test add_quantity with valid and invalid inputs **\n')
#     item.add_quantity(-50)
#     item.show_item()
#     item.add_quantity(1000001)  
#     item.show_item()
#     item.add_quantity(50)
#     item.show_item()

#     # Test decrease_quantity with valid and invalid inputs
#     print('\n** Test decrease_quantity with valid and invalid inputs **\n')
#     item.decrease_quantity(-20)
#     item.show_item()
#     item.decrease_quantity(1000)  
#     item.show_item()
#     item.decrease_quantity(50)
#     item.show_item()

#     # Test validation inputs
#     print("\n** Test setting up validation **\n")
#     item.set_id("invalid_id")
#     item.set_name('')
#     item.set_price("invalid_price")
#     item.set_quantity("invalid_quantity")

#     print('\n')
#     item.add_quantity("invalid_amount")
#     item.add_quantity(50)
#     item.decrease_quantity("invalid_amount")
#     item.decrease_quantity(50)
#     item.show_item()

# # Run the test
# test_item_class()
