from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name            # call setter method to set name attribute
        self._shape_type = 'shape'  # protected attribute
    @property
    def name(self):
        return self.__name          # private attribute
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError('name cannot be empty')
        self.__name = name

    # area() is abstract method because we don't know how to calculate area of a general shape
    @abstractmethod
    def area(self):
        pass

    # override __str__ method to return string representationg of the object
    def __str__(self):
        return f'{self.__name} is a {self._shape_type} with area {self.area()}'