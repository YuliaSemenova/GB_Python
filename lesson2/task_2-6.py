product_tuple = ()
product_list = []
product_dict = {}
final_dict = {}
count = 1
name_set = set()
price_set = set()
measure_set = set()
amount_set = set()
add = ''
while True:
    if count > 1:
        add = 'следующего '
    product_name = input(f'Введите название {add}товара (для выхода из меню нажмите Enter)\n')
    if product_name == '':
        break
    product_price = input(f'Введите цену товара "{product_name}", руб.\n')
    while product_price.isdigit() == 0:
        product_price = input('Цена товара должна быть числом. Введите еще разок\n')
    product_msr = input(f'Введите единицу измерения товара "{product_name}"\n')
    product_amount = input(f'Введите количество товара "{product_name}", {product_msr}\n')
    while product_amount.isdigit() == 0:
        product_amount = input('Количество товара должно быть числом. Введите ещё разок\n')
    product_dict = {'name': product_name, 'price': product_price, 'measure': product_msr, 'amount': product_amount}
    product_tuple = (count, product_dict)
    product_list.append(product_tuple)
    name_set.add(product_name)
    price_set.add(product_price)
    measure_set.add(product_msr)
    amount_set.add(product_amount)
    final_dict = {'name': list(name_set), 'price': list(price_set), 'measure': list(measure_set),
                  'amount': list(amount_set)}
    count += 1
if len(product_list) != 0:
    print('Исходный список')
    print('-' * 16)
    for i in product_list:
        print(i)
if len(final_dict) != 0:
    print('\n')
    print('Словарь с аналитикой')
    print('-' * 21)
    for i in final_dict:
        print(i, final_dict[i])
input('До свидания! Нажмите Enter для завершения')
