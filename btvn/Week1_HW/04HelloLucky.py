from random import randint

lucky_N = randint(1,100)
name=input('what is ur name?')
if name==" " :
    print("Invalid input. Your name cannot be blank. ")
else:
    print(f'Hello {name}, your lucky number is {lucky_N}')

