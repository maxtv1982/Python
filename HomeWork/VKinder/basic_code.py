from random import randrange
import re
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from InfoUserVK import UserVK

token = '40f4cb15dcd7458c34a6a73b75d7e0784bc8fc49dd8f4cbf71970420351d16133fc501d370cd767a59667'
pattern_request = r"(\d+)\,\s*(\d+)\,\s*(\d)\,\s*(\w+)\,\s*(\d)"

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })


for event in longpoll.listen():
    #print(event.type)
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:

        request = event.text

        if re.search('(привет|добрый|здравствуйте)', request.lower()):
            write_msg(event.user_id, f"Привет, {event.user_id}")
        elif re.search('(пока|до свидания)', request.lower()):
            write_msg(event.user_id, "до свидания")
        elif re.search('(познакомится|ищу)', request.lower()):
            write_msg(event.user_id,
                      "Я помогу Вам найти пару. Введите параметры через запятую: диапазон возраста - от, до;"
                      " пол (1 — женщина; 2 — мужчина); город; семейное положение (1 — не женат (не замужем);"
                      "2 — встречается; 3 — помолвлен(-а); 4 — женат (замужем); 5 — всё сложно; 6 — в активном поиске;"
                      " 7 — влюблен(-а); 8 — в гражданском браке)")
        elif re.search(pattern_request, request.lower()):
            write_msg(event.user_id, "Спасибо, сейчас поищу ...")
            info = request.split(',')
            inform = {'hometown': info[3], 'status': info[4], 'sex': info[2], 'age_from': info[0], 'age_to': info[1]}
            id_using = []
            for id in UserVK(event.user_id).dating_users(inform):
                id_using.append(id)
                for photo in UserVK(id).get_photo():
                    write_msg(event.user_id, photo['photo'])
                write_msg(event.user_id, "Next/End")
                if re.search('end', request.lower()):
                    write_msg(event.user_id, f"спасибо, {event.user_id}")
                    break

        else:
            write_msg(event.user_id, "Не поняла вашего ответа...")
