# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
#  дробной части элемент

my_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = [(num % 1) for num in my_list if isinstance(num, float)]
print(new_list)
max_num = max(new_list)
min_num = min(new_list)
print(f'разница между мин и макс = {float(max_num - min_num):g}')

