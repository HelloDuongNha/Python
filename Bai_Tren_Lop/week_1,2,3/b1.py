#number operator: + - * / // % **
a= int(input('enter a:'))
b= int(input('enter b:'))
print('a + b =',a+b)
print('a - b =',a-b)
print('a * b =',a*b)
print('a / b =',a/b)
print('a // b',a//b)
print('a % b =',a%b)
print('a ** b =',a**b)

#string operator: +; *
a = 'hello'
b = 'world'
c = a + ' ' + b
print(c)

c= a + a + a
print(c)

c= a*3
print(c)

# boolean operator: and, or, not
a = True
b = False

#without format, python reserver just enough spaces to print
s='hello'
a=4
b=4.32

#reserved 20 spaces to print
print(f'|{s:20}|') #by default, string is aligned on the left
print(f'|{a:20}|') #by deafault, number are aligned on the right
print(f'|{b:20}|')

#mannual align output
print(f'|{s:>20}|') #align s on the right
print(f'|{a:<20}|') #align a on the left
print(f'|{b:^20}|') #align b in the middle

