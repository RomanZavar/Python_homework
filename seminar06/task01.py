# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной
# последовательности


lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")


# A = [1, 2, 3, 2, 5, 1]
# found = set()
# found_again = set()

# for a in A:
#     if a in found_again:
#         continue
#     if a in found:
#         found.remove(a)
#         found_again.add(a)
#     else:
#         found.add(a)

# print(list(found))