from random import randint

lucky_N = randint(1,10)
name=input('what is ur name?')
message =f'Hello {name}, your lucky number is {lucky_N}'
if name==" " :
    print("Invalid input. Your name cannot be blank. ")
else:
    
    if lucky_N==3 or lucky_N==9:
        message += 'and you have won a prize'
    elif lucky_N==7:
        message += ' and you have hit the jackpot'
print(message)