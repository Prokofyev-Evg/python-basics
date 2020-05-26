# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("Примеры_файлов/employees.txt", 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    print(f'Количество строк: {len(lines)}')
    for i, line in enumerate(lines):
        print(f'Количество слов в {i+1}-й строке: {len(line.split())}')
