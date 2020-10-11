import requests
# import vk_api
# from vk_api.longpoll import VkLongPoll, VkEventType

token = 'ba79b7b6ba79b7b6ba79b7b6d4ba0abaa4bba79ba79b7b6e50f968240536031b140d0aa'  # здесь вы должны написать свой access_token
data = requests.get('https://api.vk.com/method/messages.getLongPollServer', params={'access_token': token, 'v': 5.21}).json()  # получение ответа от сервера
print(data)