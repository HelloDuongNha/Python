n = int(input("Nhap n: "))

print('1st triangle: ')
for i in range(n, 0, -1):
    print(" " * (n - i) * 2, end="")
    print("* " * (i * 2 - 1))

print('2nd triangle: ')

for i in range(n, 0, -1):
    print(" " * (n - i) * 2, end="")
    print("* " * i)
