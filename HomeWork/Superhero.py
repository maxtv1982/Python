import requests

superhero = ['Hulk', 'Captain America', 'Thanos']


def hero_intelligence(name):
    url_name = (f'https://superheroapi.com/api/2619421814940190/search/{name}')
    resp_id = requests.get(url_name)
    character_id = resp_id.json()['results'][0]['id']
    url_id = ('https://superheroapi.com/api/2619421814940190/' + character_id + '/powerstats')
    resp_intelligence = requests.get(url_id)
    return resp_intelligence.json()['intelligence']


max_intelligence = 0
name_hero = ''
for hero in superhero:
    intelligence = int(hero_intelligence(hero))
    if intelligence > max_intelligence:
        max_intelligence = intelligence
        name_hero = hero

print(f'самый умный c intelligence = {max_intelligence}, это - {name_hero}')
