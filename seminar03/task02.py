# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний.


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
result_list = []
for i in range((len(my_list)+1)//2):
    result_list.append(my_list[i] * my_list[-1-i])
print(result_list)