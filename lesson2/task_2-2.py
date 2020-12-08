el_number = input('Введите желаемое количество элементов списка\n')
my_list = list()
while el_number.isdigit() == 0:
    el_number = input('Нужно ввести целое положительное число. Введите ещё раз\n')
el_number = int(el_number)
i = 0
while i < el_number:
    my_list.append(input(f'Введите {i + 1}-й элемент списка из {el_number}\n'))
    i += 1
print(f'Исходный список: {my_list}')
if el_number % 2 > 0:
    el_number = el_number - 1
i = 0
while i < el_number:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print(f'Новый список: {my_list}')
input('Нажмите Enter для завершения')
