import os
import sys
import requests
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build


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
                name_photo = f"{photo_info['file_name']}.jpg"
                with open(os.path.join("..", "Photo_VK", name_photo), 'wb') as file:
                    file.write(download.content)
                print(f" - фотография {name_photo} загружена c VK на компьютер -")
            print(f'список загруженных файлов - {self.photo_base}')
        else:
            sys.exit('Некорректные данные пользователя VK')


class YandexAPIClient(UserVK):

    def upload_photo_Yandex(self, key_ya):
        """ отправляем фотографий с профиля(стены) пользователя vk с компьютера на Яндекс.диск """

        URL = 'https://cloud-api.yandex.net:443/v1/disk/'
        headers = {'Authorization': key_ya}

        # создаём папку на яндекс диске
        params = {'path': '/Photo_VK'}
        resp = requests.put(URL + 'resources', params=params, headers=headers)

        print(' <<< отправляем фотографии на Яндекс.диск >>>')
        for photo in self.photo_base:

            photo_name = f"{photo['file_name']}.jpg"
            # открываем загружаемый файл
            with open(os.path.join("..", "Photo_VK", photo_name), 'rb') as new_file:
                my_file = new_file.read()

            # получаем загрузочную ссылку
            params_file = {'path': '/Photo_VK/' + photo_name}
            url_upload = requests.get(URL + 'resources/upload', params=params_file, headers=headers, )
            if url_upload.status_code == 200:
                href = url_upload.json()['href']
                # используя ссылку загружаем файл на диск
                upload_file = requests.put(href, data=my_file)
                if upload_file.status_code == 201:
                    print(f" - фотография {photo_name} загружена на Яндекс.диск -")
                else:
                    print('Ошибка загрузки')
            else:
                print('Ошибка запроса, возможно файл с таким именем уже существует')


class GoogleAPIClient(UserVK):

    def upload_photo_Google(self, folder_id, service_key):
        """ отправляем фотографий с профиля(стены) пользователя vk с компьютера на Google.диск """
        # Указываем Scopes. Scopes — это перечень возможностей, которыми будет обладать сервис, созданный в скрипте.
        scopes = ['https://www.googleapis.com/auth/drive']
        # указываем путь к файлу с ключами сервисного аккаунта
        service_account_file = os.path.join("..", "..", service_key)
        # Создаем credentials (учетные данные), указав путь к сервисному аккаунту, а также заданные Scopes.
        credentials = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=scopes)
        # создаем сервис, который будет использовать 3ю версию REST API Google Drive,
        # отправляя запросы из-под учетных данных credentials.
        service = build('drive', 'v3', credentials=credentials)
        # создание папки делается с помощью метода create
        name = 'Photo_VK'
        file_metadata = {'name': name, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [folder_id]}
        result = service.files().create(body=file_metadata, fields='id').execute()
        folder_id_vk = result['id']
        # загрузка файла в папку
        print(' <<< отправляем фотографии на Google.диск >>>')
        for photo in self.photo_base:
            photo_name = f"{photo['file_name']}.jpg"
            file_path = os.path.join("..", "Photo_VK", photo_name)
            file_metadata = {'name': photo_name, 'parents': [folder_id_vk]}
            media = MediaFileUpload(file_path, resumable=True)
            r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'- фотография {photo_name} c id - {r["id"]} загружена на Google.диск -')


if __name__ == '__main__':
    with open(os.path.join("..", "..", "key.txt")) as f:
        token_vk = f.readline().rstrip()
        token_ya = f.readline().rstrip()

    id_user = 552934290
    album = 'profile'
    count = 3
    folder_parent = '17kd8jJyLUZuNi2Br4TXWyxarkXZdjFiX'
    key = "river-runner-283818-aa3dd09a7020.json"

    # id_user = input('Введите id пользователя: ')
    # album = input('Из какого альбома нужно сохранить фотографии (wall/profile) : ')
    # count = input('Сколько фотографий сохранить: ')
    # token_vk = input('Введите токен для VK api: ')
    disk = input('На какой диск копировать (Google, Yandex - G/Y/G+Y) : ')

    # User = UserVK(id_user)
    # User.get_photo_album(album, count)

    if disk == 'G':
        # folder_parent = input('Введите id корневой папки Google.Диска: ')
        # key = input('Введите название ключа для сервисного аккаунта в формате JSON для Google.Диска: ')
        User = GoogleAPIClient(id_user)
        User.get_photo_album(album, count)
        User.upload_photo_Google(folder_parent, key)
    elif disk == 'Y':
        # token_ya = input('Введите токен с Полигона Яндекс.Диска: ')
        User = YandexAPIClient(id_user)
        User.get_photo_album(album, count)
        User.upload_photo_Yandex(token_ya)
    elif disk == 'G+Y':
        # folder_parent = input('Введите id корневой папки Google.Диска: ')
        # key = input('Введите название ключа для сервисного аккаунта в формате JSON для Google.Диска: ')
        UserGoogle = GoogleAPIClient(id_user)
        UserGoogle.get_photo_album(album, count)
        UserGoogle.upload_photo_Google(folder_parent, key)
        # token_ya = input('Введите токен с Полигона Яндекс.Диска: ')
        UserYandex = YandexAPIClient(id_user)
        UserYandex.photo_base = UserGoogle.photo_base
        # UserYandex.get_photo_album(album, count)
        UserYandex.upload_photo_Yandex(token_ya)
    else:
        print('некорректно указан диск')
