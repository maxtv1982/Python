import requests

with open('C:\key.txt') as f:
    token = f.read()

class UserVK:

    def __init__(self, UserID):
        self.UserID = UserID

    # метод поиска друзей пользователя UserID
    def friends(self):
        response = requests.get('https://api.vk.com/method/friends.get',
                                params={'access_token': token, 'user_id': self.UserID, 'v': 5.21})
        return response.json()['response']['items']

    # метод поиска общих друзей пользователя user и пользователя UserID
    def common_friends(self, user):
        friends1 = set(self.friends())
        friends2 = set(user.friends())
        return friends1.intersection(friends2)


id_1 = input('Введите id первого пользователя: ')
id_2 = input('Введите id второго пользователя: ')

User1 = UserVK(id_1)
User2 = UserVK(id_2)

print(f'общие друзья пользователей - {User1.common_friends(User2)}')

print(f"профиль пользователя c id={id_1} https://vk.com/id{id_1}")
print(f"профиль пользователя c id={id_2} https://vk.com/id{id_2}")