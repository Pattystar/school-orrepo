import time

def dec(func):
    def wrapper():
        print('Начало процесса')
        n = 0
        pause = int(input('Введтие задержку выполнения программы в секундах:\n'))
        time.sleep(pause)
        func()
        print('Процесс завершён спустя {} сек.'.format(pause))
    return wrapper


@dec
def dinner():
    print('Я опоздал на обед!!!')

dinner()
                
