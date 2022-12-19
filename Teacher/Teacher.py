'''
Teacher:
    - Написание ДЗ.(готово)
    - Выставление оценок.
    - Запрос админу.
'''
import os
import csv
import openpyxl
from datetime import date

os.chdir(os.path.dirname(__file__))


def dir_maker(path_id):
    if not os.path.exists(path_id):
        os.makedirs(path_id)


def class_existence_checker(message):
    class_list = ['1А', '1Б', '2А', '2Б', '3А', '3Б', '4А', '4Б', '5А', '5Б',
                  '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б']
    class_id = input(message)
    if class_id.upper() not in class_list:
        print('Такого класса не существует!')
        class_id = class_existence_checker(message)
    return class_id.upper()


def rater_input_checker(message):
    knowledge_rating = input(message)
    try:
        knowledge_rating = int(knowledge_rating)
        if knowledge_rating not in range(1, 6):
            print('Такие оценки ставить нельзя!')
            knowledge_rating = rater_input_checker(message)
    except:
        print('Ошибка ввода! Оценка может быть только числом от 1 до 5.')
        knowledge_rating = rater_input_checker(message)
    finally:
        return knowledge_rating


def homework_adder(teacher_id):
    teacher_id = list(teacher_id.split(';'))
    lesson_id = teacher_id[2]
    lesson_date = date.today().strftime('%d.%m.%Y')
    class_id = class_existence_checker(
        f'{" ".join(teacher_id[0:2])}, какому классу будет Д/З: ')

    path_id = r'..\DataBase\{}_Класс'.format(class_id)
    homework_file = r'{}\{}_ДЗ_{}.csv'.format(
        dir_maker(path_id), class_id, lesson_id)
    homework = input(f'Какое Д/З будет у {class_id}?\n')
    homework = [[lesson_date, lesson_id, homework]]

    with open(homework_file, 'a', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for row in homework:
            writer.writerow(row)
    print('Домашнее задание добавлено.')


def knowledge_rater(teacher_id):
    teacher_id = list(teacher_id.split(';'))
    lesson_id = teacher_id[2]
    class_id = class_existence_checker('Номер класса: ')
    student_id = input('Введите Имя и Фамилию ученика через пробел: ')
    knowledge_rating = rater_input_checker('Введите оценку: ')
    student_id.append(lesson_id).append(knowledge_rating)

    path_id = r'..\DataBase\{}_Класс'.format(class_id)
    rating_paper = r'{}\{}_Оценки.csv'.format(dir_maker(path_id), class_id)
    with open(rating_paper, 'a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for row in student_id:
            if row[0:3] == student_id[0:3]:
                writer.writerow(student_id[3])
    print(teacher_id, student_id, knowledge_rating)


def student_finder(student_id, class_id):
    student_id = student_id.split()
    student_id.append(class_id)
    print(student_id)
    path_id = r'..\DataBase\{}_Класс'.format(class_id)
    students_list = r'{}\{}_Список_Учеников.csv'.format(
        dir_maker(path_id), class_id)
    with open(students_list, 'r', encode='utf-8') as file:
        for line in file:
            print(line)


def menu_(key, teacher_id):
    menu_dict = {'1': (homework_adder, teacher_id),
                 '2': (knowledge_rater, teacher_id)}
    el1, el2 = menu_dict[key]
    el1(el2)


# teacher_id = 'Василий;Петров;Математика'
# menu_list = '1. Дать ДЗ.\n2. Дать оценку.'
# print(menu_list)
# menu_(input('Введите что хотите сделать: '), teacher_id)

'''
    #Намётки на меню и вызов функций через словари.
teacher_id = 'Василий;Петров;Математика'


def menu_(key, teacher_id):
    menu_dict = {'1': (homework_adder, teacher_id), '2': (knowledge_rater, teacher_id)}
    el1, el2 = menu_dict[key]
    el1(el2)


menu_list = '1. Дать ДЗ.\n2. Дать оценку.'
print(menu_list)
menu_(input('Введите что хотите сделать: '), teacher_id)
'''