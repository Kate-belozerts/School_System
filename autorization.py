# import teacher as en
import csv


def Teacher(password):
    cnt = False
    with open('8S_HW\_Teacher.csv', 'r', encoding='utf-8') as file:
        reader_teacher = csv.reader(file, delimiter=';')
        for row in reader_teacher:
            if password in row[3]:
                cnt = True
                break
            else:
                cnt = False
    return cnt


def Students(password):
    # a = False
    with open('8S_HW\_Students.csv', 'r', encoding='utf-8') as file:
        reader_students = csv.reader(file, delimiter=';')
        for row in reader_students:
            if password in row[3]:
                a = True
                break
            else:
                a = False
    return a


# print(Teacher('Petrova'))
# print(Students('Belova'))

# def admin(password):
#     pas_ad = False
#     with open('8S_HW\_Admin.csv', 'r', encoding='utf-8') as file:
#         reader_admin = csv.reader(file, delimiter=';')
#         for row in reader_admin:
#             if password in row[3]:
#                 pas_ad = True
#                 break
#             else:
#                 pas_ad = False
#         return pas_ad
