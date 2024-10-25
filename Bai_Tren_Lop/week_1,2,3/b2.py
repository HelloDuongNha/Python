import turtle as t
length = int(input('enter length'))
color = input('enter color(red, green or blue)')

if length <50 or length >100:
    print(' length must be between 50 and 100')
elif color != 'red' and color != 'green' and color != 'blue' :
    print('fs')
else:
    t.forward