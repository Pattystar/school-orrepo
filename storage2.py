""" НАДО УТОЧНИТЬ НЕКОТОРЫЕ МОМЕНТЫ """
import sqlite3
import os.path as Path

CREATE TABLE DIARY(
   ID  INT PRIMARY KEY      NOT NULL,
   TASK_TEXT       TEXT     NOT NULL,
   TASK_TIME       INT      NOT NULL,
   TASK_STATUS     TEXT     NOT NULL,
   CREATED         DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
   );  # создал список

SQL_SELECT_ALL = SELECT
id, task_text, task_time, task_status, created
FROM
diary

SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'

SQL_SELECT_TASK_BY_TASK_TEXT = SQL_SELECT_ALL + ' WHERE task_text=?'

SQL_SELECT_TASK_BY_TASK_TIME = SQL_SELECT_ALL + ' WHERE task_time=?'

SQL_SELECT_TASK_BY_TASK_STATUS = SQL_SELECT_ALL + ' WHERE task_status=?'

SQL_INSERT_TASK = INSERT INTO dairy VALUES (?, ?, ?, ?)
)   # найти задачу по статусу

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


def add_task(conn, task_text=''):# добавить задачу
    
    if not task:
        return

    with conn:
        found = find_task_by_task_text(conn, task_text)

        if found:
            return found[2]

        cursor = conn.execute(SQL_INSERT_TASK, (task_text,))
        return

def find_all(conn):  # список задач
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def find_task_by_pk(conn, pk): # найти задачу по ид
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
        return cursor.fetchone()


def find_task_by_status(conn, task_status):  # найти задачу по статусу
    pass


def find_task_by_text(conn, task_text): # найти задачу по наименованию
    
    with conn:
        cursor = conn.execute(
            SQL_SELECT_TASK_BY_TEXT, (task_text,)
        )
        return cursor.fetchone()
