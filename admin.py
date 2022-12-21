import os
import csv

import os

os.chdir(os.path.dirname(__file__))

def user_add(admin_id):
    
    print(f'{admin_id[0]} {admin_id[1]}, введите информацию: ')
    db_admin = []

    db_admin.append(input("Введите логин -> "))
    db_admin.append(input("Введите пароль -> "))
    db_admin.append(input("Введите фамилию -> "))
    db_admin.append(input("Введите имя -> "))
    db_admin.append(input("Введите подразделение -> "))
    db_admin.append(input("Введите описание (Admin, Teacher, Student) -> "))

    with open("_BD/_Users.csv", "a", encoding='utf-8-sig') as file_csv:
        file_csv.write("\n{};{};{};{};{};{}".format(db_admin[0], db_admin[1], db_admin[2], db_admin[3], db_admin[4], db_admin[5]))
    print(f'Пользователь {db_admin[2:4]} добавлен')


def delete_user(admin_id):
    # try:
        word = str(input(f"{admin_id[0]} {admin_id[1]}, введите искомое значение для удаления (можно часть начала логина) -> "))
        with open(r'_BD/_Users.csv', 'r+', encoding='utf-8-sig') as file_csv:
            content = file_csv.readlines()
            file_csv.seek(0)
            for line in content:
                if word not in line:
                    file_csv.write(line)
            file_csv.truncate()
        print('Пользователь удален.')


    #     Logger.log_logger('Find_Finder', True)
    # # except:
    #     Logger.log_logger('Find_Finder', False)

def view_applications(admin_id):
    print(f'{admin_id[0]} {admin_id[1]}, введите информацию: ')
    with open(r'_BD/_Requests.csv', 'r+', encoding='utf-8-sig') as file_csv:
        while True:
            line = file_csv.readline()
            if not line:
                break
            print(line.strip())
