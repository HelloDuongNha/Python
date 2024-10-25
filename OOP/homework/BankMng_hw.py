from Bank_hw import Bank
from Account_hw import Account

class BankManagementProgram:
    def __init__(self, name):
        self.__bank = Bank(name)

    def __print_menu(self):
        print('Welcome to Bank Management Program')
        print('1. Show all accounts')
        print('2. Search account by ID')
        print('3. Add new account')
        print('4. Withdraw from account')
        print('5. Deposit to account')
        print('6. Remove account')
        print('7. Exit')

    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.__bank.show_all()
            elif choice == 2:
                self.__search_account()
            elif choice == 3:
                self.__add_account()
            elif choice == 4:
                self.__withdraw()
            elif choice == 5:
                self.__deposit()
            elif choice == 6:
                self.__remove_account()
            elif choice == 7:
                running = False
            else:
                print('Invalid choice. Please try again.')

    def __search_account(self):
        id = int(input('Enter account ID to search: '))
        self.__bank.show_account(id)

    def __add_account(self):
        id = int(input('Enter account ID: '))
        name = input('Enter account name: ')
        balance = float(input('Enter initial balance: '))
        try:
            account = Account(id, name, balance)
            self.__bank.add(account)
            print('Account added successfully.')
        except ValueError as e:
            print(e)

    def __withdraw(self):
        id = int(input('Enter account ID to withdraw from: '))
        amount = float(input('Enter amount to withdraw: '))
        try:
            self.__bank.withdraw(id, amount)
            print('Amount withdrawn successfully.')
        except ValueError as e:
            print(e)

    def __deposit(self):
        id = int(input('Enter account ID to deposit to: '))
        amount = float(input('Enter amount to deposit: '))
        try:
            self.__bank.deposit(id, amount)
            print('Amount deposited successfully.')
        except ValueError as e:
            print(e)

    def __remove_account(self):
        id = int(input('Enter account ID to remove: '))
        try:
            self.__bank.remove(id)
            print('Account removed successfully.')
        except ValueError as e:
            print(e)


# To run the program
if __name__ == "__main__":
    bank_management = BankManagementProgram("My Bank")
    bank_management.run()