"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""
class MyZeroDivisionException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    if b == 0:
        raise MyZeroDivisionException("Делитель должен быть отличен от нуля")
except ValueError:
    print('Ошибка ввода, введите число')
except MyZeroDivisionException as err:
    print(err)
else:
    c = a / b
    print(f'Результат деления - {c}')
finally:
    print('Конец программы')
