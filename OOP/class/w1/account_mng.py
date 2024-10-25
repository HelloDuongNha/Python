list_ids = [1, 2, 3]
list_names = ['a', 'b', 'c']
list_balance = [10000, 20000, 30000]

def run():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_account()
        elif choice == 2:
            with_draw()
        elif choice == 3:
            delete_account()
        elif choice == 4:
            search_account()
        elif choice == 5:
            show_debit()
        elif choice == 0:
            print('thank you for using Account Management Appliation')
            running = False
        else:
            print('invalid value')


def print_menu():
    print('selection 0: exit')
    print('selection 1: Add the new account')
    print('selection 2: With draw money')
    print('selection 3: Delete the account')
    print('selection 4: Search account by ID')
    print('selection 5: Show debit account')

def check_id(id):
    for i in range(len(list_ids)):
        if list_ids[i] == id:
            return i
    return -1

def add_account():
    id = int(input('enter an ID: '))
    if check_id(id) == -1:
        name = input('enter an account name: ')
        balance = int(input('enter a balance: '))
        list_ids.append(id)
        list_names.append(name)
        list_balance.append(balance)
        print(f'account {name} added successfully')
    else:
        print('invalid ID')

def with_draw():
    id = int(input('enter ID: '))
    for i in range(len(list_ids)):
        if

run()