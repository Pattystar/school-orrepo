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


def action_rest():
    print('''Повторное объявление задачи:
''')
    storage.rest_task()
              
    
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
6. Показать меню.
v. Выход
''')


def action_exit():
    """Обработчик действия выйти"""
    sys.exit(0)
    


def main():
    show_menu()

    actions = {
        '1': action_find_all,
        '2': action_add,
        '3': action_red,
        '4': action_exit_task,
        '5': action_rest,
        '6': action_show_menu,
        'v': action_exit
    }

    while True:
        id_action = input('''Введите номер действия: ''')
        action = actions.get(id_action)

        if action:
            action()
        else:
            print('''Вы ввели неверные данные''')
