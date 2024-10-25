class Cooker:
    def __init__ (self, model):
        self.model = model
        self.state = 'off'
        self.mode = "boil"
        self.temp = 0

    def show_info(self):
        print(f'MODEL: {self.model} | status: {self.state} | mode: {self.mode} | degree: {self.temp}\n')

    def turn_on (self):
        if self.state == 'on': print('this cooker is already ON !\n')
        else:
            self.state = 'on'
            self.mode = 'boil'
            self.temp = 100
            print(f'Turn ON the cooker successfully \n')
            self.show_info()
    
    def turn_off(self):
        if self.state == 'off': print('this cooker is already OFF \n')
        else:
            self.state = 'off'
            self.mode = 'idk'
            self.temp = 0
            print(f'Turn OFF the cooker successfully \n')
            self.show_info()

    def change_mode(self):
        if self.state == 'off': 
            print('Please turn on the Cooker first !\n')
            return
        mode = input('| BOIL | HOT POT | FRY |\nPlease choose your mode: ').lower()
        if mode not in ('boil', 'hot pot', 'fry'):
            print('The input mode is invalid, please try agian\n')
            return
        self.mode = mode
        if mode == 'boil': 
            self.temp = 100
            print(f'Changed mode successfully \nMODEL: {self.model} | status: {self.state} | mode: {self.mode} | degree: {self.temp} \n')
        elif mode == 'hot pot': 
            self.temp = 90
            print(f'Changed mode successfully \nMODEL: {self.model} | status: {self.state} | mode: {self.mode} | degree: {self.temp} \n')
        elif mode == 'fry': 
            self.temp = 70
            print(f'Changed mode successfully \nMODEL: {self.model} | status: {self.state} | mode: {self.mode} | degree: {self.temp} \n')

    def increase_temp(self):
        if self.state == 'off': 
            print('Please turn on the Cooker first !\n')
            return
        self.temp += 5
        print(f'increase tempature successfully! \nMODEL: {self.model} | status: {self.state} | mode: {self.mode} | degree: {self.temp}\n')

    def decrease_temp(self):
        if self.state == 'off': 
            print('Please turn on the Cooker first !\n')
            return
        if self.temp <= 0: 
            print('can not decrease. 0 degree is same as turn OFF. Please increase the Tempature! \n')
            return
        self.temp -= 5
        print(f'decrease tempature successfully! \nMODEL: {self.model} | status: {self.state} | mode: {self.mode} | degree: {self.temp}\n')

    def print_menu(self):
        print(f'Welcome to {self.model} COOKER')
        print('1. turn ON')
        print('2. turn OFF')
        print('3. change mode')
        print('4. increase temp')
        print('5. decrease temp')
        print('0. tắt cầu giao\n')

    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1: self.turn_on()
            elif choice == 2: self.turn_off()
            elif choice == 3: self.change_mode()
            elif choice == 4: self.increase_temp()
            elif choice == 5: self.decrease_temp()
            elif choice == 0: running = False

# testing time
model = input("please enter your dream Cooker model: ")
model = Cooker(model)
model.run()

# # test turn on
# model.turn_on()
# model.turn_on()

# # test turn off
# model.turn_off()
# model.turn_off()

# model.turn_on()
# # test change mode
# model.turn_off()
# model.change_mode('lmao')
# model.change_mode('fry')

# model.turn_on()
# model.change_mode('lmao')
# model.change_mode('fry')

# # test increase temp
# model.increase_temp()
# model.increase_temp()

# model.turn_off()
# model.increase_temp()

# #test decrease temp
# model.turn_on()
# model.decrease_temp()
# model.decrease_temp()

# model.turn_off()
# model.decrease_temp()


