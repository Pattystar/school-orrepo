# Пока не сделано, надо спать
import sys

from diary import storage

get_connection = lambda: storage.connect('diary.sqlite')

def action_add():
    print('''Добавление  задачи:
''')
    storage.add_task()


def action_red():
    print('''Редактирование задачи:
''')
    storage.red_task()
    
def action_exit_task():
    print('''Завершение задачи:
''')
    storage.exit_task()


def action_find_all():
    print('''Список задач:
''')
    storage.find_all()

    


def action_show_menu():
    print('''Ежедневник. Выберите действие:

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Выход
''')


def action_exit():
    """Обработчик действия выйти"""
    sys.exit(0)
    


    action_id = input('Введите номер действия: ')
    if action_id not in ['1', '2', '3', '4', '5', '6']:
        print('Выбрано неверное действие. Попробуйте снова.\n')
        menu()
    else:
        action_id = int(action_id)

    if action_id == 1:
        action_find_all()
        menu()
    elif action_id == 2:
        action_add_task()
        menu()
    elif action_id == 3:
        action_red_task()
        menu()
    elif action_id == 4:
        action_exit_task()
        menu()
    elif action_id == 5:
        action_rest_task()
        menu()
    elif action_id == 6:
        action_exit()

menu()

