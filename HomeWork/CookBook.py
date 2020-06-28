from pprint import pprint

def info_ingredient_to_dict(ing_str):
    ''' преобразуем информацию об ингредиенте в словарь'''

    ingredient_info = dict()
    ingredient = list(ing_str.split('|'))
    ingredient_info['ingredient_name'] = ingredient[0]
    ingredient_info['quantity'] = int(ingredient[1])
    ingredient_info['measure'] = ingredient[2]
    return ingredient_info

def make_cook_book(file):
    ''' создаём кулинарную книгу '''
    
    with open(file) as file_cook:
       cook_book = dict()
       while True:
           dish = file_cook.readline().rstrip()
           num_ingredients_dish = file_cook.readline().rstrip()

           if not dish or not num_ingredients_dish:
              break

           ingredients = []
           for i in range(int(num_ingredients_dish)):
               ingredients.append(info_ingredient_to_dict(file_cook.readline().rstrip()))
           cook_book[dish] = ingredients

           file_cook.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
   ''' состовляем список покупок'''

   shop_list = dict()
   count = int(person_count)
   for meal in dishes:                                      # итерация по блюдам в списке
      for ingredients in cook_book[meal]:                   # итерация по ингридиентам в блюде
          if ingredients['ingredient_name'] in shop_list.keys():  # ищем повторяющиеся ингридиенты
              ingredient_repeat = (ingredients['quantity'] * count) + \
                                  shop_list[ingredients['ingredient_name']]['quantity']
              shop_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'], \
                        'quantity': ingredient_repeat}
          else:
              shop_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'], \
                    'quantity': ingredients['quantity'] * count}

   return shop_list



cook_book = make_cook_book('recipes.txt')
#pprint(cook_book)

shop_list = get_shop_list_by_dishes(['Фахитос', 'Фахитос', 'Омлет', 'Омлет', 'Омлет'], 2)
pprint(shop_list)