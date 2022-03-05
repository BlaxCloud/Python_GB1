from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    @abstractmethod
    def rasch1(ABS):
        pass
        #return self.param1 / 6.5 + 0.5

    @abstractmethod
    def rasch2(ABS):
        pass
        #return self.param2 / 6.5 + 0.5

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.param1 / 6.5 + 0.5) + (self.param2 * 2 + 0.3)}')
    # @property
    # def square(self):
    #     return (self.size / 6.5 + 0.5) + (self.growth * 2 + 0.3)

class Coat(Clothes):


    @property
    def rasch1(self):
        return self.param1 / 6.5 + 0.5

class suit(Clothes):


    @property
    def rasch2(self):
        return self.param2 * 2 + 0.3

#clothes_r = Clothes(4,52)

Suit_r = suit(4)
Coat_r = Coat(52)
print(suit)
print(Coat)
print(f'Площадь ткани на костюм {Suit_r.rasch1}')
print(f'Площадь ткани на пальто {Coat_r.rasch2}')
print(f'Общая площаль ткани {Suit_r.rasch1 + Coat_r.rasch2} ')
print(Clothes.get_sq_full)
#print(f'Общая площадь ткани {Clothes.square}')