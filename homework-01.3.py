from math import sqrt
x1, y1 = [int(n) for n in input("Введите координаты вершины A через запятую: ").split(',')]
x2, y2 = [int(n) for n in input("Введите координаты вершины B через запятую: ").split(',')]
x3, y3 = [int(n) for n in input("Введите координаты вершины C через запятую: ").split(',')]
a = sqrt((x2-x1)**2+(y2-y1)**2)
b = sqrt((x3-x2)**2+(y3-y2)**2)
c = sqrt((x1-x3)**2+(y1-y3)**2)

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Этот треугольник прямоугольный")
else:
    print("Этот треугольник не прямоугольный")
