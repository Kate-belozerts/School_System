import os
import csv

os.chdir(os.path.dirname(__file__))

def user_add(login='', passwrd='', name='', surname='', description=''):

    db_admin = []

    db_admin.append(login)
    db_admin.append(passwrd)
    db_admin.append(name)
    db_admin.append(surname)
    db_admin.append(description)

    with open("db_access.csv", "a", encoding='utf-8') as file_csv:
        file_csv.write("{};{};{};{};{}\n".format(db_admin[0], db_admin[1], db_admin[2], db_admin[3], db_admin[4]))

# def user_delete()



lo = 'Sysadm'
ps = 'qwe123'
n = "Иван"
s = "Петров"
d = "Админ"


user_add(lo, ps, n, s, d)