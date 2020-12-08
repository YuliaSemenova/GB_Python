new_list = [1, 2, 2, 14.5, [1, 2, 10], 'some text', True, ('some tuple text', 15, 10 + 2j), {1, 2, 6, 8},
            {'a': 15, 'b': 55}, 5j + 18]
class_dict = {
    'int': 'целое число', 'float': 'дробное число', 'list': 'список', 'str': 'строка', 'tuple': 'кортеж',
    'set': 'множество', 'dict': 'словарь', 'bool': 'логическое значение', 'complex': 'комплексное число'}
print(f'Всего в списке {len(new_list)} элементов')
for ind, el in enumerate(new_list):
    if type(el) == list or type(el) == set or type(el) == tuple or type(el) == dict:
        print(f'Элемент {ind + 1} - {class_dict.get(str(type(el))[8:-2:1])} из {len(el)} элементов')
    else:
        print(f'Элемент {ind + 1} - {class_dict.get(str(type(el))[8:-2:1])}')
input('Нажмите Enter для завершения')
