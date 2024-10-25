from w6_hw5_account import Account
class DebitAccount(Account):
    def __init__(self, name, balance, limit):
        self.limit = limit
        super().__init__(name, balance)
        

    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, limit):
        if limit < 0:
            raise ValueError('limit cannot be negative')
        self.__limit = limit
    
    def withdraw(self, amount):
        if abs(self.balance - amount) > self.limit :
            raise ValueError('Insufficient limit')
        if amount <= 0:
            raise ValueError('Amount must be positive')
        # self._Account__balance -= amount
        self._set_balance(self.balance - amount)

    def show(self):
        super().show()
        print(f'Account limit: {self.limit}\n')

# Test the DebitAccount class

def test_debit_account():
    # Create a DebitAccount instance
    try:
        account = DebitAccount('Alice', 1000, 500)
        print('Account created successfully.')
    except ValueError as e:
        print(f'Failed to create account: {e}')
    
    # Test show method
    print('\nInitial account details:')
    account.show()
    
    # Test deposit method
    try:
        account.deposit(500)
        print('\nDeposited 500 successfully.')
    except ValueError as e:
        print(f'Failed to deposit: {e}')
    
    # Test show method after deposit
    print('\nAccount details after deposit:')
    account.show()
    
    # Test withdraw method within limit
    try:
        account.withdraw(1200)
        print('\nWithdrew 1200 successfully.')
    except ValueError as e:
        print(f'Failed to withdraw: {e}')
    
    # Test show method after withdrawal within limit
    print('\nAccount details after withdrawal within limit:')
    account.show()
    
    # Test withdraw method exceeding limit
    try:
        account.withdraw(400)
        print('\nWithdrew 400 successfully.')
    except ValueError as e:
        print(f'Failed to withdraw: {e}')
    
    # Test show method after withdrawal exceeding limit
    print('\nAccount details after withdrawal exceeding limit:')
    account.show()
    
    # Test setting negative limit
    try:
        account.limit = -100
        print('\nLimit set to -100 successfully.')
    except ValueError as e:
        print(f'Failed to set limit: {e}')
    
    # Test setting valid limit
    try:
        account.limit = 1000
        print('\nLimit set to 1000 successfully.')
    except ValueError as e:
        print(f'Failed to set limit: {e}')
    
    # Test show method after setting limit
    print('\nAccount details after setting limit:')
    account.show()

# Run the test
# test_debit_account()
