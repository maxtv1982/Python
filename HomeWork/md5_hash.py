import hashlib


def Hash(file_for_hash):
    with open(file_for_hash) as file_read:
        for string in file_read:
            string = file_read.readline().rstrip()
            hash_object = hashlib.md5(string.encode())
            yield hash_object.hexdigest()


file = input('введите путь к файлу:  ')
md5 = Hash(file)
print(next(md5))
print(next(md5))
print(next(md5))
