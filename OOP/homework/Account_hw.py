class Account:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def __id(self, value):
        if value <= 0:
            raise ValueError('Account ID must be positive')
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
    def balance(self):
        return self.__balance
    
    @balance.setter
    def __balance(self, value):
        if value < 0:
            raise ValueError('Balance must be non-negative')
        self.__balance = value

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive')
        if amount > self.balance:
            raise ValueError('Insufficient balance')
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount

    def show(self):
        print(f'| Account ID: {self.id:3} | Account Name: {self.name:10} | Balance: ${self.balance:10.2f} |')