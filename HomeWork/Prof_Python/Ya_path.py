import os
import requests
import unittest
import json
from pprint import pprint

def Yandex_path():
    with open(os.path.join("..", "..", "..", "key.txt")) as f:
        f.readline().rstrip()
        token_ya = f.readline().rstrip()

    URL = 'https://cloud-api.yandex.net:443/v1/disk/'
    headers = {'Authorization': token_ya}

    # создаём папку на яндекс диске
    params = {'path': '/new_Path'}
    resp = requests.put(URL + 'resources', params=params, headers=headers)

    if resp.status_code == 201:
        resp_ya = requests.get(URL + 'resources', params={'path': '/'}, headers=headers)
        resp_json = resp_ya.json()
        for item in resp_json['_embedded']['items']:
            if item['name'] == 'new_Path':
                return True
    elif resp.status_code == 409:
        return False




class TestSomething(unittest.TestCase):

    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    # тест для создания новой папки
    def test_Yandex_path_OK(self):
        self.assertEqual(Yandex_path(), True)

    # # тест для проверки уже существующей папки
    # def test_Yandex_path_Bad(self):
    #     self.assertEqual(Yandex_path(), False)

if __name__ == '__main__':
    unittest.main()

