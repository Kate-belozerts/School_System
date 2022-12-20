# import teacher as en
import csv


def teacher(login):
    # log_th = False
    with open('8S_HW\_Teacher.csv', 'r', encoding='utf-8') as file:
        reader_teacher = csv.reader(file, delimiter=';')
        for row in reader_teacher:
            if login in row[3]:
                log_th = True
                break
            else:
                log_th = False
    return log_th


def teacher1(password):
    # pas_th = False
    with open('8S_HW\_Teacher.csv', 'r', encoding='utf-8') as file:
        reader_teacher = csv.reader(file, delimiter=';')
        for row in reader_teacher:
            if password in row[3]:
                pas_th = True
                break
            else:
                pas_th = False
    return pas_th


def students(login):
    # a = False
    with open('8S_HW\_Students.csv', 'r', encoding='utf-8') as file:
        reader_students = csv.reader(file, delimiter=';')
        for row in reader_students:
            if login in row[3]:
                log_st = True
                break
            else:
                log_st = False
    return log_st


def students1(password):
    # a = False
    with open('8S_HW\_Students.csv', 'r', encoding='utf-8') as file:
        reader_students = csv.reader(file, delimiter=';')
        for row in reader_students:
            if password in row[3]:
                pas_st = True
                break
            else:
                pas_st = False
    return pas_st


def admin(login):
    pas_ad = False
    with open('8S_HW\_Admin.csv', 'r', encoding='utf-8') as file:
        reader_admin = csv.reader(file, delimiter=';')
        for row in reader_admin:
            if login in row[3]:
                pas_ad = True
                break
            else:
                pas_ad = False
        return pas_ad


def admin1(password):
    pas_ad = False
    with open('8S_HW\_Admin.csv', 'r', encoding='utf-8') as file:
        reader_admin = csv.reader(file, delimiter=';')
        for row in reader_admin:
            if password in row[3]:
                pas_ad = True
                break
            else:
                pas_ad = False
        return pas_ad
