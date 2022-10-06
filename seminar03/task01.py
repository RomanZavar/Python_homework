# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

my_list = []
my_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f'сумма равна {(sum(my_list[1::2]))}')


# def index_list_suma(my_list):
#     result = 0
#     for i in range(1, len(my_list), 2):
#      result += my_list[i]
#     print(f"Сумма равна: {result}")


# my_list = []
# my_list = list(map(int, input("Введите числа через пробел:\n").split()))
# index_list_suma(my_list)


