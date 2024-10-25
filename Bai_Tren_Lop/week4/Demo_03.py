import random as rd

answer = 'y'
while answer =='y' or answer == 'yes':
    n_corrects = 0
    n_incorrects = 0
    for i in range(5):
        guess_number = int(input('enter your guess (1-5): '))
        n_random = rd.randint(1,5)
        if n_random == guess_number:
            print('correct!')
            n_corrects += 1
        else:
            print('incorrect!')
            n_incorrects += 1

    print(f'number of correct guess: {n_corrects}')
    print(f'number of incorrect guess: {n_incorrects}')
    answer = input('do you wanna pla again (y/n):')

print('goodbye!')