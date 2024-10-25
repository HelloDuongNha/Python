s = 0
n = int(input('enter an even nubmer: '))
while n % 2 !=1:
    s += n
    n = int(input('enter an even number: '))

print(f'sum of even entered number: {s}')