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
    print(menu)