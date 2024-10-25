class Movie:
    def __init__(self, name, director, rate):
        self.set_name(name)
        self.set_director(director)
        self.set_rate(rate)
        # self.__name = name
        # self.__director = director
        # self.__rate = rate

    def set_name(self, name):
        if name == '':
            print('sorry, Name cannot emty\n')
            self.__name = 'no name'
            return
        self.__name = name
        print('set up Name successfully \n')
        # self.show_movie()

    def set_director(self, director):
        if director == '':
            print('sorry, Di cannot emty\n')
            self.__director = 'no director'
            return
        self.__director = director
        print('set up Di successfully \n')
        # self.show_movie()

    def set_rate(self, rate):
        try:
            # rate = int(input('in range 0 to 5 star: '))
            if rate not in range(0,6):
                print('please enter number in range 0-5!!\n')
                self.__rate = 0
                return
            self.__rate = rate
            print('set up RAtE successfully \n')
            # self.show_movie()
        except ValueError:
            print('please input a interger number instead\n')
    
    def get_name(self):
        return self.__name

    def get_director(self):
        return self.__director
    
    def get_rate(self):
        return self.__rate

    def show_movie(self):
        print(f'name: {self.__name} | director: {self.__director} | rate: {self.__rate}\n')

# test
lmao = Movie('', "", 5)


lmao.show_movie()
lmao.set_rate(4)
# lmao.set_rate()
lmao.show_movie()
print(lmao.get_name())

lmao.show_movie()