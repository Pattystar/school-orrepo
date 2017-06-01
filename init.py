# Пока не сделано, надо спать
import sys

from diary import storage

#def get_connection():
# return storage.connect('shortener.sqlite')
get_connection = lambda: storage.connect('diary.sqlite')

def action_add():
    ok = False

    while not ok:
        task = input('\nВведите задачу: ')

        if not task:
            break

        ok = True


def action_red():
    ok = False

    while not ok:
        task = input('\nОтредактируйте задачу: ')

        if not task:
            break

        ok = True


def action_find_all():
    """Обработчик действия показать все ссылки"""
    with get_connection() as conn:
        task = storage.find_all(conn)

    for task in tasks:
        print('{task[task]} - {task[task_time]} - {task[task_status]} '.format(task=task))


def action_show_menu():
    print('''Ежедневник. Выберите действие:

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Выход''')


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
        Tasks.show_tasks()
        menu()
    elif action_id == 2:
        Tasks.add_task()
        menu()
    elif action_id == 3:
        Tasks.edit_task()
        menu()
    elif action_id == 4:
        Tasks.close_task()
        menu()
    elif action_id == 5:
        Tasks.reopen_task()
        menu()
    elif action_id == 6:
        Tasks.diary_exit()

menu()

