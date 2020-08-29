import json
from datetime import datetime


def make_log_to_path(path):
    def make_log(fn):
        log = dict()

        def wrapped(*args):
            log['дата и время вызова'] = str(datetime.today())
            log['название функции'] = fn.__name__
            log['аргумегы'] = args
            log['результат выполнения'] = fn(*args)
            print(log)
            with open(path + "logs.json", "a", encoding="utf-8") as file:
                json.dump(log, file, ensure_ascii=False, indent=4)
            return fn(*args)

        return wrapped

    return make_log


path_user = input('введите путь к файлу: ')


@make_log_to_path(path_user)
def summa(a, b):
    return a + b


print(summa(11, 10))
