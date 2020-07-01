import json

def top_ten_words_news_json(file):
   ''' для файлов .json'''
   with open(file, encoding="utf-8") as f:
      json_data = json.load(f)

   news_list = json_data["rss"]["channel"]["items"]
   list_news = []
   for news in news_list:
       list_news.extend(news["description"].split(' '))
   print('для файлов .json')
   top_ten_words_news(list_news)

def top_ten_words_news(list_news):
   ''' функция, которая выводит топ 10 самых часто встречающихся в новостях слов длиннее 6 символов'''
   # создаём список всех слов в новостях
   word_list = []
   for word in list_news:
       if len(word) > 6:
           word_list.append(word)

   # создаём словарь с колличеством повторений
   words = {}
   for word in set(word_list):
      repeats = word_list.count(word)
      words[word] = repeats

   top_ten = {}
   repeat = sorted(words.values())
   for i in range(10):
      for k, v in words.items():
          if v == repeat[len(repeat) - 1 - i] and len(top_ten) < 10:
             top_ten[k] = v

   for word in top_ten.keys():
      print(f'слово "{word}" встречается "{top_ten[word]}" раз')

top_ten_words_news_json("newsafr.json")



