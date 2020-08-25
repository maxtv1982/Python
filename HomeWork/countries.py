import json


class Country_in_wiki:
    def __init__(self, file):
        self.file = file
        with open(self.file, encoding="utf-8") as f:
            self.json_data = json.load(f)

    def __next__(self):
        country_wiki = dict()
        for country in self.json_data:
            country_wiki[country['name']['common']] = f"https://en.wikipedia.org/wiki/{country['name']['common']}"
        with open("country_wiki.json", "w") as f:
            json.dump(country_wiki, f, indent=4)

    def __iter__(self):
        pass
        return self


next(Country_in_wiki('countries.json'))
