for i in range (10):
    print(i, end='')

print('\n------------')

s = 0
for i in range(1,11):
    s += i # s = s + i

print(f'sum of number from 1 to 10: {s}')

sao = int(input('how many star which u want? :'))
for i in range (sao):
    print('*', end='')

n = int(input('which number? : '))
for i in range (1,11):
    print(f'{i:2} x {n:2} = {i*n:2}')