# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
from functools import reduce

with open('Примеры_файлов/text_5.txt', 'w', encoding='utf-8') as w_file:
    values = [randint(-1000, 1000) for val in range(100)]
    w_file.write(' '.join(map(str, values)))

with open('Примеры_файлов/text_5.txt', 'r', encoding='utf-8') as r_file:
    line = r_file.readline()
    val_sum = reduce(lambda x, y: x + y, map(int, line.split()))
    print(f'Сумма равна: {val_sum}')
