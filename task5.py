rev = int(input('Введите сумму выручки\n'))
cost = int(input('Введите сумму издержек\n'))
result = rev - cost
if result < 0:
    print(f'Убыток составил {result} рублей')
else:
    print(f'Прибыль составила {result} рублей. Рентабельность {result/rev*100:.2f}%')
    staff = int(input('Сколько у вас сотрудников?\n'))
    print(f'Прибыль на одного сотрудника составила {result/staff:.2f} рублей')
input('Нажмите Enter для завершения')
