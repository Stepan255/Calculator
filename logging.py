import time

def logger(data):
    log_time = time.asctime()
    with open('C:\Pratice_code\Calculator\log.txt', 'a') as file:
        file.write('{}-{}\n' . format(log_time, data))


logger('test')