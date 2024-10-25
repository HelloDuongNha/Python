class Employee:
    def __init__(self, id, name, rate):
        self.id = id
        self.name = name
        self.rate = rate
    
    @property
    def id(self):
        return self.__id 
    
    @id.setter
    def id(self, value):
        if value <= 0:
            raise ValueError('Employee ID must be positive')
        self.__id = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__name = value

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, value):
        if value <= 0:
            raise ValueError('Rate must be positive')
        self.__rate = value

    def show(self):
        print(f'| Employee ID: {self.id:3} | Employee name {self.name:10} | Employee rate: {self.rate:3} |')