#ladder if else if
#enter 3 grades (math, english, physics)
#caclculate the average
#consider the rank based on he average:
#fail: average < 5, pass: 5 <= aveerage < 7,
#merit: 7 <= average < 8, distinction: 8 <= average <= 10
#print therank with the average

math= int(input('enter your math score:'))
english= int(input('enter your english score:'))
physics= int(input('enter your physics score:'))

if math < 0 or math > 10 or english <0 or english >10 or physics <0 or physics >10:
    print('grade must be between 0 and 10')
else:
    average = (math + english + physics)/3
    if average < 5:
        rank = 'fail'
    elif average < 7:
        rank = 'pass'
    elif average<8:
        rank ='merit'
    else:
        rank='distinction'
    print(f'average: {average:.2f}, rank: {rank}')