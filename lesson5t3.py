# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
from functools import reduce

with open("Примеры_файлов/employees.txt", 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    employees = [(employee.split()[0], float(employee.split()[1])) for employee in lines]
    print(f'Сотрудники с зарплатой меньше 20000: {list(filter(lambda x: x[1] < 20000, employees))}')
    print(f'Средняя зарплата: {reduce(lambda x, y: x + y, map(lambda x: x[1], employees)) / len(employees)}')
