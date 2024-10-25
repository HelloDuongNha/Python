n = int(input('input a number'))
output = ""
if n<0:
    n = input('please enter a number again: ')

while n!=0:
    r = n%2
    n = n//2
    output = str(r) + output
print(f' may tinh se hieu la {output}')