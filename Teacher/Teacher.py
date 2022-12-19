'''
Teacher:
    - Написание ДЗ.
    - Выставление оценок.
    - Запрос админу.
'''
import os
import csv
from datetime import date

os.chdir(os.path.dirname(__file__))


def class_existence_checker(message):
    class_list = ['1А', '1Б', '2А', '2Б', '3А', '3Б', '4А', '4Б', '5А', '5Б']
    class_id = input(message)
    if class_id.upper() not in class_list:
        print('Такого класса не существует!')
        class_id = class_existence_checker(message)
    return class_id.upper()


def homework_adder(teacher_id):
    teacher_id = list(teacher_id.split(';'))
    lesson_subject = teacher_id[2]
    lesson_date = date.today().strftime('%d.%m.%Y')
    class_id = class_existence_checker('Введите, какому классу будет Д/З: ')
    homework_file = r'..\DataBase\{}-ДЗ.csv'.format(class_id)
    homework = input(f'Какое Д/З будет у {class_id}?\n')
    with open(homework_file, 'a') as file:
        file.write(f'{lesson_date};{lesson_subject};{homework}\n')
    print('Домашнее задание добавлено.')


homework_adder('Вадим;Петров;Математика;1234')