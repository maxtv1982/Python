from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build
import pprint
import os
from pprint import pprint

# Указываем Scopes. Scopes — это перечень возможностей, которыми будет обладать сервис, созданный в скрипте.
SCOPES = ['https://www.googleapis.com/auth/drive']
# указываем путь к файлу с ключами сервисного аккаунта
SERVICE_ACCOUNT_FILE = os.path.join("..", "river-runner-283818-aa3dd09a7020.json")
# Создаем credentials (учетные данные), указав путь к сервисному аккаунту, а также заданные Scopes.
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# создаем сервис, который будет использовать 3ю версию REST API Google Drive,
# отправляя запросы из-под учетных данных credentials.
service = build('drive', 'v3', credentials=credentials)
# получить список файлов и папок, к которым имеет доступ сервис
results = service.files().list(pageSize=1000, fields="files(id, name, mimeType, size)").execute()

folder_id = '17kd8jJyLUZuNi2Br4TXWyxarkXZdjFiX'

# создание папки делается с помощью метода create
name = 'VK'
file_metadata = {'name': name, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [folder_id]}
result = service.files().create(body=file_metadata, fields='id').execute()
folder_id_VK = result['id']

# загрузка файла в папку
my_file = '22'
file_path = '../Photo_VK/2.jpg'
file_metadata = {'name': my_file, 'parents': [folder_id_VK]}
media = MediaFileUpload(file_path, resumable=True)
r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

print(r)


