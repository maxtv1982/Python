import re
from pprint import pprint
import csv

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
book = []

# из каждой строки создаём словарь, параллельно распределяем ФИО и удаляем дубли
# и добавляем во временный список book
for result in contacts_list:
    fio = result[0] + ' ' + result[1] + ' ' + result[2]
    FIO = re.findall(r'\w+', fio)
    if len(FIO) < 3:
        FIO.append(' ')
    info = dict()
    for x in range(0, 3):
        info[x] = FIO[x]
    for x in range(3, 7):
        info[x] = result[x]
    n = 0
    # ищем дубли и добавляем информацию из них всуществующий словарь
    for item in book:
        if (info[0] in item[0]) and (info[1] in item[1]):
            n += 1
            for x in range(3, 7):
                if not item[x]:
                    item[x] = info[x]
    if n == 0:
        book.append(info)

contacts_list_new = []
# итерируемся по списку словарей и в каждом словаре исправляем телефонный номер
pattern = r"(\+7|8)?\s*\(?\s*(\d{3})\)?(\s|-)*(\d{3})(\s|-)*(\d{2})(\s|-)*(\d{2})\s*\(?(\доб.)?\s*(\d+)*\)?"
regex = re.compile(pattern)
for item in book:
    text = regex.sub(r"+7 (\2)\4-\6-\8 доб.\10", item[5])
    item[5] = text
    contacts_list_new.append(list(item.values()))

# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list_new)
  print('адресная книга исправлена')
