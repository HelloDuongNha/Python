print('Scenario: ứng tuyển vào công ty')
name = str(input('what is ur name?  '))
nn = str(input('which do u expert in C or Java : '))
kn = int(input('so nam kinh nghiem cua ban: '))
#con thieu check nn va kn
if nn =='C' or 'c':
    if kn < 2:
        lv='junior'
    elif kn<=5:
        lv='senior'
    else:
        lv='team leader'
    print(f'tham gia dự án hệ thống ở vị trí {lv}')
elif nn=="java" or "Java":
    if kn < 2:
        lv='junior'
    elif kn<=5:
        lv='senior'
    else:
        lv='team leader'
    print(f'tham gia dự án web ở vị trí {lv}')
else:
    print('please rechoose ur language experise')

