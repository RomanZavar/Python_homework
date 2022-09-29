import math
xa = int(input('ВВедите координату первой точки по оси X = '))
ya = int(input('ВВедите координату первой точки по оси Y = '))
xb = int(input('ВВедите координату второй точки по оси X = '))
yb = int(input('ВВедите координату второй точки по оси Y = '))
result = math.sqrt((xb-xa)**2 + (yb-ya)**2)
result = round(result, 2)
print(result)