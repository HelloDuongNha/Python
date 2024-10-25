class Course:
    def __init__(self, name, credit, type):
        self.set_name(name)
        self.set_credit(credit)
        self.set_asm_type(type)
        # self.__name = name
        # self.__director = director
        # self.__rate = rate

    def set_name(self, name):
        if name == '':
            print('sorry, cannot emty\n')
            self.__name = 'no name'
            return
        self.__name = name
        print('set up successfully \n')
        self.show_course()

    def set_credit(self, credit):
        try:
            # credit = int(input(f'| 15 | 30 | 60 |\nPlease choose your credit'))
            if credit not in [15, 30, 60]:
                print('please choose 1 of [15, 30, 60]\n')
                self.__credit = 'no credit'
                return
            self.__credit = credit
            print('set up successfully \n')
            # self.show_course()
        except ValueError:
            print('please input a interger number instead\n')
    
    def set_asm_type(self, type):
        try:
            # type = int(input(f'selection 1. Exam\nselection 2. Report\nPLEASE CHOOSE 1 or 2: '))
            if type not in [1, 2]:
                print('please only choose 1 or 2\n')
                self.__asm_type = 'no type'
                return
            self.__asm_type = type
            print('set up successfully \n')
            # self.show_course()
        except ValueError:
            print('please input a interger number instead\n')

    def get_name(self):
        return self.__name

    def get_credit(self):
        return self.__credit
    
    def get_asm_type(self):
        return self.__asm_type

    def show_course(self):
        print(f'name: {self.__name} | credit: {self.__credit} | asm type: {self.__asm_type}\n')

# test
lmao = Course('IT', "15", "1")


lmao.show_course()
lmao.set_name('lmao')
lmao.set_credit(15)
lmao.set_asm_type('report')
lmao.show_course()
print(lmao.get_name())

# lmao.show_movie()