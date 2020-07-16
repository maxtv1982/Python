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
    def __and__(self, user):
        friends1 = set(self.friends())
        friends2 = set(user.friends())
        print(f'общие друзья пользователей - {friends1.intersection(friends2)}')

    def __str__(self):
        return f"профиль пользователя c id={self.UserID} https://vk.com/id{self.UserID}"


id_1 = input('Введите id первого пользователя: ')
id_2 = input('Введите id второго пользователя: ')

User1 = UserVK(id_1)
User2 = UserVK(id_2)

User1 & User2

print(User1)
print(User2)
