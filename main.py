
cook_book = {}
with open('cook_book.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name_dishes = line.strip()
        recipes = []
        count_of_persons = f.readline()
        #print(count_of_persons)
        for i in range(int(count_of_persons)):
            count_of_pers = f.readline()
            ingredients, quantity, measure = count_of_pers.strip().split(' | ')
            recipes.append({'ingredient_name': ingredients,
                        'quantity': int(quantity),
                        'measure': measure})
        dish = {name_dishes: recipes}
        line_2 = f.readline()
        cook_book.update(dish)
    print(f'cook_book: = {cook_book}')


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in ingredients_list:
                    ingredients_list[ingredient['ingredient_name']]['quantity'] += (ingredient['quantity'] * person_count)
                else:
                    ingredients_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                          'quantity': (ingredient['quantity'] * person_count)}
        else:
            print('Такого блюда нет в кулинарной книге')
    return ingredients_list
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2))