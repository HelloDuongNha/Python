l_product = []
l_price = []

def print_product():
    for i in range(len(l_product)): 
        print(f"name: {l_product[i]}, price: {l_price[i]}")

def add_product():
    name = input("Enter the product name: ")
    price = input("Enter the product price: ")
    if name in l_product:
        print("product already exists")
    else:
        l_product.append(name)
        l_price.append(price)
        print("product added")

def edit_product():
    name = input('Enter the product name to edit: ')
    price = input('Enter new price: ')
    if name not in l_product:
        print('product does not exist')
    else:
        index = l_product.index(name) 
        l_price[index] = price
        print('product updated')

def del_product():
    name = input('Enter the product name to delete: ')
    if name not in l_product:
        print('product does not exist')
    else:
        index = l_product.index(name) 
        l_product.pop(index) 
        l_price.pop(index)
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