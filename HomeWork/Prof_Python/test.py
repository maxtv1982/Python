import re

pattern = r"(\+7|8)?\s*\(\s*(\d+)\s*\)\s*(\d+)(\s*|-?)(\d+)(\s*|-?)(\d+)"
regex = re.compile(pattern)
text = ",,8 495-913-0168,Мартиняхин,Виталий,Геннадьевич,ФНС,Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),"
text2 = regex.findall(text)
print(text2)

