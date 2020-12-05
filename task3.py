n = input('Введите любое целое число\n')
m = 0
while n.isdigit() == 0:
    n = input('Вы ошиблись, нужно ввести целое число\n')
m = int(n) + int(n + n) + int(n + n + n)
print(f'{n} + {n + n} + {n + n + n} будет {m}!')
input('Нажмите Enter для завершения')
