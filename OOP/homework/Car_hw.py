class Car:
    def __init__(self, id, brand, price, miles):
        self.id = id
        self.brand = brand
        self.price = price
        self.miles = miles

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value <= 0:
            raise ValueError('ID must be positive')
        self.__id = value

    @property
    def brand(self):    
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value == '':
            raise ValueError('brand cannot be empty')
        self.__brand = value


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be a positive number")
        self.__price = value

    @property
    def miles(self):
        return self.__miles

    @miles.setter
    def miles(self, value):
        if value < 0:
            raise ValueError("Miles must be a non-negative number")
        self.__miles = value

    def show(self):
        print(f'| Car {self.brand:7}: {self.price:7}$ | miles: {self.miles:7} |')
