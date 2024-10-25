taikhoan = 0
money = int(input('ban muon nap bao nhieu? :'))
taikhoan += money
print(f'gio tai khoan cua ban co {taikhoan} VND')
wanna_play = True

while wanna_play == True:
    name = input('ten game la gi: ')
    cost = int(input('bao nhieu tien 1p : '))
    time = int(input('how many time u wanna play? :'))
    if taikhoan - (cost*time) < 0 or taikhoan == 0 :
        print(f'ko du tien, tai khoan cua ban con {taikhoan} va ban du de choi game {name} trong {taikhoan/cost} phut')
        ask_money = input('ban co muon nap them tien ko? (y/n) : ').lower()
        if ask_money == 'y':
            money = int(input('ban muon nap them bao nhieu? :'))
            taikhoan += money
            print(f'gio tai khoan cua ban co {taikhoan} VND')
        else:
            time = int(input('Okay. How many time u wanna play? :'))
    elif taikhoan - (cost*time) > 0:
        taikhoan -= (cost*time)
        print(f'tai khoan cua ban con {taikhoan} ')
        ask_play = input('wanna play more? (y/n) : ').lower()
        wanna_play = ask_play == 'y'
print('byeeeeee')
