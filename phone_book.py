import tkinter as tk
import json






def new():
    name = input('Введите имя абонента ')
    phone = input('Введите телефоны абонента через запятую ').split(',')
    email = input('Введите электронный адрес ')
    if "@" in email:
        phone_book[name] = {'phones': phone, 'email': email}
    else:
        phone_book[name] = {'phones': phone}


def edit():
    name_1 = input('Введите имя контакта, который хотите изменить ')
    print(phone_book[name_1])
    param = int(input(
        'Введите параметр, который хотите изменить:\nИмя абонента - введите 1\nТелефон абонента - введите 2\nEmail - введите 3 '))
    if param == 3:
        phone_book[name_1]['email'] = input('Введите новый email ')
        print(f'Контакт успешно изменен \n{phone_book[name_1]}')
    if param == 2:
        answer = int(input(
            'Чтобы удалить номер телефона - введите: 1\nЧтобы изменить номер телефона - введите: 2\nЧтобы добавить номер телефона - введите: 3 '))
        if answer == 1:
            num = int(input('Введите порядковый номер телефона, который хотите удалить '))
            del (phone_book[name_1]['phones'])[num - 1]
            print(f'Контакт успешно изменен \n{phone_book[name_1]}')
        if answer == 2:
            phone = int(input('Введите новый номер телефона '))
            if len(phone_book[name_1]['phones']) > 1:
                num = int(input('Введите порядковый номер телефона, который хотите изменить '))
                phone_book[name_1]['phones'][num - 1] = phone
            else:
                phone_book[name_1]['phones'][0] = phone
            print(f'Контакт успешно изменен \n{phone_book[name_1]}')
        if answer == 3:
            phone = int(input('Введите новый номер телефона '))
            (phone_book[name_1]['phones']).append(phone)
            print(f'Контакт успешно изменен \n{phone_book[name_1]}')
    if param == 1:
        name_2 = input('Введите новое имя абонента ')
        phone_book[name_2] = phone_book.pop(name_1)
        print(f'Контакт успешно изменен \n{phone_book[name_2]}')

def delete():
    name_1 = input('Введите имя контакта, который хотите удалить ')
    choice = input('Подвердите удаление Y/N ').lower()
    if choice == 'y':
        del phone_book[name_1]
    print(phone_book.keys())



def save():
    with open('phone_book.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
    print('Изменения успешно сохранены ')


def load():
    with open('phone_book.json', 'r', encoding='utf-8') as fh:
        phone_book = json.load(fh)
    print('Телефонная книга успешно загружена')
    return phone_book


phone_book = load()

while True:
    command = input('Введите команду ')
    if command == '/start':
        print('Добро пожаловать в вашу телефонную книгу')
    elif command == '/stop':
        break
    elif command == '/all':
        print(*phone_book.keys(), sep=', ')

    elif command == '/new':
        new()
    elif command == '/save':
        save()
    elif command == '/show':
        name_1 = input('Введите имя абонента ')
        for key,val in phone_book[name_1].items():

            if type(val) == list:
                print(key,*val)
            else:
                print(key,val)

    elif command == '/del':
        delete()
    elif command == '/edit':
        edit()
