"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __str__(self):
        return f'{self.re} + i * {self.im}'


z1 = Complex(2, 3)
z2 = Complex(-1, 1)

print(f'({z1}) + ({z2}) = {z1 + z2}')
print(f'({z1}) * ({z2}) = {z1 * z2}')
