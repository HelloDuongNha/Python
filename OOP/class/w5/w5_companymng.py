from w5_employee import Employee
from w5_company import Company

class CompanyManagerProgram:
    def __init__(self, name):
        self.__company = Company(name)

    def __print_menu(self):
        print('Welcome to Company Manager')
        print('1. Show all employees')
        print('2. Search employee by ID')
        print('3. Add new employee')
        print('4. Edit employee rate')
        print('5. Delete employee')
        print('6. Exit')

    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.__company.show_all()
            elif choice == 2:
                self.__search_employee()
            elif choice == 3:
                self.__add_employee()
            elif choice == 4:
                self.__edit_employee_rate()
            elif choice == 5:
                self.__delete_employee()
            elif choice == 6:
                running = False
            else:
                print('Invalid choice. Please try again.')

    def __search_employee(self):
        id = int(input('Enter employee ID to search: '))
        self.__company.show_employee(id)

    def __add_employee(self):
        id = int(input('Enter employee ID: '))
        name = input('Enter employee name: ')
        rate = float(input('Enter employee rate: '))
        try:
            employee = Employee(id, name, rate)
            self.__company.add(employee)
            print('Employee added successfully.')
        except ValueError as e:
            print(e)

    def __edit_employee_rate(self):
        id = int(input('Enter employee ID to edit: '))
        new_rate = float(input('Enter new rate: '))
        try:
            self.__company.change(id, new_rate)
            print('Employee rate updated successfully.')
        except ValueError as e:
            print(e)

    def __delete_employee(self):
        id = int(input('Enter employee ID to delete: '))
        try:
            self.__company.remove(id)
            print('Employee removed successfully.')
        except ValueError as e:
            print(e)


#test
lmao = CompanyManagerProgram('lmao')
lmao.run()