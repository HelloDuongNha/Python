l_product = {}

def print_product():
    for name, price in l_product.items():
        print(f"name: {name}, price: {price}")

def add_product():
    name = input("Enter the product name: ")
    price = input("Enter the product price: ")
    if name in l_product:
        print("product already exists")
    else:
        l_product[name] = price
        print("product added")

def edit_product():
    name = input('Enter the product name to edit: ')
    price = input('Enter new price: ')
    if name not in l_product:
        print('product does not exist')
    else:
        l_product[name] = price
        print('product updated')

def del_product():
    name = input('Enter the product name to delete: ')
    if name not in l_product:
        print('product does not exist')
    else:
        del l_product[name]
        print('product deleted')

### Main ###
running = True
while running:
    print('1. Print product')
    print('2. Add product')
    print('3. Edit product')
    print('4. Delete product')
    print('5. Quit')
    choice = input('Enter your choice: ')
    if choice == '1':
        print_product()
    elif choice == '2':
        add_product()
    elif choice == '3':
        edit_product()
    elif choice == '4':
        del_product()
    elif choice == '5':
        running = False
    else:
        print('Invalid choice')
    print()