import teacher
import student
import autorization as au
import logger as lg
import admin

print('Добро пожаловать! Вас приветствует информационная система "Школик"')


def Menu():
    flag = True

    while flag:
        print('Введите логин и пароль либо пробелы для выхода:\n'
                '1 - Авторизоваться\n'
                '2 - Выход\n')
        login = str(input('Введите логин: '))
        
        lg.Log(f'User has entered login - {login}')
        password = str(input('Введите пароль: '))
        lg.Log(f'User has entered password - {password}')
        
        status = au.control(login, password)
        print(status)

        if status == ' Teacher':
            print('Вы вошли как преподаватель. Введите необходимое действие:\n'
            '1 - Написание ДЗ\n'
            '2 - Выставление оценок\n'
            '3 - Запрос админу\n'
            '4 - Выход')
            command = int(input('Введите действие: '))

            while command != 4:
                if command == 1:
                    message = str(input('Введите ДЗ: '))
                    teacher.write_HW(message)
                if command == 2:
                    teacher.write_score()
                if command == 3:
                    message = str(input('Введите запрос: '))
                    teacher.request_admin(message)
        
        if status == ' Student':
            print('Вы вошли как ученик. Введите необходимое действие:\n'
            '1 - Просмотр оценок\n'
            '2 - Просмотр ДЗ\n'
            '3 - Запрос админу\n'
            '4 - Выход')
            command = int(input('Введите действие: '))

            while command != 4:
                if command == 1:
                    student.read_score()
                if command == 2:
                    student.read_HW()
                if command == 3:
                    message = str(input('Введите запрос: '))
                    student.request_admin(message)
                
        if status == ' Admin':
            print('Вы вошли как администратор. Введите необходимое действие:\n'
            '1 - Добавление учетной записи\n'
            '2 - Удаление учетной записи\n'
            '3 - Чтение запроса\n'
            '4 - Чтение логов'
            '5 - Выход')
            command = int(input('Введите действие: '))

            while command != 5:
                if command == 1:
                    admin.create()
                if command == 2:
                    admin.delete()
                if command == 3:
                    admin.read_request()
                if command == 4:
                    admin.read_log()
                

        if login == ' ' and password == ' ':
            lg.Log('User has selected exit')
            flag = False
    