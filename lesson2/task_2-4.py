words_str = input('Введите строку из нескольких слов, разделенных пробелом\n')
words_str = words_str.replace(',', ' ')
words_str = words_str.replace(':', ' ')
words_str = words_str.replace(';', ' ')
words_str = words_str.replace('  ', ' ')
words_list = words_str.split(' ')
for ind, el in enumerate(words_list):
    print(f'{ind + 1} - {el[0:10:1].title()}')
input('Нажмите Enter для завершения работы')
