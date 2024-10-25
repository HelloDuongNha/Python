#ve hinh tam giac
n = int(input('nhap so dong: '))
a = ''
for i in range(n):
    a+='*'
    print(a)
    print()

#ve hinh vuong
n =  int(input('enter n: '))
for i in range(n):
    for j in range(n):
        print('*', end= ' ')
    print()

#ve hinh chu nhat
m = int(input('enter m: '))
for i in range(n):
    for j in range(m):
        print('*', end=' ')
    print()

#ve hinh tam giac nguoc
n =  int(input('enter n: '))
for i in range(n,0,-1):
    for j in range(i):
        print('*', end= ' ')
    print()

n =  int(input('enter n: '))
for i in range(n+1):
    b = n - i
    for c in range(b):
        print(' ', end= ' ')
    for j in range(i):
        print('*', end= ' ')
    print()


n =  int(input('enter n: '))
for i in range(n+1):
    b = n - i
    for c in range(b):
        print(' ', end= ' ')
    for j in range(i*2+1):
        print('*', end= ' ')
    print()