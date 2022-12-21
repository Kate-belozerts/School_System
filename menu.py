import teacher
import student
import autorization as au
import admin

print('Добро пожаловать! Вас приветствует информационная система "Школик"')


def teachers_menu(key, teacher_id):
    flag = True
    menu_teacher_dict = {'1': (teacher.homework_adder, teacher_id), '2': (teacher.knowledge_rater, teacher_id), 
    '3': (teacher.request_admin, teacher_id), '4': (turn_to_false, flag)}
    el1, el2 = menu_teacher_dict[key]
    el1(el2)


def students_menu(key, student_id):
    flag = True
    menu_student_dict = {'1': (student.read_score, student_id), '2': (student.read_HW, student_id), 
    '3': (student.request_admin, student_id), '4': (turn_to_false, flag)}
    el1, el2 = menu_student_dict[key]
    el1(el2)


def admins_menu(key, admin_id):
    flag = True
    menu_admin_dict = {'1': (admin.user_add, admin_id), '2': (admin.delete_user, admin_id), 
    '3': (admin.view_applications, admin_id), '4': (turn_to_false, flag)}
    el1, el2 = menu_admin_dict[key]
    el1(el2)


def Menu():
    flag = True

    while flag:
        print('Введите логин и пароль либо пробелы для выхода:\n'
                '1 - Авторизоваться\n'
                '2 - Выход\n')

        login = str(input('Введите логин: '))
        password = str(input('Введите пароль: '))

        status, id = au.control(login, password)
        name = f'{login};{password}'

        if status == 'Teacher':
            print('Вы вошли как преподаватель. Введите необходимое действие:\n'
            '1 - Написание ДЗ\n'
            '2 - Выставление оценок\n'
            '3 - Запрос админу\n'
            '4 - Выход')
            teachers_menu(input('Введите действие: '), id)

        
        if status == 'Student':
            print('Вы вошли как ученик. Введите необходимое действие:\n'
            '1 - Просмотр оценок\n'
            '2 - Просмотр ДЗ\n'
            '3 - Запрос админу\n'
            '4 - Выход')
            students_menu(input('Введите действие: '), name)

                
        if status == 'Admin':
            print('Вы вошли как администратор. Введите необходимое действие:\n'
            '1 - Добавление учетной записи\n'
            '2 - Удаление учетной записи\n'
            '3 - Чтение запросов\n'
            '4 - Выход')
            admins_menu(input('Введите действие: '), id[2:4])
                

        if login == ' ' and password == ' ':
            # lg.Log('User has selected exit')
            flag = False


def turn_to_false(flag):
    flag = False
    return flag

