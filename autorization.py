# import teacher as en
import csv


def control(login, password):
    with open('_BD_Users.csv', 'r', encoding='utf-8') as file:
        reader_users = csv.reader(file, delimiter=';')
        for row in reader_users:
            print(row)
            if login == row[0] and password == row[1]:
                status = row[4]
                return status, row


# def control(lg):
    # bases = {'School_System/_BD/_Teacher.csv': ' Teacher', 'School_System/_BD/_Students.csv': ' Student', 'School_System/_BD/_Admin.csv': ' Admin'}
    # bases = '_BD\_Users.csv'
    # for key in bases.keys():
    # with open('_BD\_Users.csv', 'r', encoding='utf-8') as file:
    #     reader = csv.reader(file, delimiter=';')
    #     for row in reader:
    #         if lg in row[0]:
    #             log_th = bases[key]
    #             break
    #         else:
    #             log_th = ' '
                       
    # return log_th

# Fedorov;Victor;Федоров;Виктор;Admin 
# логин  пароль 
# Поиск только по логину!

