#Mодуль логирования.

import os
from datetime import datetime as dt

os.chdir(os.path.dirname(__file__))

def Log(operation, operation_bool_result):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('_BD\Log_File.txt', 'a', encoding='utf-8') as log_file:
        log_file.write('{} - {} - {};\n'.format(time, operation, operation_bool_result))


#     try:      
#         ### КОД ###
#         Logger.log_logger('TXT_Import', True)
#     except:
# 	    Logger.log_logger('TXT_Import', False)


# Тимофея:
# import os
# import logger
# from datetime import datetime as dt
# os.chdir(os.path.dirname(__file__))


# logger.add('logger.json', format='{time} , {level} , {message}',#(тут время, уровень ошибки и сообщение)
# level='DEBUG', rotation='100 KB', compression='zip') #(debug,info,error). rotation(размер лога,
# # можно указать вместо 100 KB - 1 MB или 10:00 (файл будет перезивасыватся в зип каждый день в 10 утра)

# logger.debug(logger)
