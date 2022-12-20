from datetime import datetime as dt
from time import time

def Log(data):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} - {}\n'
                    .format(time, data))



# import os
# from loguru import logger
# from datetime import datetime as dt
# os.chdir(os.path.dirname(__file__))


# logger.add('logger.json', format='{time} , {level} , {message}',#(тут время, уровень ошибки и сообщение)
# level='DEBUG', rotation='100 KB', compression='zip') #(debug,info,error). rotation(размер лога,
# # можно указать вместо 100 KB - 1 MB или 10:00 (файл будет перезивасыватся в зип каждый день в 10 утра)

# logger.debug(logger)

logger.debug(logger)
def Log(data):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{} - {}\n'
                    .format(time, data))