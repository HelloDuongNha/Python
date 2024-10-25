from w6_hw5_account import Account
from w6_debit_account import DebitAccount
from w6_hw5_bank import Bank

class BankManager:
    def __init__(self, name):
        self.__bank = Bank(name)
    
    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:     self.__add_account()
            elif choice == 2:   self.__remove_account()
            elif choice == 3:   self.__withdraw()
            elif choice == 4:   self.__deposit()
            elif choice == 5:   self.__show()
            elif choice == 6:   self.__show_all()
            elif choice == 0:   running = False
            else:               print('Invalid choice')
    
    def __print_menu(self):
        print('1. Add account')
        print('2. Remove account')
        print('3. Withdraw')
        print('4. Deposit')
        print('5. Show')
        print('6. Show all')
        print('0. Quit')

    def __add_account(self):
        try:
            name = input('Enter account name: ')
            balance = float(input('Enter account balance: '))

            acc_type = int(input('choose account type: 1: normal | 2: debit'))
            if acc_type not in [1, 2]:
                raise ValueError('invalid account type')
            elif acc_type == 1:
                acc = Account(name, balance)
            else:
                limit = float(input('enter debit limit: '))
                acc = DebitAccount(name, balance, limit)
            
            self.__bank.add(acc)
            print('Account added')
        except ValueError as e:
            print('Error:', e)

    def __remove_account(self):
        try:
            id = int(input('Enter account ID: '))
            self.__bank.remove(id)
            print('Account removed')
        except ValueError as e:
            print('Error:', e)
    
    def __withdraw(self):
        try:
            id = int(input('Enter account ID: '))
            amount = float(input('Enter amount to withdraw: '))
            self.__bank.withdraw(id, amount)
            print('Withdrawal successful')
        except ValueError as e:
            print('Error:', e)

    def __deposit(self):
        try:
            id = int(input('Enter account ID: '))
            amount = float(input('Enter amount to deposit: '))
            self.__bank.deposit(id, amount)
            print('Deposit successful')
        except ValueError as e:
            print('Error:', e)
    
    def __show(self):
        try:
            id = int(input('Enter account ID: '))
            self.__bank.show(id)
        except ValueError as e:
            print('Error:', e)

    def __show_all(self):
        self.__bank.show_all()

if __name__ == '__main__':
    name = input('Enter bank name: ')
    manager = BankManager(name)
    manager.run()