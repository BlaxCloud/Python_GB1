class Technique:
    type: str
    lable: str
    model: str
    price: int
    number: int

    def __init__(self, lable, model, price, type, number):
        self.model = model
        self.price = price
        self.lable = lable
        self.type = type
        self.number = number

    def __repr__(self):
        return str(f'Марка: {self.lable} Модель: {self.model} Цена: {self.price} Количество: {self.number} шт.')


class ModelTypeException(Exception):
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Тип техники не может быть числовым. "


class Stock:
    # max_count: int
    technique: dict

    def __init__(self):
        # self.max_count = count
        self.technique = {}

    def store(self, Technique):

        if Technique.type.isdigit():
            raise ModelTypeException(Technique.type)

        self.technique.setdefault(Technique.type, []).append(Technique)


class Printer(Technique):
    capasity: float

    def __init__(self, type, lable, model, price, number, capasity):
        super().__init__(type, lable, model, price, number)
        self.capasity = capasity
        self.price = price
        self.lable = lable
        self.model = model
        self.type = type
        self.number = number


class Scanner(Technique):
    scan_speed: float

    def __init__(self, type, lable, model, price, number, scan_speed):
        super().__init__(type, lable, model, number, price)
        self.scan_speed = scan_speed
        self.price = price
        self.lable = lable
        self.model = model
        self.type = type
        self.number = number


class Xerox(Technique):
    Xerox_speed: float

    def __init__(self, type, lable, model, price, number, Xerox_speed):
        super().__init__(type, lable, model, number, price)
        self.Xerox_speed = Xerox_speed
        self.price = price
        self.lable = lable
        self.model = model
        self.type = type
        self.number = number


Stock = Stock()
printer = Printer('Принтер', 'Hp', 'Z850', '12333', '20', '400')
scanner = Scanner('Сканер', 'Hp', 'H033', '23445', '25', '150')
xerox = Xerox('Ксерокс', 'Xerox', 'L033', '42343', ' 30', '50')
Stock.store(scanner)
Stock.store(printer)
Stock.store(xerox)
print(Stock.technique)