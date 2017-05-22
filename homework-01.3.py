a = 3
b = 4
c = int(input("Введите значение вершины с:"))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Yes")
else:
    print("no")
