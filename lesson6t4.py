"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from enum import Enum, auto
from random import choice


class Direction(Enum):
    LEFT = "лево"
    RIGHT = "право"


class Car:
    speed = .0
    color = ""
    name = ""
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} начал движение")

    def stop(self):
        print(f"{self.name} остановился")

    def turn(self, direction):
        print(f"{self.name} повернула на{direction}")

    def show_speed(self):
        print(f"{self.name} передвигается со скоростью {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} превышает. Его скорость составляет {self.speed} км/ч")
        else:
            print(f"{self.name} передвигается со скоростью {self.speed} км/ч")


class SportCar(Car):
    def TurnTurbo(self, enable):
        print(f"{self.name} {'включил' if enable else 'выключил'} турбо режим")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} превышает. Его скорость составляет {self.speed} км/ч")
        else:
            print(f"{self.name} передвигается со скоростью {self.speed} км/ч")


class PoliceCar(Car):
    def TurnLight(self, enable):
        print(f"{self.name} {'включил' if enable else 'выключил'} сирену")


cars = [TownCar(40, "Серый", "Городской автомобиль 1", False),
        TownCar(120, "Черный", "Городской автомобиль 2", False),
        SportCar(180, "Красный", "Спортивный автомобиль", False),
        WorkCar(40, "Желтый", "Рабочий автомобиль 1", False),
        WorkCar(50, "Оранжевый", "Рабочий автомобиль 2", False),
        PoliceCar(80, "Синий", "Полицейский автомобиль", True)]

for car in cars:
    car.show_speed()
    if car.is_police:
        car.TurnLight(True)
    else:
        car.turn(choice(list(Direction)).value)
    if car.name == "Спортивный автомобиль":
        car.TurnTurbo(False)
