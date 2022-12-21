# Информационная система для Школы - "Школик ver.1"


## Описание задачи

Создать информационную систему позволяющую работать с сотрудниками некой компании\студентами вуза\учениками школы


## Команда 

Данное задание выполнялось в составе команды №4:
- Денис Щанников - https://github.com/DenisPotorsky
- Николай Сабайкин - https://github.com/MoJIoToK
- Екатерина Белозерцева - https://github.com/Kate-belozerts
- Ярослав Сысоев - https://github.com/YarrS1986
- Валерий Смекалов - https://github.com/GungsterAXEL
- Тимофей Дашковский


## Структура программы

Программа разделена на несколько модулей, каждый из которых выполняет свою функцию:

1. main - основной модуль, активирует работу программы
2. menu - модуль взаимодействия с пользователем, активирует функции в нижеописанных модулях взависимости от выбора пользователя  
3. teacher - модуль с функционалом преподавателя
4. student - модуль с функционалом студента
5. admin - модуль с функционалом администратора системы
6. autorization - модуль авторизации пользователя

## Краткое описание работы программы

\\\

\\\

## Недостатки и идеи для доработки

1. Малое количество функций.
2. Нерациональное использование баз данных. В модуле `teacher.py` файл `_Marks.csv` перезаписываем каждый раз при добавлении новой оценки. Структура БД не прозрачна, необходимо её упорядочить.