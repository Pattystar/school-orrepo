import sqlite3
import os.path as Path

sql = '''
    CREATE TABLE diary(
        ID INT PRIMARY KEY NOT NULL,
        TASK_TEXT TEXT NOT NULL,
        TASK_TIME INT NOT NULL,
        TASK_STATUS TEXT NOT NULL,
    )'''  # создал список

SQL_SELECT_ALL =
    SELECT id, task_text, task_time, task_status
    FROM diary

SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'

SQL_RED_TASK =
    UPDATE diary
    SET(id, task_text, task_time, task_status) + ' WHERE id=?'

SQL_REST_TASK =
    UPDATE diary
    SET task_status = 'Не выполнено' + ' WHERE id=?'

SQL_EXIT_TASK =
    UPDATE diary
    SET task_status = 'Выполнено' + ' WHERE id=?'

SQL_INSERT_TASK =
    INSERT INTO dairy (id, task_text, task_time, task_status)
    VALUES (?, ?, ?, ?)


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

    if not task:
        return

    with conn:
        cursor = conn.execute(SQL_INSERT_TASK, (id, task_text, task_time, task_status))
        return


def red_task(conn, id, task_text, task_time, task_status):# редактировать задачу

    if not task:
        return

    with conn:
        cursor = conn.execute(SQL_RED_TASK, (id, task_text, task_time, task_status))
        return

def find_all(conn):  # список задач
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def rest_task(conn, id): # найти задачу по ид
    with conn:
        cursor = conn.execute(SQL_REST, (id,))


def exit_task_(conn, id):  # найти задачу по статусу
    with conn:
        cursor = conn.execute(SQL_EXIT, (id,))


