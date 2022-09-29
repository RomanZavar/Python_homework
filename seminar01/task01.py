a = int(input('введите день недели = '))
if 0 < a <= 5:
    print('нет')
if a > 7 or a < 0:
    print ('введите коректное число дня недели')
else:
    print('да')