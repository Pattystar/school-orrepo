def a(x):
    x = input("Введите текст:")
    y = x[::-1]
    if x == y:
        return True
    else:
        return False

b = a(1)
print(b)
