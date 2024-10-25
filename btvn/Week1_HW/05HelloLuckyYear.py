from random import randint

name=input('what is ur name? : ')
birth=int(input('which year u born in : '))
lucky_Y=randint(birth,birth +70)
print(f'Hello {name}, your lucky number is {lucky_Y}')