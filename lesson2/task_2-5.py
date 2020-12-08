my_list = [8, 7, 5, 5, 3]
new_el = input('Введите новый элемент рейтинга (целое положительное число)\n')
while new_el.isdigit() == 0:
    new_el = input('Нужно ввести целое положительное число. Попробуйте еще раз\n')
new_el = int(new_el)
print(f'Исходный рейтинг: {my_list}')
if new_el <= my_list[-1]:
    my_list.append(new_el)
else:
    for el in my_list:
        if el < new_el:
            my_list.insert(my_list.index(el), new_el)
            break
        else:
            i = my_list.index(el) + 1
print(f'Новый рейтинг: {my_list}')
input('Нажмите Enter для завершения')
