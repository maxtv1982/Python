import os
import sys
import time
import requests
from tqdm import tqdm


class UserVK:

    def __init__(self, UserID):
        self.UserID = UserID
        # создаем пустой список фотографий
        self.photo_base = []

    def get_photo_album(self, album, count):
        """ копирования фотографий с профиля(стены) пользователя vk на компьютер """
        response = requests.get('https://api.vk.com/method/photos.get',
                                params={'access_token': token_vk, 'owner_id': self.UserID, 'album_id': album,
                                        'extended': 1, 'photo_sizes': 1, 'count': count, 'rev': 1, 'v': 5.21})
        if response.status_code == 200 and 'error' not in response.json().keys():
            # собираем информацию по каждой фотографии и загружаем на компьютер
            print(' <<< загружаем фотографии с профиля(стены) пользователя vk >>> ')
            for photo in response.json()['response']['items']:

                download_photo = ''
                type_size = 'a'
                # ищем ссылку на фотографию с максимальным размером
                for size in photo['sizes']:
                    if size['type'] > type_size:
                        type_size = size['type']
                        download_photo = size['src']
                # создаём словарь с иформацией о фотографии
                photo_info = {'file_name': photo['likes']['count'], 'size': type_size}
                # если количество лайков одинаково, то добавить дату загрузки
                if photo['likes']['count'] in (photos['file_name'] for photos in self.photo_base):
                    photo_info['file_name'] = f"{photo['likes']['count']}_{photo['date']}"
                # добаляем словарь с иформацией о фотографии в базу фотографий
                self.photo_base.append(photo_info)
                # загружаем фотографию на компьютер
                download = requests.get(download_photo)
                # прогресс-бар для каждого файла
                for i in tqdm(range(1)):
                    time.sleep(0.005)

                name_photo = f"{photo_info['file_name']}.jpg"
                with open(os.path.join("C:\Photo_VK", name_photo), 'wb') as f:
                    f.write(download.content)
            print(f'список загруженных файлов - {self.photo_base}')
        else:
            sys.exit('Некорректные данные пользователя VK')

    def upload_photo_Yandex(self, key):
        """ отправляем фотографий с профиля(стены) пользователя vk с компьютера на Яндекс.диск """

        URL = 'https://cloud-api.yandex.net:443/v1/disk/'
        headers = {'Authorization': key}

        # создаём папку на яндекс диске
        params = {'path': '/Photo_VK'}
        resp = requests.put(URL + 'resources', params=params, headers=headers)

        print(' <<< отправляем фотографии на Яндекс.диск >>>')
        for photo in self.photo_base:

            photo_name = f"{photo['file_name']}.jpg"
            # открываем загружаемый файл
            with open(os.path.join("C:\Photo_VK", photo_name), 'rb') as new_file:
                my_file = new_file.read()

            # получаем загрузочную ссылку
            params_file = {'path': '/Photo_VK/' + photo_name}
            url_upload = requests.get(URL + 'resources/upload', params=params_file, headers=headers, )
            if url_upload.status_code == 200:
                href = url_upload.json()['href']
                # используя ссылку загружаем файл на диск
                upload_file = requests.put(href, data=my_file)
                # прогресс-бар для каждого файла
                for i in tqdm(range(1)):
                    time.sleep(0.005)

                if upload_file.status_code == 201:
                    print('Success!')
                else:
                    print('Ошибка загрузки')
            else:
                print('Ошибка запроса, возможно файл с таким именем уже существует')


if __name__ == '__main__':
    # with open('C:\key.txt') as f:
    #     token_vk = f.readline().rstrip()
    #     token_ya = f.readline().rstrip()
    #
    # id_user = 552934290
    # album = 'profile'
    # count = 3

    id_user = input('Введите id пользователя: ')
    album = input('Из какого альбома нужно сохранить фотографии (wall/profile) : ')
    count = input('Сколько фотографий сохранить: ')
    token_vk = input('Введите токен для VK api: ')
    token_ya = input('Введите токен с Полигона Яндекс.Диска: ')

    User = UserVK(id_user)
    User.get_photo_album(album, count)
    User.upload_photo_Yandex(token_ya)
