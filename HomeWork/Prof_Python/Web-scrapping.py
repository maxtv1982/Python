# определяем список хабов, которые нам интересны
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'программ']

import requests
import re
from bs4 import BeautifulSoup

# получаем страницу с самыми свежими постами
ret = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(ret.text, 'html.parser')
# извлекаем посты
posts = soup.find_all('article', class_='post')
for post in posts:
    # извлекаем preview-информацию статьи поста
    previews = map(lambda h: h.text.lower(), post.find_all('div', class_='post__body'))
    for preview in previews:
        for word in KEYWORDS:
            # ищем вхождение хотя бы одного желаемого слова
            if re.search(word, preview):
                title_element = post.find('a', class_='post__title_link')
                print('дата статьи:', post.find('span', class_='post__time').text,
                      '- заголовок:', title_element.text,
                      '- ссылка:', title_element.attrs.get('href'))
                # так как пост уже нам подошел - дальше нет смысла проверять хабы
                break

