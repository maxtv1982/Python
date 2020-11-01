import requests
import vk_api
import os
from datetime import timedelta, datetime
import re
from pprint import pprint

with open(os.path.join("..", "..", "..", "key.txt")) as f:
    token = f.readline().rstrip()
# Подключение к VK API
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()


class UserVK:
    """ сбор ифнормации из vk api по определённым параметрам"""

    def __init__(self, user_id):
        self.user_id = user_id

    def info_user(self):
        """получаем необходимую информацию о пользователе по его id """
        info = {}  # словарь с данными
        response = vk.users.get(user_id=self.user_id, fields='bdate, city, relation, sex')
        info['vk_id'] = response[0]['id']
        info['first_name'] = response[0]['first_name']
        info['last_name'] = response[0]['last_name']
        info['sex'] = response[0]['sex']
        regex = re.compile(r'(\d+)\.(\d+)\.(\d{4})')
        text = response[0]['bdate']
        info['age'] = int(((datetime.now() - datetime(int(regex.sub(r'\3', text)), int(regex.sub(r'\2', text)),
                                                      int(regex.sub(r'\1', text)))).days) / 365)
        info['city'] = response[0]['city']['title']
        return info

    def get_photo(self):
        """ получаем ссылку на 3 популярных фотографии с аватара пользователя по его id """
        response = vk.photos.get(owner_id=self.user_id, album_id='profile', extended=1, photo_sizes=1)
        photo_list = []  # список 3-х словарей {'likes':колличество, 'photo': ссылка}
        for photo in response['items']:
            download_photo = ''
            type_size = 'a'
            # ищем ссылку на фотографию с максимальным размером
            for size in photo['sizes']:
                if size['type'] > type_size:
                    type_size = size['type']
                    download_photo = size['url']
            photo_info = {'likes': photo['likes']['count'], 'photo': download_photo}
            photo_list.append(photo_info)
        photo_list.sort(key=lambda x: x['likes'], reverse=True)
        photos_for_user = photo_list[0:3]
        return photos_for_user

    def dating_users(self, search_info):
        """ по заданным параметрам ищем пользователей и возвращаем список их id"""
        id_persons = []
        response = vk.users.search(hometown=search_info['hometown'], has_photo=1,
                                   status=search_info['status'], sex=search_info['sex'],
                                   age_from=search_info['age_from'], age_to=search_info['age_to'])
        for person in response['items']:
            if not vk.users.get(user_id=person['id'], fields='is_closed')[0]['is_closed']:
                id_persons.append(person['id'])
        return id_persons


# id = 692651
# User = UserVK(id)
# inform = {'hometown': 'Москва', 'status': 1, 'sex': 1, 'age_from': 20, 'age_to':21}
# pprint(User.dating_users(inform))
