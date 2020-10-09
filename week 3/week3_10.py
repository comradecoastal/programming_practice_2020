big_dict = dict()

# заполнение соваря со словарями в формате {имя: {продукт: количество}}
# для каждого имени и продукта проверям встречались ли они раньше
while True:
    # пытаемся считать строку, если это не получается разрываем цикл
    try:
        line = input()
    except EOFError:  # если строчки кончелись то разрываем цикл
        break

    name, item, count = line.split()
    count = int(count)
    if name in big_dict:
        if item in big_dict[name]:
            big_dict[name][item] += count
        else:
            big_dict[name][item] = count
    else:
        big_dict[name] = {item: count}

# делаем список всех имён и сортируем его в нужном порядке
names = list(big_dict.keys())
names.sort()

# теперь проходимся по именам в отсортированном списке
for name in names:
    print(name + ':')
    # для кажного имени делаем отсортированный список продуктов
    items = list(big_dict[name].keys())
    items.sort()
    for item in items:
        print(item, big_dict[name][item])
