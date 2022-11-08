import os
current = os.getcwd()
file_name = 'resipe.txt'

full_path = os.path.join(current, file_name)

with open(full_path, 'rt', encoding="utf-8") as file:
    menu = {}
    for line in file:
        dish = line.strip()
        quantitys = int(file.readline().strip())
        food = []
        for x in range(quantitys):
            ingridient = file.readline().strip().split(' | ')
            dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
            for item in ingridient:
                dish_items['ingredient_name'] = ingridient[0]
                dish_items['quantity'] = ingridient[1]
                dish_items['measure'] = ingridient[2]
            food.append(dish_items)
        cook_book = {dish: food}
        menu.update(cook_book)
        file.readline()

    print('Ознакомьтесь с Нашим меню :')
    print()
    for dish in menu:
        print(dish)
    print()

    def get_shop_list_by_dishes(dishes, person_count):
        shopping_list = {}
        try:
            for dish in dishes:
                for item in (menu[dish]):
                    items_list = dict([(item['ingredient_name'],
                                        {'measure': item['measure'],
                                         'quantity': int(item['quantity']) * person_count})])
                    if shopping_list.get(item['ingredient_name']):
                        quantity_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                         int(items_list[item['ingredient_name']]['quantity']))
                        shopping_list[item['ingredient_name']]['quantity'] = quantity_item
                    else:
                        shopping_list.update(items_list)
            print(f"Для приготовления блюд на {person_count} человек  нам необходимо купить:")
            print(shopping_list)
        except KeyError:
            print("Вы ошиблись в названии блюда, проверьте ввод")

get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3)


