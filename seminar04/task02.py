# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Факторизация чисел

def primfact(n):
   i = 2
   primfact = []
   while i * i <= n:
       while n % i == 0:
           primfact.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfact.append(n)
   return primfact

n = int(input('введите число = '))
print(primfacs(n))