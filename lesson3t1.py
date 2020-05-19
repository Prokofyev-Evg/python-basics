# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def divide(divisible, divisor):
    try:
        return divisible / divisor
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль")


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

print(f'Частное = {divide(a, b)}')
