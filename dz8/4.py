class Stock:
  def __init__(self):
    self._dict = {}

  def add_to(self, Technique):
    self._dict.setdefault(Technique.lable, []).append(Technique.model)

  # def __init__(self, type, number, model):
  #     self.type = type
  #     self.number = number
  #     self.model = model

  # def __str__(self):
  #     return f'На складе находится {self.type}ов {self.model} {self.number} шт'



class Technique:
    model: str
    price: int
    lable: str



    def __init__(self, model, price, lable):
        self.lable = lable
        self.price = price
        self.model = model

    def __repr__(self):
        return str(
            f' {self.model} по цене {self.price}   на складе')


class Printer(Technique):
    capasity: float

    def __init__(self, lable, model, price, capasity):
        super().__init__(model, price, lable)
        self.capasity = capasity
        self.price = price
        self.lable = lable
        self.model = model


    # def __str__(self):
    #     return str(f'Принтера {self.model} модели {self.model} по цене {self.price} емкостью {self.capasity} на складе ')

class Scanner(Technique):
    scan_speed: float

    def __init__(self, lable, model, price, scan_speed):
        super().__init__(model, price, lable)
        self.scan_speed = scan_speed
        self.price = price
        self.lable = lable
        self.model = model




class Xerox(Technique):
    Xerox_speed: float

    def __init__(self,lable, model, price,  Xerox_speed):
        super().__init__(model, price, lable)
        self.Xerox_speed = Xerox_speed
        self.price = price
        self.lable = lable
        self.model = model




Stock = Stock()
printer = Printer('Hp', 'Z850', '123334', '400')
scanner = Scanner('Hp', 'H033', '234455', '150')
xerox = Xerox('Xerox', 'L033', '42343425', '50')
Stock.add_to(scanner)
Stock.add_to(xerox)
Stock.add_to(xerox)



# создаем объект и добавляем
# scaner = Scaner('hp','321', 90)
# sklad.add_to(scaner)
# scaner = Scaner('hp','311', 97)
# sklad.add_to(scaner)
# scaner = Scaner('hp','330', 99)
# sklad.add_to(scaner)
#print(Printer.model)
print(Stock._dict)



