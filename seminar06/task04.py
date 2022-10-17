# Напишите программу, удаляющую из текста все слова, 
# содержащие "абв".


my_list = 'абва кадабра'

my_list = filter(lambda x: 'абв' not in x, my_list.split())
my = " ".join(my_list)
print(my)

# specific_chars = ['абв'] 

# test = "абва кадабра"

# for i in specific_chars : 
#     test_string = test.replace(i, '') 
# print(test_string)






