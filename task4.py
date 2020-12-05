n = int(input('Введите любое целое число\n'))
m = n % 10
while n > 10:
    if n % 10 > m: m = n % 10
    n = int(n / 10)
if n > m: m = n
print(f'Самая большая цифра в числе - {m}')
input('Нажмите Enter для завершения')

