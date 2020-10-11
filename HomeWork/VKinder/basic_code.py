from random import randrange
import re
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from InfoUserVK import UserVK

token = '40f4cb15dcd7458c34a6a73b75d7e0784bc8fc49dd8f4cbf71970420351d16133fc501d370cd767a59667'

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })

for event in longpoll.listen():
    print(event.type)
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if re.search('(привет|добрый|здравствуйте)', request.lower()):
                write_msg(event.user_id, f"Привет, {event.user_id}")
            elif re.search('(пока|до свидания)', request.lower()):
                write_msg(event.user_id, "до свидания")
            elif re.search('(познакомится|ищу)', request.lower()):
                write_msg(event.user_id, "Я помогу Вам найти пару. Введите параметры через запятую: диапазон возраста - от, до;"
                                         " пол; город; семейное положение")
            elif re.search(r'(\d+)\,\s*(\d+)\,\s*', request.lower()):
                write_msg(event.user_id, "Спасибо, сейчас поищу ...")
                for photo in UserVK(692651).get_photo():
                    write_msg(event.user_id, photo['photo'])
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")

