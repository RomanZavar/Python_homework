# Задайте список из N элементов, заполненных числами из промежутка
#  [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


# with open('file.txt', 'a') as lists:
#     number.write('3\n')
#     number.write('1\n')
size = int(input('Введите число = '))
my_list = list(range(-size, size + 1))
path = 'file.txt'
lists = open(path, 'r')
for line in my_list:
    print(line)
sum = 1
for position in lists:
    sum *= my_list[int(position)]

print(my_list)
print(sum)
