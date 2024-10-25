class Item:
    def __init__(self, item_id, name, brand, price):
        self.__item_id = item_id
        self.name = name
        self.brand = brand
        self.price = price
    
    @property
    def item_id(self):
        return self.__item_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def price(self):
        return self.__price
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name = name
    
    @brand.setter
    def brand(self, brand):
        if not brand:
            raise ValueError("Brand cannot be empty")
        self.__brand = brand
    
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price