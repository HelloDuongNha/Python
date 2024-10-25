from w6_hw5_account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.__accounts = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError('Name cannot be empty')
        self.__name = name

    
    def add(self, acc):
        self.__accounts.append(acc)

    def remove(self, id):
        acc = self.__search(id)
        if not acc:
            raise ValueError(f'Account ID {id} not found')
        
    def withdraw(self, id, amount):
        acc = self.__search(id)
        if not acc:
            raise ValueError(f'Account ID {id} not found')
        acc.withdraw(amount)

    def deposit(self, id, amount):
        acc = self.__search(id)
        if not acc:
            raise ValueError(f'Account ID {id} not found')
        acc.deposit(amount)

    def show(self, id):
        acc = self.__search(id)
        if not acc:
            raise ValueError(f'Account ID {id} not found')
        acc.show()

    def __search(self, id):
        for acc in self.__accounts:
            if acc.id == id:
                return acc
        return None
    
    def show_all(self):
        for acc in self.__accounts:
            acc.show()
