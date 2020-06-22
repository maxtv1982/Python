class Animal:
    ''' создаём общий класс животных, в котором будем производить все действия с ними'''

    def __init__(self, name, weight, voice):
      self.name = name
      self.voice = voice
      self.weight = weight

    def eat(self):
       print(f'{self.__class__.__name__} {self.name} - покормили')

    def milk(self):
        print(f'{self.__class__.__name__} {self.name} - подоили')

    def egg(self):
        print(f'{self.__class__.__name__} {self.name} - собрали яйца')

    def cut(self):
        print(f'{self.__class__.__name__} {self.name} - подстригли')

class Goose(Animal):
    '''  Создаём подкласс гусей '''
    def __init__(self, name, weight):
      super().__init__(name, weight, 'Га-га')

class Cow(Animal):
    '''  Создаём подкласс коров '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Му-му')

class Sheep(Animal):
    '''  Создаём подкласс овец '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Бе-бе')

class Chiken(Animal):
    '''  Создаём подкласс куриц '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Ко-ко')

class Goat(Animal):
    '''  Создаём подкласс коз '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Ме-ме')

class Duck(Animal):
    '''  Создаём подкласс уток '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Кря-кря')


goose1 = Goose('Серый', 10)
goose2 = Goose('Белый', 12)
goose1.eat()
goose1.egg()
goose2.eat()
goose2.egg()

cow1 = Cow('Манька', 200)
cow1.eat()
cow1.milk()

sheep1 = Sheep('Барашек', 60)
sheep2 = Sheep('Кудрявый', 70)
sheep1.eat()
sheep1.cut()
sheep2.eat()
sheep2.cut()

chiken1 = Chiken('Ко-ко', 7)
chiken2 = Chiken('Кукареку', 8)
chiken1.eat()
chiken1.egg()
chiken2.eat()
chiken2.egg()

goat1 = Goat('Рога', 17)
goat2 = Goat('Копыта', 18)
goat1.eat()
goat1.milk()
goat2.eat()
goat2.milk()

duck1 = Duck('Кряква', 6)
duck1.eat()
duck1.egg()

print('Общий вес всех животных: ', goose1.weight + goose2.weight + cow1.weight + sheep1.weight + sheep2.weight /
      + chiken1.weight + chiken2.weight + goat1.weight + goat2.weight + duck1.weight, 'кг')

all_animals = dict({goose1.name: goose1.weight, goose2.name: goose2.weight, cow1.name: cow1.weight,
                    sheep1.name: sheep1.weight, sheep2.name: sheep2.weight, chiken1.name: chiken1.weight,
                    chiken2.name: chiken2.weight, goat1.name: goat1.weight, goat2.name: goat2.weight,
                    duck1.name: duck1.weight})

''' Ищем животное с максимальным весом'''
max_weight = max(all_animals.values())
for n, w in all_animals.items():
  if w == max_weight:
      print(f'самый большой вес - {w}кг у {n}')