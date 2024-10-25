n_kh = int(input('how many khach hang: '))
for i in range (1, n_kh+1):
    mua_tiep = True
    while mua_tiep:
        print(f'welcome Khach Hang number {i}')
        tong = 0
        name = input('Ten San Pham? :')
        cost = float(input('how much is that San Pham in VND? : '))
        amount = int(input('How many So Luong San Pham?       :'))
        ask = input('wanna buy more? (y/n)').lower()
        tong += cost * amount
        mua_tiep = ask == 'y' 
        
    print(f'Tong tien phai thanh toan cua khach hang {i}: {tong}')
        
        




