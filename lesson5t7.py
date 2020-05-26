# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
from functools import reduce
import json

with open('Примеры_файлов/text_77.json', 'w', encoding='utf-8') as w_file:
    with open('Примеры_файлов/text_7.txt', 'r', encoding='utf-8') as r_file:
        lines = r_file.readlines()
        firms = [line.split() for line in lines]
        profit = {cells[0]: int(cells[2]) - int(cells[3]) for cells in firms}
        positive_profit = list(filter(lambda x: x > 0, profit.values()))
        average_profit = reduce(lambda x, y: x + y, positive_profit) / len(positive_profit)

        json.dump([profit, {'average_profit': average_profit}], w_file, ensure_ascii=False)
        print(f'{profit}')
        print(average_profit)