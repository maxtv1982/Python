import requests
import time
from tqdm import tqdm
from pprint import pprint

with open('C:\key.txt') as f:
    token_vk = f.readline().rstrip()
    token_ya = f.readline().rstrip()

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
        # собираем информацию по каждой фотографии и загружаем на компьютер
        print(' <<< загружаем фотографии с профиля(стены) пользователя vk >>> ')
        for photo in response.json()['response']['items']:
            # прогресс-бар для каждого файла
            for i in tqdm(range(100)):
                time.sleep(0.01)

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
            for photos in self.photo_base:
                if photo_info['file_name'] == photos['file_name']:
                    photo_info['file_name'] = f"{photo['likes']['count']}_{photo['date']}"
            # добаляем словарь с иформацией о фотографии в базу фотографий
            self.photo_base.append(photo_info)
            # загружаем фотографию на компьютер
            download = requests.get(download_photo)
            with open(f"C:\Photo_VK\{photo_info['file_name']}.jpg", 'wb') as f:
                f.write(download.content)

        print(f'список загруженных файлов - {self.photo_base}')

    def upload_photo_Yandex(self, key):
        """ отправляем фотографий с профиля(стены) пользователя vk с компьютера на Яндекс.диск """

        URL = 'https://cloud-api.yandex.net:443/v1/disk/'
        headers = {'Authorization': key}

        # создаём папку на яндекс диске
        params = {'path': '/Photo_VK'}
        resp = requests.put(URL + 'resources', params=params, headers=headers)

        print(' <<< отправляем фотографии на Яндекс.диск >>>')
        for photo in self.photo_base:
            # прогресс-бар для каждого файла
            for i in tqdm(range(100)):
                time.sleep(0.01)

            photo_name = f"{photo['file_name']}.jpg"
            # открываем загружаемый файл
            with open(f'C:\Photo_VK\{photo_name}', 'rb') as new_file:
                my_file = new_file.read()

            # получаем загрузочную ссылку
            params_file = {'path': '/Photo_VK/' + photo_name}
            url_upload = requests.get(URL + 'resources/upload', params=params_file, headers=headers, )
            if url_upload.status_code == 200:
                href = url_upload.json()['href']
                # используя ссылку загружаем файл на диск
                upload_file = requests.put(href, data=my_file)
                if upload_file.status_code == 201:
                    print('Success!')
                else:
                    print('Error')
            else:
                print('Error')






id_user = 552934290  # input('Введите id пользователя: ')
album = 'profile'  # input('Из какого альбома нужно сохранить фотографии (wall/profile) : ')
count = 3  # int(Сколько Фотографий сохранить: ')
# token_ya = input('Введите токен с Полигона Яндекс.Диска: ')

User = UserVK(id_user)
User.get_photo_album(album, count)
User.upload_photo_Yandex(token_ya)
