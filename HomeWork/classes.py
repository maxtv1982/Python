class Animal:
    ''' создаём общий класс животных, в котором будем производить все действия с ними'''

    all_animals = {}

    def __init__(self, name, weight, voice):
      self.name = name
      self.voice = voice
      self.weight = weight
      self.all_animals[name] = weight

    def eat(self):
       print(f'{self.__class__.__name__} {self.name} - покормили')

class Bird(Animal):
    '''  Создаём подкласс птиц '''

    def egg(self):
        print(f'{self.__class__.__name__} {self.name} - собрали яйца')

class GiveMilkAnimal(Animal):
    '''  Создаём подкласс животных, дающих молоко '''

    def milk(self):
        print(f'{self.__class__.__name__} {self.name} - подоили')

class Goose(Bird):
    '''  Создаём подкласс гусей '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Га-га')

class Cow(GiveMilkAnimal):
    '''  Создаём подкласс коров '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Му-му')

class Sheep(Animal):
    '''  Создаём подкласс овец '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Бе-бе')

    def cut(self):
      print(f'{self.__class__.__name__} {self.name} - подстригли')

class Chiken(Bird):
    '''  Создаём подкласс куриц '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Ко-ко')

class Goat(GiveMilkAnimal):
    '''  Создаём подкласс коз '''

    def __init__(self, name, weight):
      super().__init__(name, weight, 'Ме-ме')

class Duck(Bird):
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

print('Общий вес всех животных: ', sum(Animal.all_animals.values()))

''' Ищем животное с максимальным весом'''
max_weight = max(Animal.all_animals.values())
for n, w in Animal.all_animals.items():
   if w == max_weight:
      print(f'самый большой вес - {w}кг у {n}')