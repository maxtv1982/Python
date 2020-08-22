import requests

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        with open('C:\key.txt') as f:
           key = f.read()
        URL = 'https://cloud-api.yandex.net:443/v1/disk/'
        headers = {'Authorization': key}

        # создаём папку на яндекс диске
        params = {'path': '/my_folder'}
        resp = requests.put(URL + 'resources', params=params, headers=headers)

        # открываем загружаемый файл
        file_name = 'second.txt'
        with open(f'C:\my_folder\{file_name}', encoding='utf8') as new_file:
           my_file = new_file.read()

        # получаем загрузочную ссылку
        params_file = {'path': '/my_folder/' + file_name}
        url_upload = requests.get(URL + 'resources/upload', params=params_file, headers=headers, )
        href = url_upload.json()['href']

        # используя ссылку загружаем файл на диск
        upload_file = requests.put(href, data=my_file)
        if upload_file.status_code == 201:
           print('Success!')
        else:
           print('Error')


if __name__ == '__main__':

    uploader = YaUploader(f'C:\my_folder\'second.txt')
    result = uploader.upload()



# просмотр содержимого диска
# resp = requests.get(URL + 'resources', params={'path': '/'}, headers=headers)
# resp_json = resp.json()
# for i in resp_json['_embedded']['items']:
#    print(i['name'])