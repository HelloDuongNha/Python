class Customer:
    __id = 0
    def __init__(self, name):
        self.name = name
        self.bill = 0
        self.__id = Customer.__id 
        Customer.__id += 1   


    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError('Name cannot be empty')
        self.__name = name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def bill(self):
        return self.__bill
    
    @bill.setter
    def bill(self, amount):
        if amount < 0:
            raise ValueError('amount cannot be negative')
        self.__bill = amount

    def print_receipt(self):
        print(f'Customer ID: {self.id}')
        print(f'Customer name: {self.name}')
        print(f'Customer bill: {self.bill + self.bill*10/100}')

# Tạo một vài đối tượng Customer và kiểm tra các phương thức và thuộc tính
def test_customer():
    # Test việc khởi tạo và tăng ID tự động
    print("Tạo khách hàng A:")
    customerA = Customer("Alice")
    print(f'ID: {customerA.id}, Name: {customerA.name}, Bill: {customerA.bill}')
    print()

    print("Tạo khách hàng B:")
    customerB = Customer("Bob")
    print(f'ID: {customerB.id}, Name: {customerB.name}, Bill: {customerB.bill}')
    print()

    # Test thuộc tính name
    print("Thay đổi tên khách hàng B thành 'Charlie':")
    customerB.name = "Charlie"
    print(f'ID: {customerB.id}, Name: {customerB.name}, Bill: {customerB.bill}')
    print()

    # Test ngoại lệ cho thuộc tính name
    try:
        print("Thay đổi tên khách hàng B thành chuỗi rỗng:")
        customerB.name = ""
    except ValueError as e:
        print(f'Caught an exception: {e}')
    print()

    # Test thuộc tính bill
    print("Cập nhật bill cho khách hàng A lên 100:")
    customerA.bill = 100
    print(f'ID: {customerA.id}, Name: {customerA.name}, Bill: {customerA.bill}')
    print()

    # Test ngoại lệ cho thuộc tính bill
    try:
        print("Cập nhật bill cho khách hàng A thành giá trị âm:")
        customerA.bill = -50
    except ValueError as e:
        print(f'Caught an exception: {e}')
    print()

    # Test phương thức print_receipt
    print("In hóa đơn cho khách hàng A:")
    customerA.print_receipt()
    print()

    print("In hóa đơn cho khách hàng B:")
    customerB.print_receipt()
    print()

# Gọi hàm test để kiểm tra lớp Customer
# test_customer()