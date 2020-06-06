"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    date = ''

    def __init__(self, date):
        MyDate.date = date

    @classmethod
    def convert_date(cls):
        return [int(item) for item in cls.date.split('-')]

    @staticmethod
    def date_validation():
        date = MyDate.convert_date()
        if 0 < date[0] <= 31:
            if 0 < date[1] <= 12:
                return True
        return False


MyDate('20-45-2020')
print(MyDate.convert_date())
print(MyDate.date_validation())

MyDate('20-06-2020')
print(MyDate.convert_date())
print(MyDate.date_validation())