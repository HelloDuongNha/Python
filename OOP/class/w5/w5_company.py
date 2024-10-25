from w5_employee import Employee
class Company:
    def __init__(self, name):
        self.name = name 
        self.__employees = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Company naem cannot be empty")
        self.__name = name

    def add(self, e):
        self.__employees.append(e)

    def remove(self, id):
        e = self.__search(id)
        if e is None:
            raise ValueError(f"Employee not found for id {id}")
        self.__employees.remove(e)

    def __search(self, id):
        for e in self.__employees:
            if e.id == id:
                return e

    def change(self, id, new_rate):
        e = self.__search(id)     #find employee with id
        if e is None:
            raise ValueError(f"Employee not found for id {id}")
        #if found, change rate of employee
        e.rate = new_rate

    def show_employee(self, id):
        e = self.__search(id)
        if e is None:
            print(f'Employee not found for id {id}')
        else:
            e.show()

    def show_all(self):
        for e in self.__employees:
            e.show()
