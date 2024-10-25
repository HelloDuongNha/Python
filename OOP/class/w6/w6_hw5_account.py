class Account:
    # static attribute
    __id = 0
    def __init__(self, name, balance):
        self.name = name
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self.__balance = balance
        self.__id = Account.__id    # set instance attribute to static attribute
        Account.__id += 1           # increment static attribute by 1
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def balance(self):
        return self.__balance
    
    def _set_balance(self, balance):
        self.__balance = balance
    
    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError('Name cannot be empty')
        self.__name = name

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError('Insufficient balance')
        if amount <= 0:
            raise ValueError('Amount must be positive')
        self.__balance -= amount
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        self.__balance += amount
    
    def show(self):
        print(f'Account ID: {self.id}')
        print(f'Account name: {self.name}')
        print(f'Account balance: {self.balance}')