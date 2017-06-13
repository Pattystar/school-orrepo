import time


def pause(sec):
    def dec(func):
        def wrapper(*args, **kwargs):
            print('Начало процесса.')
            time.sleep(3)
            func(*args, **kwargs)
            print('Процесс завершён спустя {} сек.'.format(sec))
        return wrapper
    return dec


@pause(3)
def dinner():
    print('Я опоздал на обед!!!')

dinner()
                
