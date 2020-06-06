"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
    который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
    уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
    определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
    других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
    указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
    уроках по ООП.
"""
from enum import Enum


class OutOfRangeException(Exception):
    def __init__(self, txt):
        self.txt = txt


class NegativeException(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, wh=None):
        self.warehouse = wh if wh else []

    def restock(self, office_equipment_list):
        self.warehouse.extend(office_equipment_list)

    def fetch(self, eq_type, brand_name, model_name):
        """
        Прием оргтехники
        """
        temp_list = self.warehouse
        if eq_type:
            temp_list = (x for x in temp_list if x.type == eq_type)
        if brand_name:
            temp_list = (x for x in temp_list if x.brand_name == brand_name)
        if model_name:
            temp_list = (x for x in temp_list if x.model_name == model_name)
        return list(temp_list)

    def give_out(self, eq_type=None, brand_name=None, model_name=None):
        """
        Передача оргтехники
        """
        item = None
        temp_list = self.fetch(eq_type, brand_name, model_name)
        if len(temp_list) >= 1:
            item = temp_list.pop()
            self.warehouse.remove(item)
        return item

    def count(self, eq_type=None, brand_name=None, model_name=None):
        """
        Подсчет количества оргтехники
        """
        temp_list = self.fetch(eq_type, brand_name, model_name)
        return len(temp_list)

    def __str__(self):
        return str('\n'.join(map(str, self.warehouse)))


class OfficeEquipment:
    class OfficeEquipmentType(Enum):
        Printer = 0
        Scanner = 1
        Xerox = 2

    def __init__(self, brand_name, model_name, office_equipment_type):
        self.brand_name = brand_name
        self.model_name = model_name
        self.type = office_equipment_type

    def __str__(self):
        return f"{self.brand_name} - {self.model_name}"


class Printer(OfficeEquipment):
    class PrinterType(Enum):
        Laser = 0
        InkJet = 1

    def __init__(self, brand_name, model_name, printer_type):
        super().__init__(brand_name, model_name, OfficeEquipment.OfficeEquipmentType.Printer)
        self.printer_type = printer_type

    def __str__(self):
        return f"Принтер - " + super().__str__()


class Scanner(OfficeEquipment):
    class ScannerType(Enum):
        HandHeld = 0
        FeedIn = 1
        FlatBed = 2

    def __init__(self, brand_name, model_name, scanner_type):
        super().__init__(brand_name, model_name, OfficeEquipment.OfficeEquipmentType.Scanner)
        self.scanner_type = scanner_type

    def __str__(self):
        return f"Сканер - " + super().__str__()


class Xerox(OfficeEquipment):
    class XeroxType(Enum):
        Mono = 0
        Color = 1

    def __init__(self, brand_name, model_name, xerox_type):
        super().__init__(brand_name, model_name, OfficeEquipment.OfficeEquipmentType.Xerox)
        self.xerox_type = xerox_type

    def __str__(self):
        return f"Ксерокс - " + super().__str__()


def input_choice_validation(text, choices):
    param = []
    for i, choice in enumerate(choices):
        param.append(f'{i} - {choice}')
    msg = f'{text} [{", ".join(param)}]? '
    flag = False
    ix = 0
    while not flag:
        try:
            ix = int(input(msg))
            if ix not in range(len(choices)):
                raise OutOfRangeException(f'Доступен ввод в диапазоне 0 - {len(choices) - 1}')
        except ValueError:
            print('Ошибка, разрешен ввод только чисел')
        except OutOfRangeException as err:
            print(err.txt)
        else:
            flag = True
    return ix


def input_count_validation(text):
    flag = False
    count = 0
    while not flag:
        try:
            count = int(input(text))
            if count <= 0:
                raise NegativeException(f'Число должно быть больше 1')
        except ValueError:
            print('Ошибка, разрешен ввод только чисел')
        except OutOfRangeException as err:
            print(err.txt)
        else:
            flag = True
    return count


def add_office_equipment():
    val = input_choice_validation('Что принять', ['Принтер', 'Сканер', 'Ксерокс'])
    brand_name = input("Введите имя бренда: ")
    model_name = input("Введите модель: ")
    item = None
    if val == 0:
        eq_type = input_choice_validation('Какой тип', ['Laser', 'InkJet'])
        item = Printer(brand_name, model_name, eq_type)
    elif val == 1:
        eq_type = input_choice_validation('Какой тип', ['HandHeld', 'FeedIn', 'FlatBed'])
        item = Scanner(brand_name, model_name, eq_type)
    elif val == 2:
        eq_type = input_choice_validation('Какой тип', ['Mono', 'Color', 'FlatBed'])
        item = Xerox(brand_name, model_name, eq_type)
    items = []
    count = input_count_validation("Введите количество: ")
    for _ in range(count):
        items.append(item)
    return items


def give_out_office_equipment():
    val = input_choice_validation('Что хотите передать', ['Принтер', 'Сканер', 'Ксерокс'])
    eq_type = OfficeEquipment.OfficeEquipmentType(val)
    query = input_choice_validation('Какой передать', ['любой', 'выбрать по бренду', 'выбрать модель'])
    if query == 0:
        item = warehouse.give_out(eq_type=eq_type)
    elif query == 1:
        brand_name = input("Введите имя бренда: ")
        item = warehouse.give_out(eq_type=eq_type, brand_name=brand_name)
    else:
        model_name = input("Введите модель: ")
        item = warehouse.give_out(eq_type=eq_type, model_name=model_name)
    return item


def run_stock_app():
    cmd = ''
    while cmd != 'stop':
        cmd = input_choice_validation("Какое действие хотите совершить", ['вывести остаток',
                                                                          'принять оргтехнику',
                                                                          'передать оргтехнику'])
        if cmd == 0:
            print(warehouse)
        elif cmd == 1:
            item = add_office_equipment()
            if item:
                warehouse.restock(item)
        elif cmd == 2:
            item = give_out_office_equipment()
            print(item)


warehouse = Warehouse()
run_stock_app()
