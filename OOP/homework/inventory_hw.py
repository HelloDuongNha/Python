from item_hw import Item
class Inventory:
    def __init__(self):
        self.__items = []

    def check_id(self, id):
        for i in range(len(self.__items)):
            if self.__items[i].get_id() == id:
                return i
        return -1

    def add_item(self, id, name, price, quantity):
        try:
            id = int(id)
        except ValueError:
            pass  # Allow non-integer IDs
        
        if id == "no id":
            item = Item(id, name, price, quantity)
            self.__items.append(item)
            print("Item added successfully.")
        
        if self.check_id(id) != -1:
            print('This Item ID is already in use, please try again! \n')
            return
        item = Item(id, name, price, quantity)
        self.__items.append(item)
        print("Item added successfully.")

    def remove(self, id):
        index = self.check_id(id)
        if index == -1:
            print('Sorry, item ID not found')
            return
        self.__items.pop(index)
        print("Item removed successfully.")

    def remove_all_invalid_ids(self):
        while True:
            index = self.check_id('no id')
            if index == -1:
                break
            self.__items.pop(index)
        print("All items with ID 'no id' removed successfully.")

    def add_quantity(self, item_id, amount):
        index = self.check_id(item_id)
        if index == -1:
            print(f"Item with ID {item_id} not found.")
            return
        self.__items[index].add_quantity(amount)
        print('Added quantity successfully.')

    def decrease_quantity(self, item_id, amount):
        index = self.check_id(item_id)
        if index == -1:
            print(f"Item with ID {item_id} not found.")
            return
        self.__items[index].decrease_quantity(amount)
        print('Decreased quantity successfully.')

    def most_expensive(self):
        if not self.__items:
            print("No items in inventory.")
            return None
        most_expensive_item = self.__items[0]
        for item in self.__items:
            if item.get_price() > most_expensive_item.get_price():
                most_expensive_item = item
        return most_expensive_item

    def storage(self):
        total_quantity = 0
        for item in self.__items:
            total_quantity += item.get_quantity()
        return total_quantity

    def show_all(self):
        if not self.__items:
            print("Inventory is empty.")
            return
        for item in self.__items:
            item.show_item()

def test_inventory_class():
    print("\n***** Create an Inventory *****\n")
    inventory = Inventory()
    
    # Test add_item with valid and invalid inputs
    print("\n** Test add_item with valid and invalid inputs **\n")
    inventory.add_item(-1, '', 500, 100)
    inventory.add_item(1, 'Item A', 500, 100)
    inventory.add_item(2, 'Item B', 1000, 200)
    inventory.add_item(3, 'Item C', 1500, 300)
    inventory.add_item('no id', 'Invalid Item 1', 0, 0)
    inventory.add_item('no id', 'Invalid Item 2', 0, 0)
    inventory.show_all()

    # Test remove_all_invalid_ids
    print("\n** Test remove_all_invalid_ids **\n")
    inventory.remove_all_invalid_ids()
    inventory.show_all()

    # Test add_quantity with valid and invalid inputs
    print("\n** Test add_quantity with valid and invalid inputs **\n")
    inventory.add_quantity(1, 50)
    inventory.add_quantity(2, -50)  # Invalid
    inventory.add_quantity(3, 1000001)  # Invalid
    inventory.show_all()

    # Test decrease_quantity with valid and invalid inputs
    print("\n** Test decrease_quantity with valid and invalid inputs **\n")
    inventory.decrease_quantity(1, 20)
    inventory.decrease_quantity(2, -20)  # Invalid
    inventory.decrease_quantity(3, 1000)  # Valid
    inventory.decrease_quantity(3, 5000)  # Invalid, more than available quantity
    inventory.show_all()

    # Test most_expensive
    print("\n** Test most_expensive **\n")
    most_expensive_item = inventory.most_expensive()
    if most_expensive_item:
        print("Most expensive item:")
        most_expensive_item.show_item()

    # Test storage
    print("\n** Test storage **\n")
    total_storage = inventory.storage()
    print(f"Total storage: {total_storage}")

    # Test show_all
    print("\n** Test show_all **\n")
    inventory.show_all()

# Run the test
test_inventory_class()