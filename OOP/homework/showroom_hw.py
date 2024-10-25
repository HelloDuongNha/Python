from Car_hw import Car
class Showroom:
    def __init__(self, name):
        self.name = name
        self.__cars = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Showroom name cannot be empty")
        self.__name = name

    def add_car(self, car):
        if car == "":
            raise ValueError("Car name cannot be empty")
        elif not isinstance(car, Car):
            raise ValueError("Invalid car object")
        self.__cars.append(car)

    def remove_car(self, id):
        car = self.__search(id)
        if car is None:
            raise ValueError(f"Car not found for id {id}")
        self.__cars.remove(car)

    def __search(self, id):
        for car in self.__cars:
            if car.id == id:
                return car
        return None

    def change_car(self, id, new_price, new_miles):
        car = self.__search(id)
        if car is None:
            raise ValueError(f"Car not found for id {id}")
        car.price = new_price
        car.miles = new_miles

    def show_car(self, id):
        car = self.__search(id)
        if car is None:
            print(f'Car not found for id {id}')
        else:
            car.show()

    def show_all(self):
        print(f' ****** SHOWROOM {self.name} ****** ')
        for car in self.__cars:
            car.show()

    def search_brand(self, brand):
        count = 0
        for car in self.__cars:
            if brand.lower() == car.brand.lower():
                car.show()
                count += 1
        if count == 0:
            print(f'No car found for brand {brand}')

    def search_miles(self, miles):
        count = 0
        for car in self.__cars:
            if car.miles <= miles:
                car.show()
                count += 1
        if count == 0:
            print(f'No car found for miles {miles}')

    def search_price(self, price):
        count = 0
        for car in self.__cars:
            if car.price >= price:
                car.show()
                count += 1
        if count == 0:
            print(f'No car found for price {price}')

def test_car_class():
    print("Testing Car class...")

    # Test valid car creation
    try:
        car1 = Car(1, "Toyota", 20000, 15000)
        car2 = Car(2, "Honda", 25000, 10000)
        car3 = Car(3, "Ford", 30000, 5000)
        print("Car instances created successfully.")
    except ValueError as e:
        print(f"Failed to create car instances: {e}")

    # Test invalid car creation
    try:
        car_invalid = Car(-1, "", -20000, -5000)
    except ValueError as e:
        print(f"Correctly caught an error for invalid car creation: {e}\n")

def test_showroom_class():
    print("Testing Showroom class...")

    showroom = Showroom("City Motors")

    # Test adding valid cars
    try:
        car1 = Car(1, "Toyota", 20000, 15000)
        car2 = Car(2, "Honda", 25000, 10000)
        showroom.add_car(car1)
        showroom.add_car(car2)
        print("Cars added to showroom successfully.")
    except ValueError as e:
        print(f"Failed to add cars to showroom: {e}")

    # Test adding invalid car
    try:
        showroom.add_car("Not a Car Object")
    except ValueError as e:
        print(f"Correctly caught an error for adding invalid car: {e}")
    try:
        showroom.add_car("")
    except ValueError as e:
        print(f"Correctly caught an error for adding invalid car: {e}")
    # Test displaying all cars
    showroom.show_all()

    # Test searching for a brand
    showroom.search_brand("Toyota")
    showroom.search_brand("Ford")

    # Test searching by miles
    showroom.search_miles(12000)
    showroom.search_miles(5000)

    # Test searching by price
    showroom.search_price(21000)
    showroom.search_price(30000)

    # Test changing car details
    try:
        showroom.change_car(1, 21000, 14000)
        showroom.change_car(2, 26000, 9000)
        print("Car details changed successfully.")
    except ValueError as e:
        print(f"Failed to change car details: {e}")

    # Test displaying specific car
    showroom.show_car(1)
    showroom.show_car(3)

    # Test removing car
    try:
        showroom.remove_car(1)
        print("Car removed successfully.")
    except ValueError as e:
        print(f"Failed to remove car: {e}")

    # Test removing non-existent car
    try:
        showroom.remove_car(3)
    except ValueError as e:
        print(f"Correctly caught an error for removing non-existent car: {e}")

    # Final display of all cars
    showroom.show_all()

# Run the tests
test_car_class()
test_showroom_class()
