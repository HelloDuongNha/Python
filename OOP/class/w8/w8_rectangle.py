from w8_shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        self._shape_type = 'Rectangle'

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('width must be positive')
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('height must be positive')
        self.__height = height


    # area() is abstract method because we don't know how to calculate area of a general shape
    def area(self):
        return self.width * self.height

    # override __str__ method to return string representationg of the object
    def __str__(self):
        return super().__str__() + f', Dimensions: {self.width} x {self.height}'
    

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)
        self._shape_type = 'Square'

    @property
    def side(self):
        return self.width
    
    @side.setter
    def side(self, value):
        self.width = value
        self.height = value

if __name__ == '__main__':
    d = Rectangle('REC', 5, 10)
    print(d) # print will call method __str__ of Rectangle class to print

    e = Square('Sq', 10)
    print(e) # print will call method __str__ of Square class to print