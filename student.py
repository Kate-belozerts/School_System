import os
from datetime import datetime as dt
os.chdir(os.path.dirname(__file__))


def read_score(name):
    find_puple('mark', name)


def read_HW(name):
    result = find_puple('homework', name)
    subject = int(input('Чтобы посмотреть домашнее задание выберите предмет:\n1 - Математика\n2 - Русский язык\n'))

    if subject == 1:
        fileExt = (f"{result}Математика_HW.csv")
        with open (f'_BD\{fileExt}', 'r', encoding='UTF-8') as file:
            file = map(str, file.read())
            print(f'Для {result} класса домашнее задание по математике:')
            print(*file)
    if subject == 2:
        fileExt = (f"_{result}Русский_HW.csv")
        with open (f'_BD\{fileExt}', 'r', encoding='UTF-8') as file:
            file = map(str, file.read())
            print(f'Для {result} класса домашнее задание по русскому:')
            print(*file)


def request_admin(name):
    message = str(input('Введите запрос: '))
    question = (f'{message}, From {name}')
    time = str(dt.today()) + ' - '
    with open ('_BD\_Requests.csv', 'a', encoding='utf-8-sig') as send:
        send.write(time)
        send.write(question)
        send.write(f'\n')


def find_puple(request, name):
    result = []
    with open ('_BD\_Marks.csv', 'r', encoding='utf-8') as file:
        file = list(map(str, file.read().split()))
        file = list(filter(lambda x: name in x, file)) # данные одного ученика
        file = [i.split(';') for i in file] 
        [[result.append(j) for j in i] for i in file] # объединяет списки в 1 список
        # print(result)
        if request == 'mark':
            lesson = int(input('Какой предмет вас интересует?\nМатематика - нажмите 1\nРусский язык - нажмите 2\n'))
            if lesson == 1:
                result = filter(lambda i: 'Математика' in i, result)
                print(*result)
            if lesson == 2:
                result = filter(lambda i: 'Русский' in i, result)
                print(*result)        

        if request == 'homework':
            # print(result[4])
            return result[4]

