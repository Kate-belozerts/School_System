import csv


def control(login, password):
    with open('_BD\_Users.csv', 'r', encoding='utf-8') as file:
        reader_users = csv.reader(file, delimiter=';')
        for row in reader_users:
            if login == row[0] and password == row[1]:
                status = row[5]
                return status, row


