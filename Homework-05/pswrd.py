# Импорты
import random
import string

x = string.digits + string.ascii_letters  # Заносим в переменную х все используемые символы



def get_pass(n):  # Объявление функции 
    i = 1
    while i <= n:  # Объявляю условие: порядковый номер элемента (количество циклов) не больше количества элементов.
        yield random.choice(x) # Генератор выкидывает случайное значение.
        i += 1  # Объявляю новый цикл.
      
n = int(input('Введите желаемую длинну пароля: '))

pass_list = [x for x in get_pass(n)]  # Генерирую список символов.


password = ''.join([str(i) for i in pass_list])  # Перевожу список символов в строку, формирую пароль
print(password)



