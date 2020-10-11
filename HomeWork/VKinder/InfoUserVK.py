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

    def __init__(self, user_id):
        self.user_id = user_id

    def info_user(self):
        info = {}
        response = vk.users.get(user_id=self.user_id, fields='bdate, city, relation, sex')
        info['vk_id'] = response[0]['id']
        info['first_name'] = response[0]['first_name']
        info['last_name'] = response[0]['last_name']
        info['sex'] = response[0]['sex']
        regex = re.compile(r'(\d+)\.(\d+)\.(\d{4})')
        text = response[0]['bdate']
        info['age'] = int(((datetime.now() - datetime(int(regex.sub(r'\3', text)), int(regex.sub(r'\2', text)),
                                                 int(regex.sub(r'\1', text)))).days)/365)
        info['city'] = response[0]['city']['title']
        return info

    def get_photo(self):
        response = vk.photos.get(owner_id=self.user_id, album_id='profile', extended=1, photo_sizes=1)
        photo_list = []
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

    def dating_users(self):
        response = vk.users.search(city=2, has_photo=1, relation=1, status=1, sex=1, age_from=20, age_to=21)
        return response

id = 692651
User = UserVK(id)
pprint(User.dating_users()['items'])
