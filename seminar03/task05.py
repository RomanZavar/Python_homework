# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных 
#


def fib(n):
    fibo_nums = []
    a = 0
    b = 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1 
    for i in range(n - 1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

n = int(input('введите число = '))
fibo_nums = fib(n)
print(fib(n))


