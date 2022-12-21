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
    class_list = ['5А', '6А', '10А']
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
    lesson_id = teacher_id[4]
    lesson_date = date.today().strftime('%d.%m.%Y')
    class_id = class_existence_checker(
        f'{" ".join(teacher_id[2:4])}, какому классу будет Д/З: ')

    homework_file = r'_BD\{}{}_HW.csv'.format(
        class_id, lesson_id)
    homework = input(f'Какое Д/З будет у {class_id}?\n')
    homework = [[lesson_date, lesson_id, homework]]

    with open(homework_file, 'a', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for row in homework:
            writer.writerow(row)
    print('Домашнее задание добавлено.')


def knowledge_rater(teacher_id):
    subject_one = 'Математика'
    subject_two = 'Русский'
    lesson_id = teacher_id[4] # Математика
    student_id = input('Введите Фамилию и Имя ученика через пробел: ').replace(' ', ';')
    knowledge_rating = str(rater_input_checker('Введите оценку: '))
    with open ('_BD\_Marks.csv', 'r', encoding='utf-8-sig') as file:
        file = list(map(str, file.read().split()))
        temp = list(filter(lambda x: student_id not in x, file)) # Без ученка для выставления оценки
        file = list(filter(lambda x: student_id in x, file))
        file = [i.split(';') for i in file]

        if subject_one == lesson_id:
            end_position = subject_two
        elif subject_two == lesson_id:
            end_position = subject_one

        result = []
        [[result.append(j) for j in i] for i in file]
        print(result)
        if end_position in result[5]:
            end_position = result[5]
        elif end_position in result[11]:
            end_position = result[11]
        class_id = result[4] # 5A
        name = '' # Anufriev;Nikita;Ануфриев;Никита;5А;
        for i in range(5):
            name += result[i] + ';'
        result = list(filter(lambda i: lesson_id in i, result)) # ['Математика:2,5,4']
        new = f'{result[0]},{knowledge_rating}' # Математика:2,5,4,5
        result = name + new #Anufriev;Nikita;Ануфриев;Никита;5А;Математика:2,5,4,5
        end_position = name + end_position
        print(f'Оценка {knowledge_rating} выставлена ученику {class_id}-класса: {student_id}, по предмету: {lesson_id}')
    
    with open ('_BD\_Marks.csv', 'w', encoding='utf-8-sig') as file:
        for i in range(len(temp)):
            file.write(temp[i])
            file.write('\n')
        file.write(result)
        file.write('\n')
        file.write(end_position)


def student_finder(student_id, class_id):
    student_id = student_id.split()
    student_id.append(class_id)
    print(student_id)
    path_id = r'..\DataBase\{}_Класс'.format(class_id)
    students_list = r'{}\{}_Список_Учеников.csv'.format(
        dir_maker(path_id), class_id)
    with open(students_list, 'r', encoding='utf-8-sig') as file:
        for line in file:
            print(line)


def request_admin(teacher_id):
    message = str(input('Введите запрос: '))
    question = (f'{message}, From {teacher_id}')
    time = str(date.today()) + ' - '
    with open ('_BD\_Requests.csv', 'a', encoding='utf-8-sig') as send:
        send.write(time)
        send.write(question)
        send.write(f'\n')

