# Напишите программу, удаляющую из текста все слова, 
# содержащие "абв".


my_list = 'абва кадабра'

my_list = filter(lambda x: 'абв' not in x, my_list.split())
my = " ".join(my_list)
print(my)