import hashlib
import json
from datetime import datetime


def make_log(fn):
    log = dict()

    def wrapped(*args):
        log['дата и время вызова'] = str(datetime.today())
        log['название функции'] = fn.__name__
        log['аргумегы'] = args
        log['результат выполнения'] = next(fn(*args))
        print(log)
        with open("logs.json", "a", encoding="utf-8") as log_file:
            json.dump(log, log_file, ensure_ascii=False, indent=4)
        return fn(*args)

    return wrapped


@make_log
def Hash(file_for_hash):
    with open(file_for_hash) as file_read:
        for string in file_read:
            string = file_read.readline().rstrip()
            hash_object = hashlib.md5(string.encode())
            yield hash_object.hexdigest()


file = input('введите путь к файлу:  ')

md5 = Hash(file)

print(next(md5))

