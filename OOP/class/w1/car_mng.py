cars = {1: ['Honda', 'Civic', 10000, 0],
        2: ['Toyota', 'Lexus', 50000, 10000],
        3: ['Honda', 'CX5', 15000, 200],
        4: ['Hyunda', 'Kona', 8000, 500]}


def print_menu():
    print('Welcome to Car Showroom')
    print('1. Show all cars')
    print('2. Search by brand')
    print('3. Search by price')
    print('4. Search by miles')
    print('5. Add new car')
    print('6. Edit car')
    print('7. Delete car')


def print_car(car_id, car_info):
    print(f'{car_id} {car_info[0]} {car_info[1]} ${car_info[2]}, ODO {car_info[3]} miles\n')


def show_all():
    print('\n*****cars list*****\n')
    for car_id, car_info in cars.items():
        print_car(car_id, car_info)


def search_brand():
    brand = input('Enter a brand to search: ')

    for car_id, car_info in cars.items():
        if brand.lower() == car_info[0].lower(): 
            print_car(car_id, car_info)


def search_price():
    price = int(input('Enter a price to search: '))
    count = 0

    for car_id, car_info in cars.items():
        if car_info[2] >= price: 
            print_car(car_id, car_info)
            count += 1

    if count == 0:
        print(f'No car has price >= {price}')


def search_miles():
    miles = int(input('Enter a miles to search: '))
    count = 0

    for car_id, car_info in cars.items():
        if car_info[3] <= miles: 
            print_car(car_id, car_info)
            count += 1
    if count == 0:
        print(f'No car has miles <= {miles}')

def add_car():
    id = int(input("Enter ID: "))

    if id in cars:
        print(f'Car id {id} existed! please enter a new id')
        return
    
    brand = str(input('Enter brand: '))
    model = str(input('Enter model: '))
    price = int(input('Enter price: '))
    miles = 0
    cars.update({id:[brand, model, price, miles]})
    print('new car added\n')

def edit_car():
    car_id = int(input("Enter old car id to edit: "))
    if car_id not in cars:
        print(f'Car id {id}not existed! please enter a new id')
        return
    
    car_info = cars[car_id]
    car_info[2] = int(input('Enter new price: '))
    car_info[3] = int(input('Enter new miles: '))
    print(f'Car {car_id} updated')

def delete_car():
    car_id = int(input("Enter old car id to delete: "))
    if car_id not in cars:
        print(f'Car id {id}not existed! please enter a new id')
        return
    
    cars.pop(car_id)
    print(f'Car {car_id} is deleted!')


def run():
    running = True 
    while running: 
        print_menu()
        choice = int(input('Enter your choice: '))
        if   choice == 1:   show_all()
        elif choice == 2:   search_brand()
        elif choice == 3:   search_price()
        elif choice == 4:   search_miles()
        elif choice == 5:   add_car()
        elif choice == 6:   edit_car()
        elif choice == 7:   delete_car()
        elif choice == 0:   running = False
        else: print('invalid value')

run()
