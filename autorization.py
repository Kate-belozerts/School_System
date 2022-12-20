# import teacher as en
import csv

def control(lg):
    bases = {'School_System/_BD/_Teacher.csv': ' Teacher', 'School_System/_BD/_Students.csv': ' Student', 'School_System/_BD/_Admin.csv': ' Admin'}
    for key in bases.keys():
            with open(f'{key}', 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    if lg in row[1]:
                        log_th = bases[key]
                        break
                    else:
                        log_th = ' '
                       
    return log_th


# Поиск только по логину!