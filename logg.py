import time

def logger(data):
    log_time = time.asctime()
    with open(r'C:\Stepan\teamwork\Calculator\log.txt', 'a') as file:
        file.write('{}-{}\n' . format(log_time, data))


# logger('test')