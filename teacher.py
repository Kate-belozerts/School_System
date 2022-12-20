import logger as lg
import autorization as cont
import menu 


def entered_HW(message):
        with open('_5A_Russian_language_HW.csv', 'a') as file:
            writer_score = csv.writer(file, delimiter=';')
            file.write(message)
    
    # if subcommand1 == '1' and subcommand2 == '1' and subcommand3 == '2':
    #     message = input('Введите домашнее задание: ')
    #     with open('8S_HW\_5A_Russian_language_homework.csv', 'a', encoding='utf-8') as file:
    #         file.write(message)
