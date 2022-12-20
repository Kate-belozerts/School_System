import teacher
import student
import autorization as au
import logger as lg
import admin

print('Добро пожаловать! Вас приветствует информационная система "Школик"')

# def teachers_menu(key, teacher_id):
#     menu_teacher_dict = {'1': (teacher.homework_adder(teacher_id)), '2': (teacher.knowledge_rater(teacher_id)), '3': (teacher.request_admin(teacher_id)), '4': (flag = False)}
#     el1, el2 = menu_teacher_dict[key]
#     el1(el2)

# def students_menu(key, student_id):
#     menu_student_dict = {'1': (print(student_id)), '2': (print('student_id')), 
#                     '3': (print(2,'student_id')), '4': (flag = False)}
#     el1, el2 = menu_student_dict[key]
#     el1(el2)

# def admins_menu(key, admin_id):
#     menu_admin_dict = {'1': (print(admin_id)), '2': (print('admin_id')), 
#                     '3': (print(2,'admin_id')), '4': (flag = False)}
#     el1, el2 = menu_admin_dict[key]
#     el1(el2)


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
        
        status, id = au.control(login, password)
        print(status)
        print(id)

        if status == 'Teacher':
            print('Вы вошли как преподаватель. Введите необходимое действие:\n'
            '1 - Написание ДЗ\n'
            '2 - Выставление оценок\n'
            '3 - Запрос админу\n'
            '4 - Выход')
            #teachers_menu(input('Введите действие: '), id)
            command = int(input('Введите действие: '))
            while command != 4:
                if command == 1:
                    #message = str(input('Введите ДЗ: '))
                    #print(message)
                    teacher.homework_adder(id)
                if command == 2:
                    teacher.write_score()
                if command == 3:
                    message = str(input('Введите запрос: '))
                    teacher.request_admin(message)
        
        if status == 'Student':
            print('Вы вошли как ученик. Введите необходимое действие:\n'
            '1 - Просмотр оценок\n'
            '2 - Просмотр ДЗ\n'
            '3 - Запрос админу\n'
            '4 - Выход')
            #students_menu(input('Введите действие: '), id)

            while command != 4:
                if command == 1:
                    student.read_score()
                if command == 2:
                    student.read_HW()
                if command == 3:
                    message = str(input('Введите запрос: '))
                    student.request_admin(message)
                
        if status == 'Admin':
            print('Вы вошли как администратор. Введите необходимое действие:\n'
            '1 - Добавление учетной записи\n'
            '2 - Удаление учетной записи\n'
            '3 - Чтение запроса\n'
            '4 - Чтение логов'
            '5 - Выход')
            admins_menu = (input('Введите действие: '), id)

            # while command != 5:
            #     if command == 1:
            #         admin.create()
            #     if command == 2:
            #         admin.delete()
            #     if command == 3:
            #         admin.read_request()
            #     if command == 4:
            #         admin.read_log()
                

        if login == ' ' and password == ' ':
            lg.Log('User has selected exit')
            flag = False
    