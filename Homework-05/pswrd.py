# Импорты
import random
import string

x = string.digits + string.ascii_letters  # Заносим в переменную х все используемые символы



def password_generator(n):
    while 1: 
        i = 1
        psw = []
        while i <= n:  # Объявляю условие: порядковый номер элемента (количество циклов) не больше количества элементов.
            psw.append(random.choice(x)) # Генератор выкидывает случайное значение.
            i += 1  # Объявляю новый цикл.
        yield ''.join(psw)
            

       
n = int(input('Введите желаемую длинну пароля: '))
gen = password_generator(n)
print('Случайный пароль №1: {}'.format(next(gen)))
print('Случайный пароль №2: {}'.format(next(gen)))
print('Случайный пароль №3: {}'.format(next(gen)))



