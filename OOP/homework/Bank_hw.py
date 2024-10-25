from Account_hw import Account
class Bank:
    def __init__(self, name):
        self.name = name
        self.__accounts = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Bank name cannot be empty")
        self.__name = name

    def add(self, account):
        if not isinstance(account, Account):
            raise ValueError('Invalid account object')
        self.__accounts.append(account)

    def remove(self, id):
        account = self.__search(id)
        if account is None:
            raise ValueError(f"Account not found for id {id}")
        self.__accounts.remove(account)

    def __search(self, id):
        for account in self.__accounts:
            if account.id == id:
                return account
        return None

    def withdraw(self, id, amount):
        account = self.__search(id)
        if account is None:
            raise ValueError(f"Account not found for id {id}")
        account.withdraw(amount)

    def deposit(self, id, amount):
        account = self.__search(id)
        if account is None:
            raise ValueError(f"Account not found for id {id}")
        account.deposit(amount)

    def show_account(self, id):
        account = self.__search(id)
        if account is None:
            print(f'Account not found for id {id}')
        else:
            account.show()

    def show_all(self):
        print(f' ****** BANK {self.name} ****** ')
        for account in self.__accounts:
            account.show()

    def search(self, id):
        return self.__search(id)