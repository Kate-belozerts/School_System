#Mодуль логирования.

quit()
import os
from datetime import datetime as dt

os.chdir(os.path.dirname(__file__))

def log_logger(operation, operation_bool_result):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('Log_File.txt', 'a', encoding='utf-8') as log_file:
        log_file.write('{} - {} - {};\n'.format(time, operation, operation_bool_result))



# Import (считывает импортируемый файл и добавляет все записи оттуда в БД)
import os
import Logger
os.chdir(os.path.dirname(__file__))


def txt_import():
    name = input('Введите имя файла без расширения: ')
    try:
        with open (f'{name}.txt', 'r', encoding = 'utf-8') as file:
            file = list(map(str, file))
        with open ('PhoneBook.txt', 'a', encoding = 'utf-8') as send:
            send.writelines(file)
        Logger.log_logger('TXT_Import', True)
    except:
	    Logger.log_logger('TXT_Import', False)

