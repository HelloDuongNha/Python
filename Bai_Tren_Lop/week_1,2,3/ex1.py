#exercise 1:

def new_func():
    math= int(input('enter your math score:'))
    english= int(input('enter your english score:'))
    physics= int(input('enter your physics score:'))
    average=((math+english+physics)/3)
    print('math   : 'f'{math:10}')
    print('english: 'f'{english:10}')
    print('physics: 'f'{physics:10}')
    print('average: 'f'{average:10}')

new_func()
