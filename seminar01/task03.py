x = int(input('Введите координтау x ='))
y = int(input('Введите координату y ='))

if x > 0:
    if y > 0:
        print('  1')
    else: print(' 4')
elif x < 0:
    if y > 0:
        print(' 2')
    else:   print(' 3')    