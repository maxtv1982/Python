import requests
import os
from pprint import pprint

URL = 'https://reddit.com/r/gifs/top.json'

headers = {'User-Agent': 'Netology-Code'}
param = {'limit': 10}

resp = requests.get(URL, params=param, headers=headers)
resp_json = resp.json()
children = resp_json['data']['children']
for child in children:
   child_data = child['data']
   gif_url =  child_data['url']

   if 'imgur' not in gif_url:
       continue
   #print(gif_url)

   filename = f"{child_data['id']} - {child_data['title']}.mp4"
   full_filename = os.path.join('gifs/', filename)
   print(full_filename)

   download_url = gif_url.replace('.gifv', '.mp4')
   print(download_url)

   img_resp = requests.get(download_url)
   with open(C:/Users/USER/Downloads/filename, 'wb') as f:
       f.write(img_resp.content)

