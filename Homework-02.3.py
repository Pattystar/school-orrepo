def a(x):                               # Объявление функции
    n = 1                               # Присваивание переменной n начального значения.
    while n < len(x):                   # Задаётся условие для выполнения программы:"Пока порядковый номер элемента меньше количества элементов в списке:"
        for i in range(len(x)-n):       # Задается условие для выполнения программы:"После каждого прохода цикла по списку количество проверяемых на
                                        # соответствие предыдущему условию объектов списка равно разности количества чисел в списке и количества выполненных циклов"
            if x[i] > x[i+1]:           # Задается условие: "Если при сравнении двух соседних чисел первое больше второго, 
                 x[i],x[i+1] = x[i+1],x[i] # в списке они меняются местами"
                 print(x)               # Визуальный вывод функции для проверки правильности.
    n += 1                              # Счетчик проходов(элементов, которые больше не участвуют в цикле)
        
a([1, 9, 4, 5, 7, 10, 6, 3, 2, 11]) 



     
     
