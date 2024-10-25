from w6_customer import Customer
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
            raise ValueError('Amount cannot be negative')
        self.__bill = amount

    def print_receipt(self):
        print(f'Customer ID: {self.id}')
        print(f'Customer name: {self.name}')
        print(f'Customer bill: {self.bill + self.bill*10/100}')

class VipCustomer(Customer):
    def __init__(self, name, rank):
        super().__init__(name)
        self.rank = rank
    
    @property
    def rank(self):
        return self.__rank
    
    @rank.setter
    def rank(self, rank):
        if rank.lower() not in ['silver', 'gold']:
            raise ValueError('Invalid account type')
        self.__rank = rank

    def print_receipt(self):
        super().print_receipt()
        if self.rank.lower() == 'silver':
            discount = self.bill * 0.15
        else:
            discount = self.bill * 0.25
        print(f'But you are a {self.rank.capitalize()} VIP Customer, so you have a discount of {discount}')
        print(f'So your final bill is {self.bill + self.bill*0.10 - discount}')

# Test các phương thức của VipCustomer
def test_vip_customer():
    # Tạo một VipCustomer với tên và loại rank
    vip_customer = VipCustomer("John Doe", "gold")
    
    # Đặt giá trị bill
    vip_customer.bill = 1000
    
    # In hoá đơn
    vip_customer.print_receipt()
    
    # Test setter cho rank
    try:
        vip_customer.rank = 'diamond'
    except ValueError as e:
        print(e)
    
    # Test setter cho name
    try:
        vip_customer.name = ''
    except ValueError as e:
        print(e)
    
    # Test setter cho bill
    try:
        vip_customer.bill = -500
    except ValueError as e:
        print(e)

# Gọi hàm test
test_vip_customer()
