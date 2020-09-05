documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def name_by_number():
    ''' give information about name
    by given number of document '''
    number_doc = input('введите номер документа: ')
    n = 0
    for document in documents:
        if document["number"] == number_doc:
            n += 1
            print(document["name"])
    if n == 0:
        print('документ с данным номером отсутствует')


def shelf_by_number():
    ''' give information about number of shelf
    by given number of document '''
    number_doc = input('введите номер документа: ')
    n = 0
    for shelf in directories.items():
        for i in shelf[1]:
            if i == number_doc:
                n += 1
                print(f'ваш документ на полке № {shelf[0]}')
    if n == 0:
        print('документ с данным номером отсутствует')


def all_docs():
    ''' give information about all
    documents '''
    for document in documents:
        print(f'{list(document.values())[0]} "{list(document.values())[1]}" "{list(document.values())[2]}"')


def add_document():
    ''' add new document by type, number, name of owner and number of shelf '''
    new_doc = input('тип, номер, имя владельца документа и номер полки через запятую без пробелов: ').split(',')
    n = 0
    for shelf, docs in directories.items():
        if shelf[0] == new_doc[3]:
            n += 1
            docs.append(new_doc[1])
    if n == 0:
        print('неправильный номер полки')
    else:
        documents.append({"type": new_doc[0], "number": new_doc[1], "name": new_doc[2]})
    print(documents)
    print(directories)


def delete_by_number():
    ''' delete information about document
    by given number of document '''
    number_doc = input('введите номер документа: ')
    n = 0
    for document in documents:
        if document["number"] == number_doc:
            n += 1
            del (documents[documents.index(document)])
    if n == 0:
        print('документ с данным номером отсутствует')
    print(documents)
    for shelf in directories.items():
        for i in shelf[1]:
            if i == number_doc:
                del (shelf[1][shelf[1].index(i)])
    print(directories)


def move_document():
    ''' move document by number to new shelf, which will be point '''
    move_doc = input('номер документа и номер полки через запятую без пробелов: ').split(',')
    n = 0
    m = 0
    for shelf, docs in directories.items():
        if shelf[0] == move_doc[1]:
            m += 1
            break
    if m == 0:
        print('неправильный номер полки')
    else:
        for shelf, docs in directories.items():
            for i in docs:
                if i == move_doc[0]:
                    n += 1
                    del (docs[docs.index(i)])
        if n == 0:
            print('документ с данным номером отсутствует')
        else:
            docs.append(move_doc[0])
    print(directories)


def add_shelf():
    ''' add new shelf number '''
    new_doc = input('введите номер новой полки : ')
    n = 0
    for shelf in directories.items():
        if shelf[0] == new_doc:
            n += 1
    if n != 0:
        print('полка уже существует')
    else:
        directories[new_doc] = []
    print(directories)


def main():
    ''' chooze the function '''
    i = int(
        input('введите номер задачи (1 - people, 2 - shelf, 3 - list, 4 - add, 5 - delete, 6 - move, 7 - add shelf) :'))
    if i == 1:
        name_by_number()
    elif i == 2:
        shelf_by_number()
    elif i == 3:
        all_docs()
    elif i == 4:
        add_document()
    elif i == 5:
        delete_by_number()
    elif i == 6:
        move_document()
    elif i == 7:
        add_shelf()
    else:
        print('неправильный номер задачи')


main()