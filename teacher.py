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
    print(teacher_id)
    lesson_id = teacher_id[4]
    lesson_date = date.today().strftime('%d.%m.%Y')
    class_id = class_existence_checker(
        f'{" ".join(teacher_id[2:4])}, какому классу будет Д/З: ')
    homework_file = r'_BD\_{}{}_HW.csv'.format(
        class_id, lesson_id)
    homework = input(f'Какое Д/З будет у {class_id}?\n')
    homework = [[lesson_date, lesson_id, homework]]

    with open(homework_file, 'a', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for row in homework:
            writer.writerow(row)
    print('Домашнее задание добавлено.')


def knowledge_rater(teacher_id):
    lesson_id = teacher_id[4]
    class_id = class_existence_checker('Номер класса: ')
    student_id = input('Введите Имя и Фамилию ученика через пробел: ').split()
    knowledge_rating = str(rater_input_checker('Введите оценку: '))
    student_id.append(class_id)
    student_id.append(lesson_id)
    student_id.append(knowledge_rating)
    rating_paper = r'_BD\_Marks.csv'
    with open(rating_paper, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        tmp = []
        for row in reader:
            if student_id[0:4] == row[2:6]:
                row.append(student_id[4])
            tmp.append(row)
        print(tmp)
        with open(rating_paper, 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';', dialect='excel')
            for row in tmp:
                writer.writerow(row)


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


def request_admin(teacher_id):
    print('+')
