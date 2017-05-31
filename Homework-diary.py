def menu(a):
    
    print("Ежедневник. Выберите действие: ")

    print("1. Вывести список задач")

    print("2. Добавить задачу")

    print("3. Отредактировать задачу")

    print("4. Завершить задачу")

    print("5. Начать задачу сначала")

    print("6. Выход")

    num = int(input("Введите число: "))


    if num == 1:    
        with open('task_list.txt', 'w') as f:
            f.write("Список задач: ")
        with open('task_list.txt', 'r') as f:
            print(f.read())
            f.seek(0)

    if num == 2:    
        with open('task_list.txt', 'w') as f:
            f.write("Новая задача: ")
            f.seek(0)
        with open('task_list.txt', 'r') as f:
            print(f.read())
            f.seek(0)

    if num == 3:    
        with open('task_list.txt', 'w') as f:
            f.write("Редактирование задачи: ")
            f.seek(0)
        with open('task_list.txt', 'r') as f:
            print(f.read())
            f.seek(0)

    if num == 4:    
        with open('task_list.txt', 'w') as f:
            f.write("Завершение задачи: ")
            f.seek(0)
        with open('task_list.txt', 'r') as f:
            print(f.read())
            f.seek(0)

    if num == 5:    
        with open('task_list.txt', 'w') as f:
            f.write("Начать задачу заново: ")
            f.seek(0)
        with open('task_list.txt', 'r') as f:
            print(f.read())
            f.seek(0)

    if num == 6:    
        with open('task_list.txt', 'w') as f:
            f.write("Выход: ")
            f.seek(0)
        with open('task_list.txt', 'r') as f:
            print(f.read())
            f.seek(0)

menu(menu(2))

