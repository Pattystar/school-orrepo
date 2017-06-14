import sqlite3
import os.path as Path

sql = '''
    CREATE TABLE diary(
        task_id INT PRIMARY KEY AUTOINCREMENT,
        task_text TEXT NOT NULL,
        task_time INT NOT NULL,
        task_status TEXT NOT NULL,
    )'''  # создал список

SQL_SELECT_ALL ='''
    SELECT task_id, task_text, task_time, task_status
    FROM diary
    '''

SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE task_id=?'

SQL_RED_TASK ='''
    UPDATE diary
    SET(task_id, task_text, task_time, task_status) + ' WHERE task_id=?'
    '''

SQL_REST_TASK ='''
    UPDATE diary
    SET task_status = 'Не выполнено' + ' WHERE task_id=?'
    '''

SQL_EXIT_TASK ='''
    UPDATE diary
    SET task_status = 'Выполнено' + ' WHERE task_id=?'
    '''

SQL_INSERT_TASK ='''
    INSERT INTO dairy (task_id, task_text, task_time, task_status)
    VALUES (?, ?, ?, ?)
    '''


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)

    return conn # создал соединение с БД


def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'tasks.sql')

        with open(script_file_path) as f:
            conn.executescript(f.read())   # Указал файл БД


def add_task(conn, task_text, task_time, task_status):# добавить задачу

    with conn:
        cursor = conn.execute(SQL_INSERT_TASK, (task_id, task_text, task_time, task_status))
        cursor.commit() 


def red_task(conn, task_id, task_text, task_time, task_status):# редактировать задачу

    with conn:
        cursor = conn.execute(SQL_RED_TASK, (task_text, task_time, task_status, task_id,))
        return

def find_all(conn):  # список задач
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def rest_task(conn, id): # начать заново
    with conn:
        cursor = conn.execute(SQL_REST, (task_id,))


def exit_task_(conn, task_id):  # завершить задачу
    with conn:
        cursor = conn.execute(SQL_EXIT, (task_id,))
        cursor.commit()
      


