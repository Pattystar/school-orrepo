def a(x, y):
    if x < 0 and y < 0:
        b = "3"
    if x > 0 and y < 0:
        b = "4"
    if x > 0 and y > 0:
        b = "1"
    if x < 0 and y > 0:
        b = "2"
    else:
        return None
    return b

b = a(-1, 499)
print(b)

