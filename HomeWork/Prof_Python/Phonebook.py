from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

new_list = []


# for string in contacts_list:
#     for item in string:
#         print(item)
pattern = r"(\+7|8)?\s*\(\s*(\d+)\s*\)\s*(\d+)(\s*|-?)(\d+)(\s*|-?)(\d+)"
phone = re.compile(pattern)
m = phone.sub(r"+7 (\2) \3-\5-\7", 'Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,')
print(m)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook_new.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
