from w8_shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        self._shape_type = 'Circle'

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError('Radius must be positive')
        self.__radius = radius

    # area() is abstract method because we don't know how to calculate area of a general shape
    def area(self):
        return 3.14 * self.radius **2

    # override __str__ method to return string representationg of the object
    def __str__(self):
        return super().__str__() + f', radius: {self.radius}'
    
if __name__ == '__main__':
    c = Circle('Cir', 5)
    print(c) # print will call method __str__ of Circle class to print