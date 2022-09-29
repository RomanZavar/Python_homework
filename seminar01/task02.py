def check_predikat():   
    count = 0  
    for x in range(2):
        for y in range(2):
            for z in range(2):
                rez = (not(x or y or z) == ((not x) and (not y) and (not z)))
                print(rez)
                if rez: count += 1
                else: print('Утверждения не истино')
    if  count == 8: print('Утверждение истино')      
check_predikat()