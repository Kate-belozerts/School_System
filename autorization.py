import csv


def control(login, password):
    with open('_BD\_Users.csv', 'r', encoding='utf-8') as file:
        reader_users = csv.reader(file, delimiter=';')
        for row in reader_users:
            if login in row[0] and password in row[1]:
                status = row[4]
                return status
            # else:
            #     print('Введен неверный логин или пароль. Попробуйте снова')

# status = control(' ', ' ')
# print(status)


