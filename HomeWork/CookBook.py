from pprint import pprint

def ingr_to_dict(ing_str):
    ''' преобразуем информацию об ингредиенте в словарь'''
    ingredient_info = dict()
    ingredient = list(ing_str.split('|'))
    ingredient_info['ingredient_name'] = ingredient[0]
    ingredient_info['quantity'] = int(ingredient[1])
    ingredient_info['measure'] = ingredient[2]
    return ingredient_info

with open('recipes.txt') as filecook:
   cookbook = dict()
   while True:
        dish = filecook.readline().rstrip()
        num_ingredients_dish = filecook.readline().rstrip()

        if not dish or not num_ingredients_dish:
            break

        ingredients = []
        for i in range(int(num_ingredients_dish)):
            ingredients.append(ingr_to_dict(filecook.readline().rstrip()))
        cookbook[dish] = ingredients

        filecook.readline()

#print(cookbook)

def get_shop_list_by_dishes(dishes, person_count):
   ''' состовляем список покупок'''

   shop_list = dict()
   for meal in dishes:
      for ingr in cookbook[meal]:
          c = int(person_count)
          if ingr['ingredient_name'] in shop_list.keys():
             c = 2*c
          shop_list[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': ingr['quantity']*c}

   pprint(shop_list)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
