# Задайте список из n чисел последовательности
# $(1+1\n)**n и выведите на экран их сумму.


def is_int(number):
  return number.isdigit()
number = None
while not is_int(str(number)):
  number = input("Input number:")
number = int(number)
result = dict()
for i in range(1, number+1):
 result[i] = round((1 + 1 / i) ** i)
my_sum = 0
for i in result:
 my_sum += result[i]

print(result, ' ', my_sum)