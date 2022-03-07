from abc import ABC

class Clothes(ABC):

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2


    def rasch(self):
        pass




    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани  {(self.param1 / 6.5 + 0.5) + (self.param2 * 2 + 0.3)}')


class Coat(Clothes):


    @property
    def rasch(self):
        return self.param1 / 6.5 + 0.5

class suit(Clothes):


    @property
    def rasch(self):
        return self.param2 * 2 + 0.3

clothes_r = Clothes(52, 4)
Suit_r = suit(52, 4)
Coat_r = Coat(52, 4)
print(suit)
print(Coat)
print(Clothes.get_sq_full)
print(f'Площадь ткани на костюм {Suit_r.rasch}')
print(f'Площадь ткани на пальто {Coat_r.rasch}')
print(clothes_r.get_sq_full)


