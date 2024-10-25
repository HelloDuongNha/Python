a=float(input('nhap canh a '))
b=float(input('nhap canh b '))
c=float(input('nhap canh c '))

if a>0 and b>0 and c>0 and (a+b)>c and (b+c)>a and (a+c)>b :
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print(f'area of triangle ({a}, {b}, {c}) = {s:.2f}')
else:
    print('nhap lai')

