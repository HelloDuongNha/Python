employees = {}

def print_employees():
    for id, name in employees.items():
        print(f'ID: {id}, name: {name}')

def add_employees():
    id = input('enter employee ID: ')
    name = input('enter employee name: ')
    if id in employees:
        print('employee already exists')
    else:
        employees[id] = name
        print('employee added')

def edit_employess():
    id = input('enter employee ID to edit:')
    name = input('enter new name: ')
    if id not in employees:
        print('employee does not exist')
    else:
        employees[id] = name
        print('employee updated')
def del_employees():
    id = input('enter employee ID to delete:')
    if id not in employees:
        print('employee does not exist')
    else:
        del employees[id]
        print('employee deleted')