import os

os.chdir(os.path.dirname(__file__))

def user_add():

    db_admin = []

    db_admin.append(input("Введи логин -> "))
    db_admin.append(input("Введи пароль -> "))
    db_admin.append(input("Введи имя -> "))
    db_admin.append(input("Введи фамилию -> "))
    db_admin.append(input("Введи описание (админ, учитель, ученик) -> "))

    with open("_BD/_Users.csv", "a", encoding='utf-8') as file_csv:
        file_csv.write("{};{};{};{};{}\n".format(db_admin[0], db_admin[1], db_admin[2], db_admin[3], db_admin[4]))


def find_user():
    # try:
        word = input("Введи искомое значение -> ")
        with open('_BD/_Users.csv', 'r', encoding='utf-8') as file_csv:
            content = list(map(str, file_csv.read().split('\n')))

        temp = []
        for i, v in enumerate(content):
            if word.lower() in v.lower():
                temp.append(v)
        if len(temp) == 0:
            print("Ничего не найдено!")
        else:
            for i in temp:
                print(i)
        # Logger.log_logger('Find_Finder', True)
    # except:
        # Logger.log_logger('Find_Finder', False)


def delete_user():
    # try:
        word = str(input("Введи искомое значение для удаления (можно часть начала логина) -> "))
        with open(r'_BD/_Users.csv', 'r+', encoding='utf-8') as file_csv:
            content = file_csv.readlines()
            file_csv.seek(0)
            for line in content:
                if word not in line:
                    file_csv.write(line)
            file_csv.truncate()


    #     Logger.log_logger('Find_Finder', True)
    # # except:
    #     Logger.log_logger('Find_Finder', False)

def view_applications():
    with open(r'_BD/_Requests.csv', 'r+', encoding='utf-8') as file_csv:
        while True:
            line = file_csv.readline()
            if not line:
                break
            print(line.strip())


user_add()